import logging
import threading
from flask import Flask
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from telegram.ext import (
    Application, CommandHandler, MessageHandler, ConversationHandler,
    filters, ContextTypes, CallbackContext
)
import database as db
from texts import t

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN = '7486227402:AAH0zRC_kgrdzgu1dr8yryHoId6GkDNCinM'

# ──────────────────── States ────────────────────
(
    LANG_SELECT, ROLE_SELECT,
    # Client reg
    CLIENT_NAME, CLIENT_PHONE, CLIENT_MENU,
    CLIENT_TRACK, CLIENT_CALC_W, CLIENT_CALC_L, CLIENT_CALC_W2, CLIENT_CALC_H,
    # Partner
    PARTNER_CODE, PARTNER_MENU,
    ACCEPT_PHOTO, ACCEPT_WEIGHT, ACCEPT_LENGTH, ACCEPT_WIDTH, ACCEPT_HEIGHT,
    ACCEPT_CLIENT_PHONE, ACCEPT_CONFIRM,
    HANDOFF_CONFIRM,
    # Admin
    ADMIN_CODE_STATE, ADMIN_MENU,
    ADD_PARTNER_NAME, ADD_PARTNER_LOCATION, ADD_PARTNER_CODE,
) = range(25)

# ──────────────────── Keyboards ────────────────────

def lang_keyboard():
    return ReplyKeyboardMarkup([['🇷🇺 Русский', '🇬🇧 English']], resize_keyboard=True, one_time_keyboard=True)


def role_keyboard(lang):
    return ReplyKeyboardMarkup([
        [t(lang, 'btn_client')],
        [t(lang, 'btn_partner')],
        [t(lang, 'btn_admin')],
    ], resize_keyboard=True, one_time_keyboard=True)


def client_menu_keyboard(lang):
    return ReplyKeyboardMarkup([
        [t(lang, 'btn_track'), t(lang, 'btn_history')],
        [t(lang, 'btn_calculator'), t(lang, 'btn_change_lang')],
        [t(lang, 'main_menu')],
    ], resize_keyboard=True)


def partner_menu_keyboard(lang):
    return ReplyKeyboardMarkup([
        [t(lang, 'btn_accept_parcel')],
        [t(lang, 'btn_my_parcels'), t(lang, 'btn_handoff')],
        [t(lang, 'btn_stats'), t(lang, 'main_menu')],
    ], resize_keyboard=True)


def admin_menu_keyboard(lang):
    return ReplyKeyboardMarkup([
        [t(lang, 'btn_network_stats')],
        [t(lang, 'btn_list_partners'), t(lang, 'btn_add_partner')],
        [t(lang, 'main_menu')],
    ], resize_keyboard=True)


def confirm_keyboard(lang):
    return ReplyKeyboardMarkup([
        [t(lang, 'btn_confirm'), t(lang, 'cancel')],
    ], resize_keyboard=True, one_time_keyboard=True)


def back_keyboard(lang):
    return ReplyKeyboardMarkup([[t(lang, 'back')]], resize_keyboard=True)


def yes_no_keyboard(lang, yes_text=None, no_text=None):
    yes = yes_text or t(lang, 'btn_confirm')
    no = no_text or t(lang, 'cancel')
    return ReplyKeyboardMarkup([[yes, no]], resize_keyboard=True, one_time_keyboard=True)


# ──────────────────── Helpers ────────────────────

def get_lang(context: ContextTypes.DEFAULT_TYPE, user_id: int) -> str:
    lang = context.user_data.get('lang')
    if lang:
        return lang
    client = db.get_client(user_id)
    if client:
        context.user_data['lang'] = client['lang']
        return client['lang']
    return 'ru'


def status_label(lang: str, status: str) -> str:
    mapping = {
        'accepted': t(lang, 'status_accepted'),
        'in_transit': t(lang, 'status_in_transit'),
        'delivered': t(lang, 'status_delivered'),
    }
    return mapping.get(status, status)


# ──────────────────── /start ────────────────────

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    await update.message.reply_text(
        t('ru', 'choose_language'),
        reply_markup=lang_keyboard()
    )
    return LANG_SELECT


async def lang_select(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if '🇷🇺' in text or 'Русский' in text:
        lang = 'ru'
    elif '🇬🇧' in text or 'English' in text:
        lang = 'en'
    else:
        await update.message.reply_text(t('ru', 'choose_language'), reply_markup=lang_keyboard())
        return LANG_SELECT

    context.user_data['lang'] = lang
    await update.message.reply_text(
        t(lang, 'choose_role'),
        reply_markup=role_keyboard(lang)
    )
    return ROLE_SELECT


async def role_select(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text

    if text in (t('ru', 'btn_client'), t('en', 'btn_client')):
        # Check if already registered
        client = db.get_client(update.effective_user.id)
        if client:
            context.user_data['lang'] = client['lang']
            lang = client['lang']
            await update.message.reply_text(
                t(lang, 'client_already_registered', name=client['name']),
                reply_markup=client_menu_keyboard(lang)
            )
            return CLIENT_MENU
        await update.message.reply_text(t(lang, 'client_enter_name'), reply_markup=ReplyKeyboardRemove())
        return CLIENT_NAME

    elif text in (t('ru', 'btn_partner'), t('en', 'btn_partner')):
        # Check if already linked
        partner = db.get_partner_by_telegram(update.effective_user.id)
        if partner:
            context.user_data['partner_id'] = partner['id']
            await update.message.reply_text(
                t(lang, 'partner_welcome', name=partner['name'], location=partner['location']),
                reply_markup=partner_menu_keyboard(lang)
            )
            return PARTNER_MENU
        await update.message.reply_text(t(lang, 'partner_enter_code'), reply_markup=ReplyKeyboardRemove())
        return PARTNER_CODE

    elif text in (t('ru', 'btn_admin'), t('en', 'btn_admin')):
        await update.message.reply_text(t(lang, 'admin_enter_code'), reply_markup=ReplyKeyboardRemove())
        return ADMIN_CODE_STATE

    else:
        await update.message.reply_text(t(lang, 'choose_role'), reply_markup=role_keyboard(lang))
        return ROLE_SELECT


# ──────────────────── CLIENT REGISTRATION ────────────────────

async def client_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    context.user_data['reg_name'] = update.message.text.strip()
    keyboard = ReplyKeyboardMarkup(
        [[KeyboardButton(t(lang, 'btn_share_phone'), request_contact=True)]],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    await update.message.reply_text(t(lang, 'client_enter_phone'), reply_markup=keyboard)
    return CLIENT_PHONE


async def client_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)

    # Must be a shared contact, not typed text
    if not update.message.contact:
        keyboard = ReplyKeyboardMarkup(
            [[KeyboardButton(t(lang, 'btn_share_phone'), request_contact=True)]],
            resize_keyboard=True,
            one_time_keyboard=True,
        )
        await update.message.reply_text(t(lang, 'phone_not_yours'), reply_markup=keyboard)
        return CLIENT_PHONE

    contact = update.message.contact
    # Verify the contact belongs to this Telegram account
    if contact.user_id != update.effective_user.id:
        keyboard = ReplyKeyboardMarkup(
            [[KeyboardButton(t(lang, 'btn_share_phone'), request_contact=True)]],
            resize_keyboard=True,
            one_time_keyboard=True,
        )
        await update.message.reply_text(t(lang, 'phone_not_yours'), reply_markup=keyboard)
        return CLIENT_PHONE

    phone = contact.phone_number
    if not phone.startswith('+'):
        phone = '+' + phone
    name = context.user_data.get('reg_name', 'User')
    db.register_client(update.effective_user.id, name, phone, lang)
    await update.message.reply_text(
        t(lang, 'client_registered', name=name),
        reply_markup=client_menu_keyboard(lang)
    )
    return CLIENT_MENU


# ──────────────────── CLIENT MENU ────────────────────

async def client_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text

    if text in (t('ru', 'btn_track'), t('en', 'btn_track')):
        await update.message.reply_text(t(lang, 'enter_tracking'), reply_markup=back_keyboard(lang))
        return CLIENT_TRACK

    elif text in (t('ru', 'btn_history'), t('en', 'btn_history')):
        parcels = db.get_client_parcels(update.effective_user.id)
        if not parcels:
            await update.message.reply_text(t(lang, 'no_parcels'), reply_markup=client_menu_keyboard(lang))
        else:
            lines = [t(lang, 'parcel_history')]
            for p in parcels:
                partner = db.get_partner_by_id(p['partner_id'])
                pname = partner['name'] if partner else '—'
                lines.append(
                    f"• {p['tracking']} | {status_label(lang, p['status'])} | {pname} | ${p['price']}"
                )
            await update.message.reply_text('\n'.join(lines), reply_markup=client_menu_keyboard(lang))
        return CLIENT_MENU

    elif text in (t('ru', 'btn_calculator'), t('en', 'btn_calculator')):
        await update.message.reply_text(t(lang, 'calc_enter_weight'), reply_markup=back_keyboard(lang))
        return CLIENT_CALC_W

    elif text in (t('ru', 'btn_change_lang'), t('en', 'btn_change_lang')):
        await update.message.reply_text(t(lang, 'choose_language'), reply_markup=lang_keyboard())
        return LANG_SELECT

    elif text in (t('ru', 'main_menu'), t('en', 'main_menu')):
        return await start(update, context)

    else:
        client = db.get_client(update.effective_user.id)
        await update.message.reply_text(
            t(lang, 'client_menu', phone=client['phone'] if client else '—'),
            reply_markup=client_menu_keyboard(lang)
        )
        return CLIENT_MENU


async def client_track(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text.strip()

    if text in (t('ru', 'back'), t('en', 'back')):
        client = db.get_client(update.effective_user.id)
        await update.message.reply_text(
            t(lang, 'client_menu', phone=client['phone'] if client else '—'),
            reply_markup=client_menu_keyboard(lang)
        )
        return CLIENT_MENU

    parcel = db.get_parcel_by_tracking(text)
    if not parcel:
        await update.message.reply_text(
            t(lang, 'parcel_not_found', tracking=text),
            reply_markup=client_menu_keyboard(lang)
        )
        return CLIENT_MENU

    partner = db.get_partner_by_id(parcel['partner_id'])
    dims = f"{parcel['length']}×{parcel['width']}×{parcel['height']} cm"
    info = t(lang, 'parcel_info',
             tracking=parcel['tracking'],
             status=status_label(lang, parcel['status']),
             partner=partner['name'] if partner else '—',
             weight=parcel['chargeable_weight'],
             dims=dims,
             price=parcel['price'],
             date=parcel['created_at'][:10])
    await update.message.reply_text(info, reply_markup=client_menu_keyboard(lang))

    if parcel['photo_file_id']:
        await update.message.reply_photo(
            photo=parcel['photo_file_id'],
            caption=t(lang, 'parcel_photo')
        )
    return CLIENT_MENU


# ──────────────────── CALCULATOR ────────────────────

async def calc_weight(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    if update.message.text in (t('ru', 'back'), t('en', 'back')):
        client = db.get_client(update.effective_user.id)
        await update.message.reply_text(
            t(lang, 'client_menu', phone=client['phone'] if client else '—'),
            reply_markup=client_menu_keyboard(lang)
        )
        return CLIENT_MENU
    try:
        w = float(update.message.text.replace(',', '.'))
        context.user_data['calc_weight'] = w
        await update.message.reply_text(t(lang, 'calc_enter_length'))
        return CLIENT_CALC_L
    except ValueError:
        await update.message.reply_text(t(lang, 'invalid_number'))
        return CLIENT_CALC_W


async def calc_length(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    try:
        context.user_data['calc_l'] = float(update.message.text.replace(',', '.'))
        await update.message.reply_text(t(lang, 'calc_enter_width'))
        return CLIENT_CALC_W2
    except ValueError:
        await update.message.reply_text(t(lang, 'invalid_number'))
        return CLIENT_CALC_L


async def calc_width(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    try:
        context.user_data['calc_w'] = float(update.message.text.replace(',', '.'))
        await update.message.reply_text(t(lang, 'calc_enter_height'))
        return CLIENT_CALC_H
    except ValueError:
        await update.message.reply_text(t(lang, 'invalid_number'))
        return CLIENT_CALC_W2


async def calc_height(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    try:
        h = float(update.message.text.replace(',', '.'))
        w_actual = context.user_data['calc_weight']
        l = context.user_data['calc_l']
        w = context.user_data['calc_w']
        vol, chargeable, price = db.calculate_price(w_actual, l, w, h)
        await update.message.reply_text(
            t(lang, 'calc_result', actual=w_actual, vol=vol, chargeable=chargeable, price=price),
            reply_markup=client_menu_keyboard(lang)
        )
        return CLIENT_MENU
    except ValueError:
        await update.message.reply_text(t(lang, 'invalid_number'))
        return CLIENT_CALC_H


# ──────────────────── PARTNER AUTH ────────────────────

async def partner_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    code = update.message.text.strip()
    partner = db.get_partner_by_code(code)
    if not partner:
        await update.message.reply_text(t(lang, 'partner_invalid_code'))
        return PARTNER_CODE
    db.link_partner_telegram(partner['id'], update.effective_user.id)
    context.user_data['partner_id'] = partner['id']
    await update.message.reply_text(
        t(lang, 'partner_welcome', name=partner['name'], location=partner['location']),
        reply_markup=partner_menu_keyboard(lang)
    )
    return PARTNER_MENU


# ──────────────────── PARTNER MENU ────────────────────

async def partner_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text
    partner_id = context.user_data.get('partner_id')

    if not partner_id:
        return await start(update, context)

    partner = db.get_partner_by_id(partner_id)
    if not partner:
        return await start(update, context)

    if text in (t('ru', 'btn_accept_parcel'), t('en', 'btn_accept_parcel')):
        await update.message.reply_text(t(lang, 'accept_send_photo'), reply_markup=back_keyboard(lang))
        return ACCEPT_PHOTO

    elif text in (t('ru', 'btn_my_parcels'), t('en', 'btn_my_parcels')):
        parcels = db.get_partner_parcels(partner_id)
        if not parcels:
            await update.message.reply_text(t(lang, 'no_parcels_at_point'), reply_markup=partner_menu_keyboard(lang))
        else:
            lines = [t(lang, 'parcels_at_point')]
            for p in parcels:
                lines.append(t(lang, 'parcel_line',
                                tracking=p['tracking'],
                                weight=p['chargeable_weight'],
                                price=p['price'],
                                status=status_label(lang, p['status'])))
            await update.message.reply_text('\n'.join(lines), reply_markup=partner_menu_keyboard(lang))
        return PARTNER_MENU

    elif text in (t('ru', 'btn_handoff'), t('en', 'btn_handoff')):
        pending = db.get_partner_parcels(partner_id, status='accepted')
        if not pending:
            await update.message.reply_text(t(lang, 'no_parcels_to_handoff'), reply_markup=partner_menu_keyboard(lang))
            return PARTNER_MENU
        context.user_data['handoff_count'] = len(pending)
        await update.message.reply_text(
            t(lang, 'handoff_confirm', count=len(pending)),
            reply_markup=yes_no_keyboard(lang)
        )
        return HANDOFF_CONFIRM

    elif text in (t('ru', 'btn_stats'), t('en', 'btn_stats')):
        stats = db.get_partner_stats(partner_id)
        await update.message.reply_text(
            t(lang, 'partner_stats', **stats),
            reply_markup=partner_menu_keyboard(lang)
        )
        return PARTNER_MENU

    elif text in (t('ru', 'main_menu'), t('en', 'main_menu')):
        return await start(update, context)

    else:
        await update.message.reply_text(
            t(lang, 'partner_menu', name=partner['name'], location=partner['location']),
            reply_markup=partner_menu_keyboard(lang)
        )
        return PARTNER_MENU


# ──────────────────── ACCEPT PARCEL FLOW ────────────────────

async def accept_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)

    if update.message.text and update.message.text in (t('ru', 'back'), t('en', 'back')):
        partner_id = context.user_data.get('partner_id')
        partner = db.get_partner_by_id(partner_id) if partner_id else None
        await update.message.reply_text(
            t(lang, 'partner_menu',
              name=partner['name'] if partner else '—',
              location=partner['location'] if partner else '—'),
            reply_markup=partner_menu_keyboard(lang)
        )
        return PARTNER_MENU

    if update.message.photo:
        file_id = update.message.photo[-1].file_id
        context.user_data['accept_photo'] = file_id
    else:
        context.user_data['accept_photo'] = None

    await update.message.reply_text(t(lang, 'accept_enter_weight'), reply_markup=back_keyboard(lang))
    return ACCEPT_WEIGHT


async def accept_weight(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    if update.message.text in (t('ru', 'back'), t('en', 'back')):
        await update.message.reply_text(t(lang, 'accept_send_photo'), reply_markup=back_keyboard(lang))
        return ACCEPT_PHOTO
    try:
        w = float(update.message.text.replace(',', '.'))
        context.user_data['accept_weight'] = w
        await update.message.reply_text(t(lang, 'accept_enter_length'))
        return ACCEPT_LENGTH
    except ValueError:
        await update.message.reply_text(t(lang, 'invalid_number'))
        return ACCEPT_WEIGHT


async def accept_length(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    try:
        context.user_data['accept_l'] = float(update.message.text.replace(',', '.'))
        await update.message.reply_text(t(lang, 'accept_enter_width'))
        return ACCEPT_WIDTH
    except ValueError:
        await update.message.reply_text(t(lang, 'invalid_number'))
        return ACCEPT_LENGTH


async def accept_width(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    try:
        context.user_data['accept_w'] = float(update.message.text.replace(',', '.'))
        await update.message.reply_text(t(lang, 'accept_enter_height'))
        return ACCEPT_HEIGHT
    except ValueError:
        await update.message.reply_text(t(lang, 'invalid_number'))
        return ACCEPT_WIDTH


async def accept_height(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    try:
        h = float(update.message.text.replace(',', '.'))
        context.user_data['accept_h'] = h
        await update.message.reply_text(t(lang, 'accept_enter_client_phone'))
        return ACCEPT_CLIENT_PHONE
    except ValueError:
        await update.message.reply_text(t(lang, 'invalid_number'))
        return ACCEPT_HEIGHT


async def accept_client_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    phone = update.message.text.strip()
    context.user_data['accept_client_phone'] = phone

    w = context.user_data['accept_weight']
    l = context.user_data['accept_l']
    ww = context.user_data['accept_w']
    h = context.user_data['accept_h']
    vol, chargeable, price = db.calculate_price(w, l, ww, h)
    context.user_data['accept_vol'] = vol
    context.user_data['accept_chargeable'] = chargeable
    context.user_data['accept_price'] = price

    await update.message.reply_text(
        t(lang, 'accept_confirm',
          phone=phone, weight=w, l=l, w=ww, h=h,
          vol=vol, chargeable=chargeable, price=price),
        reply_markup=confirm_keyboard(lang)
    )
    return ACCEPT_CONFIRM


async def accept_confirm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text

    if text not in (t('ru', 'btn_confirm'), t('en', 'btn_confirm')):
        partner_id = context.user_data.get('partner_id')
        partner = db.get_partner_by_id(partner_id) if partner_id else None
        await update.message.reply_text(
            t(lang, 'partner_menu',
              name=partner['name'] if partner else '—',
              location=partner['location'] if partner else '—'),
            reply_markup=partner_menu_keyboard(lang)
        )
        return PARTNER_MENU

    partner_id = context.user_data['partner_id']
    partner = db.get_partner_by_id(partner_id)
    phone = context.user_data['accept_client_phone']
    client = db.get_client_by_phone(phone)
    client_tg_id = client['telegram_id'] if client else None

    parcel = db.create_parcel(
        client_phone=phone,
        client_telegram_id=client_tg_id,
        partner_id=partner_id,
        weight=context.user_data['accept_weight'],
        length=context.user_data['accept_l'],
        width=context.user_data['accept_w'],
        height=context.user_data['accept_h'],
        photo_file_id=context.user_data.get('accept_photo'),
    )

    await update.message.reply_text(
        t(lang, 'parcel_accepted', tracking=parcel['tracking']),
        reply_markup=partner_menu_keyboard(lang)
    )

    # Notify client
    if client_tg_id:
        client_lang = client['lang'] if client else lang
        try:
            await context.bot.send_message(
                chat_id=client_tg_id,
                text=t(client_lang, 'notify_accepted',
                       tracking=parcel['tracking'],
                       partner=partner['name'] if partner else '—',
                       weight=parcel['chargeable_weight'],
                       price=parcel['price'])
            )
            if parcel['photo_file_id']:
                await context.bot.send_photo(
                    chat_id=client_tg_id,
                    photo=parcel['photo_file_id'],
                    caption=t(client_lang, 'parcel_photo')
                )
        except Exception as e:
            logger.warning(f"Could not notify client {client_tg_id}: {e}")

    return PARTNER_MENU


# ──────────────────── HANDOFF ────────────────────

async def handoff_confirm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text
    partner_id = context.user_data.get('partner_id')
    partner = db.get_partner_by_id(partner_id) if partner_id else None

    if text not in (t('ru', 'btn_confirm'), t('en', 'btn_confirm')):
        await update.message.reply_text(
            t(lang, 'partner_menu',
              name=partner['name'] if partner else '—',
              location=partner['location'] if partner else '—'),
            reply_markup=partner_menu_keyboard(lang)
        )
        return PARTNER_MENU

    handed = db.handoff_parcels(partner_id)
    await update.message.reply_text(
        t(lang, 'handoff_done', count=len(handed)),
        reply_markup=partner_menu_keyboard(lang)
    )

    # Notify clients
    for p in handed:
        if p['client_telegram_id']:
            # find client lang
            client = db.get_client(p['client_telegram_id'])
            client_lang = client['lang'] if client else 'ru'
            try:
                await context.bot.send_message(
                    chat_id=p['client_telegram_id'],
                    text=t(client_lang, 'handoff_notify', tracking=p['tracking'])
                )
            except Exception as e:
                logger.warning(f"Could not notify client {p['client_telegram_id']}: {e}")

    return PARTNER_MENU


# ──────────────────── ADMIN ────────────────────

async def admin_code_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    code = update.message.text.strip()
    if code != db.ADMIN_CODE:
        await update.message.reply_text(t(lang, 'admin_invalid_code'))
        return ADMIN_CODE_STATE
    context.user_data['is_admin'] = True
    await update.message.reply_text(
        t(lang, 'admin_welcome'),
        reply_markup=admin_menu_keyboard(lang)
    )
    return ADMIN_MENU


async def admin_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text

    if not context.user_data.get('is_admin'):
        return await start(update, context)

    if text in (t('ru', 'btn_network_stats'), t('en', 'btn_network_stats')):
        stats = db.get_network_stats()
        await update.message.reply_text(
            t(lang, 'network_stats', **stats),
            reply_markup=admin_menu_keyboard(lang)
        )
        return ADMIN_MENU

    elif text in (t('ru', 'btn_list_partners'), t('en', 'btn_list_partners')):
        partners = db.get_all_partners()
        if not partners:
            await update.message.reply_text(t(lang, 'no_partners'), reply_markup=admin_menu_keyboard(lang))
        else:
            lines = [t(lang, 'partners_list')]
            for p in partners:
                cnt = db.get_partner_parcel_count(p['id'])
                lines.append(t(lang, 'partner_line',
                                name=p['name'], location=p['location'],
                                code=p['code'], count=cnt))
            await update.message.reply_text('\n'.join(lines), reply_markup=admin_menu_keyboard(lang))
        return ADMIN_MENU

    elif text in (t('ru', 'btn_add_partner'), t('en', 'btn_add_partner')):
        await update.message.reply_text(t(lang, 'add_partner_name'), reply_markup=back_keyboard(lang))
        return ADD_PARTNER_NAME

    elif text in (t('ru', 'main_menu'), t('en', 'main_menu')):
        return await start(update, context)

    else:
        await update.message.reply_text(t(lang, 'admin_menu'), reply_markup=admin_menu_keyboard(lang))
        return ADMIN_MENU


async def add_partner_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    if update.message.text in (t('ru', 'back'), t('en', 'back')):
        await update.message.reply_text(t(lang, 'admin_menu'), reply_markup=admin_menu_keyboard(lang))
        return ADMIN_MENU
    context.user_data['new_partner_name'] = update.message.text.strip()
    await update.message.reply_text(t(lang, 'add_partner_location'))
    return ADD_PARTNER_LOCATION


async def add_partner_location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    context.user_data['new_partner_location'] = update.message.text.strip()
    await update.message.reply_text(t(lang, 'add_partner_code'))
    return ADD_PARTNER_CODE


async def add_partner_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    code = update.message.text.strip()
    name = context.user_data['new_partner_name']
    location = context.user_data['new_partner_location']
    success = db.add_partner(code, name, location)
    if not success:
        await update.message.reply_text(t(lang, 'partner_code_exists'))
        return ADD_PARTNER_CODE
    await update.message.reply_text(
        t(lang, 'partner_added', name=name, location=location, code=code.upper()),
        reply_markup=admin_menu_keyboard(lang)
    )
    return ADMIN_MENU


# ──────────────────── FALLBACK ────────────────────

async def fallback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await start(update, context)


# ──────────────────── FLASK KEEP-ALIVE ────────────────────

def run_flask():
    app = Flask(__name__)

    @app.route('/')
    def health():
        return 'OK', 200

    app.run(host='0.0.0.0', port=8080, debug=False, use_reloader=False)


# ──────────────────── MAIN ────────────────────

def main():
    db.init_db()
    logger.info("Database initialized.")

    # Start Flask in background thread
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    logger.info("Flask keep-alive server started on port 8080.")

    app = Application.builder().token(BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            LANG_SELECT: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, lang_select)
            ],
            ROLE_SELECT: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, role_select)
            ],
            CLIENT_NAME: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, client_name)
            ],
            CLIENT_PHONE: [
                MessageHandler(filters.CONTACT, client_phone),
                MessageHandler(filters.TEXT & ~filters.COMMAND, client_phone),
            ],
            CLIENT_MENU: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, client_menu_handler)
            ],
            CLIENT_TRACK: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, client_track)
            ],
            CLIENT_CALC_W: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, calc_weight)
            ],
            CLIENT_CALC_L: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, calc_length)
            ],
            CLIENT_CALC_W2: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, calc_width)
            ],
            CLIENT_CALC_H: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, calc_height)
            ],
            PARTNER_CODE: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, partner_code)
            ],
            PARTNER_MENU: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, partner_menu_handler)
            ],
            ACCEPT_PHOTO: [
                MessageHandler(filters.PHOTO, accept_photo),
                MessageHandler(filters.TEXT & ~filters.COMMAND, accept_photo),
            ],
            ACCEPT_WEIGHT: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, accept_weight)
            ],
            ACCEPT_LENGTH: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, accept_length)
            ],
            ACCEPT_WIDTH: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, accept_width)
            ],
            ACCEPT_HEIGHT: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, accept_height)
            ],
            ACCEPT_CLIENT_PHONE: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, accept_client_phone)
            ],
            ACCEPT_CONFIRM: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, accept_confirm)
            ],
            HANDOFF_CONFIRM: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, handoff_confirm)
            ],
            ADMIN_CODE_STATE: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, admin_code_handler)
            ],
            ADMIN_MENU: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, admin_menu_handler)
            ],
            ADD_PARTNER_NAME: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, add_partner_name)
            ],
            ADD_PARTNER_LOCATION: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, add_partner_location)
            ],
            ADD_PARTNER_CODE: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, add_partner_code)
            ],
        },
        fallbacks=[
            CommandHandler('start', start),
            MessageHandler(filters.ALL, fallback),
        ],
        allow_reentry=True,
    )

    app.add_handler(conv_handler)

    logger.info("OWAY Cargo bot is starting...")
    app.run_polling(drop_pending_updates=True)


if __name__ == '__main__':
    main()
