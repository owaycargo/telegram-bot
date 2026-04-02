import logging
import threading
import os
from flask import Flask, jsonify, request as flask_request
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
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

BOT_TOKEN = os.environ.get('BOT_TOKEN', '7486227402:AAH0zRC_kgrdzgu1dr8yryHoId6GkDNCinM')

# ──────────────────── States ────────────────────
(
    LANG_SELECT, ROLE_SELECT,
    # Client reg
    CLIENT_NAME, CLIENT_PHONE,
    # Client type selection
    CLIENT_TYPE_SELECT,
    # Menus
    CLIENT_MENU, ORDER_MENU, SEND_MENU,
    # Tracking (shared)
    CLIENT_TRACK,
    # Calculator
    CLIENT_CALC_W, CLIENT_CALC_L, CLIENT_CALC_W2, CLIENT_CALC_H, CLIENT_CALC_COUNTRY,
    # US Address verification
    ADDRESS_VERIFY,
    # Shopping assistant
    SHOPPING_REQUEST,
    # Partner
    PARTNER_CODE, PARTNER_MENU,
    ACCEPT_PHOTO, ACCEPT_WEIGHT, ACCEPT_LENGTH, ACCEPT_WIDTH, ACCEPT_HEIGHT,
    ACCEPT_CLIENT_PHONE, ACCEPT_CONFIRM, ACCEPT_COUNTRY,
    HANDOFF_CONFIRM,
    # Admin
    ADMIN_CODE_STATE, ADMIN_MENU,
    ADD_PARTNER_NAME, ADD_PARTNER_LOCATION, ADD_PARTNER_CODE,
    ADMIN_UPDATE_TRACKING, ADMIN_UPDATE_STATUS,
    ADMIN_BROADCAST, ADMIN_SET_ADDRESS,
    ADMIN_ADD_WU_ID, ADMIN_ADD_WU_NAME,
    # Driver
    DRIVER_CODE_STATE, DRIVER_MENU, DRIVER_DELIVER,
) = range(41)

# ──────────────────── Keyboards ────────────────────

def lang_keyboard():
    return ReplyKeyboardMarkup([['🇷🇺 Русский', '🇬🇧 English']], resize_keyboard=True, one_time_keyboard=True)


def role_keyboard(lang):
    # Only show Client — staff use /admin /partner /driver commands
    return ReplyKeyboardMarkup([
        [t(lang, 'btn_client')],
    ], resize_keyboard=True, one_time_keyboard=True)


def client_type_keyboard(lang):
    return ReplyKeyboardMarkup([
        [t(lang, 'btn_order_type')],
        [t(lang, 'btn_send_type')],
    ], resize_keyboard=True, one_time_keyboard=True)


def order_menu_keyboard(lang):
    return ReplyKeyboardMarkup([
        [t(lang, 'btn_track'), t(lang, 'btn_history')],
        [t(lang, 'btn_my_address'), t(lang, 'btn_shopping')],
        [t(lang, 'btn_calculator'), t(lang, 'btn_faq')],
        [t(lang, 'btn_support'), t(lang, 'btn_miniapp')],
        [t(lang, 'btn_change_lang'), t(lang, 'main_menu')],
    ], resize_keyboard=True)


def send_menu_keyboard(lang):
    return ReplyKeyboardMarkup([
        [t(lang, 'btn_track'), t(lang, 'btn_history')],
        [t(lang, 'btn_calculator'), t(lang, 'btn_find_dropoff')],
        [t(lang, 'btn_faq'), t(lang, 'btn_support')],
        [t(lang, 'btn_miniapp')],
        [t(lang, 'btn_change_lang'), t(lang, 'main_menu')],
    ], resize_keyboard=True)


def client_menu_keyboard(lang):
    """Legacy menu — used when client_type is not set yet."""
    return ReplyKeyboardMarkup([
        [t(lang, 'btn_track'), t(lang, 'btn_history')],
        [t(lang, 'btn_calculator'), t(lang, 'btn_support')],
        [t(lang, 'btn_change_lang'), t(lang, 'main_menu')],
    ], resize_keyboard=True)


def driver_menu_keyboard(lang):
    return ReplyKeyboardMarkup([
        [t(lang, 'btn_my_deliveries')],
        [t(lang, 'btn_mark_delivered')],
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
        [t(lang, 'btn_update_status')],
        [t(lang, 'btn_broadcast')],
        [t(lang, 'btn_set_address'), t(lang, 'btn_add_website_user')],
        [t(lang, 'btn_view_requests')],
        [t(lang, 'main_menu')],
    ], resize_keyboard=True)


def status_choice_keyboard(lang, route_type='DIRECT'):
    keys = db.statuses_for_route(route_type)
    labels = [status_label(lang, s) for s in keys]
    rows = [[labels[i], labels[i+1]] if i+1 < len(labels) else [labels[i]]
            for i in range(0, len(labels), 2)]
    rows.append([t(lang, 'back')])
    return ReplyKeyboardMarkup(rows, resize_keyboard=True, one_time_keyboard=True)


def country_keyboard(lang):
    return ReplyKeyboardMarkup([
        [t(lang, 'country_KG'), t(lang, 'country_KZ')],
        [t(lang, 'country_UZ')],
        [t(lang, 'country_RU'), t(lang, 'country_BY')],
        [t(lang, 'back')],
    ], resize_keyboard=True, one_time_keyboard=True)


def confirm_keyboard(lang):
    return ReplyKeyboardMarkup([
        [t(lang, 'btn_confirm'), t(lang, 'cancel')],
    ], resize_keyboard=True, one_time_keyboard=True)


def back_keyboard(lang):
    return ReplyKeyboardMarkup([[t(lang, 'back')]], resize_keyboard=True)


def calc_result_keyboard(lang):
    return ReplyKeyboardMarkup([
        [t(lang, 'btn_recalculate')],
        [t(lang, 'btn_contact_manager')],
        [t(lang, 'back')],
    ], resize_keyboard=True)


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


STATUS_ICONS = {
    'accepted': '✅',
    'in_transit': '✈️',
    'arrived': '📍',
    'customs': '🛃',
    'ready': '📦',
    'transit_zone': '🔄',
    'arrived_moscow': '📍',
    'with_driver': '🚚',
    'delivered': '🏠',
}


def status_label(lang: str, status: str) -> str:
    return t(lang, f'status_{status}')


def build_timeline(lang: str, events: list) -> str:
    if not events:
        return ''
    lines = [t(lang, 'parcel_timeline')]
    for ev in events:
        icon = STATUS_ICONS.get(ev['status'], '•')
        label = status_label(lang, ev['status'])
        date = ev['created_at'][:16].replace('T', ' ')
        lines.append(f"{icon} {label} — {date}")
    return '\n'.join(lines)


def menu_keyboard_for_client(client, lang):
    """Return the right menu keyboard based on client_type."""
    ctype = client['client_type'] if client else None
    if ctype == 'ORDER':
        return order_menu_keyboard(lang)
    elif ctype == 'SEND':
        return send_menu_keyboard(lang)
    return client_menu_keyboard(lang)


def menu_state_for_client(client):
    """Return the right ConversationHandler state based on client_type."""
    ctype = client['client_type'] if client else None
    if ctype == 'ORDER':
        return ORDER_MENU
    elif ctype == 'SEND':
        return SEND_MENU
    return CLIENT_TYPE_SELECT


def menu_text_for_client(client, lang):
    ctype = client['client_type'] if client else None
    phone = client['phone'] if client else '—'
    if ctype == 'ORDER':
        return t(lang, 'order_menu', phone=phone)
    elif ctype == 'SEND':
        return t(lang, 'send_menu', phone=phone)
    return t(lang, 'client_type_select')


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
        client = db.get_client(update.effective_user.id)
        if client:
            context.user_data['lang'] = client['lang']
            lang = client['lang']
            if not client['client_type']:
                # Existing client without type → ask type
                await update.message.reply_text(
                    t(lang, 'client_already_registered', name=client['name']) + '\n\n' +
                    t(lang, 'client_type_select'),
                    reply_markup=client_type_keyboard(lang)
                )
                return CLIENT_TYPE_SELECT
            await update.message.reply_text(
                t(lang, 'client_already_registered', name=client['name']),
                reply_markup=menu_keyboard_for_client(client, lang)
            )
            return menu_state_for_client(client)
        await update.message.reply_text(t(lang, 'client_enter_name'), reply_markup=ReplyKeyboardRemove())
        return CLIENT_NAME

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

    if not update.message.contact:
        keyboard = ReplyKeyboardMarkup(
            [[KeyboardButton(t(lang, 'btn_share_phone'), request_contact=True)]],
            resize_keyboard=True,
            one_time_keyboard=True,
        )
        await update.message.reply_text(t(lang, 'phone_not_yours'), reply_markup=keyboard)
        return CLIENT_PHONE

    contact = update.message.contact
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
        reply_markup=ReplyKeyboardRemove()
    )
    # Ask client type
    await update.message.reply_text(
        t(lang, 'client_type_select'),
        reply_markup=client_type_keyboard(lang)
    )
    return CLIENT_TYPE_SELECT


# ──────────────────── CLIENT TYPE SELECTION ────────────────────

async def client_type_select(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text

    if text in (t('ru', 'btn_order_type'), t('en', 'btn_order_type')):
        db.set_client_type(update.effective_user.id, 'ORDER')
        client = db.get_client(update.effective_user.id)
        phone = client['phone'] if client else '—'
        await update.message.reply_text(
            t(lang, 'order_menu', phone=phone),
            reply_markup=order_menu_keyboard(lang)
        )
        return ORDER_MENU

    elif text in (t('ru', 'btn_send_type'), t('en', 'btn_send_type')):
        db.set_client_type(update.effective_user.id, 'SEND')
        client = db.get_client(update.effective_user.id)
        phone = client['phone'] if client else '—'
        await update.message.reply_text(
            t(lang, 'send_menu', phone=phone),
            reply_markup=send_menu_keyboard(lang)
        )
        return SEND_MENU

    else:
        await update.message.reply_text(
            t(lang, 'client_type_select'),
            reply_markup=client_type_keyboard(lang)
        )
        return CLIENT_TYPE_SELECT


# ──────────────────── ORDER MENU (CIS clients — ordering from USA) ────────────────────

async def order_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text
    client = db.get_client(update.effective_user.id)

    if text in (t('ru', 'btn_track'), t('en', 'btn_track')):
        await update.message.reply_text(t(lang, 'enter_tracking'), reply_markup=back_keyboard(lang))
        context.user_data['track_return'] = 'ORDER'
        return CLIENT_TRACK

    elif text in (t('ru', 'btn_history'), t('en', 'btn_history')):
        await _show_history(update, context, lang, order_menu_keyboard(lang))
        return ORDER_MENU

    elif text in (t('ru', 'btn_my_address'), t('en', 'btn_my_address')):
        # Check if website_id already set
        if client and client['website_id']:
            address = db.get_config('us_warehouse_address', db.DEFAULT_US_ADDRESS)
            await update.message.reply_text(
                t(lang, 'address_already_set', address=address),
                reply_markup=order_menu_keyboard(lang)
            )
            return ORDER_MENU
        await update.message.reply_text(
            t(lang, 'address_enter_id'),
            reply_markup=back_keyboard(lang)
        )
        return ADDRESS_VERIFY

    elif text in (t('ru', 'btn_shopping'), t('en', 'btn_shopping')):
        await update.message.reply_text(
            t(lang, 'shopping_intro'),
            reply_markup=back_keyboard(lang)
        )
        await update.message.reply_text(t(lang, 'shopping_enter_request'))
        return SHOPPING_REQUEST

    elif text in (t('ru', 'btn_calculator'), t('en', 'btn_calculator')):
        await update.message.reply_text(t(lang, 'calc_enter_weight'), reply_markup=back_keyboard(lang))
        context.user_data['calc_return'] = 'ORDER'
        return CLIENT_CALC_W

    elif text in (t('ru', 'btn_faq'), t('en', 'btn_faq')):
        await update.message.reply_text(
            t(lang, 'faq_order'),
            reply_markup=order_menu_keyboard(lang)
        )
        return ORDER_MENU

    elif text in (t('ru', 'btn_support'), t('en', 'btn_support')):
        await update.message.reply_text(
            t(lang, 'support_message'),
            reply_markup=order_menu_keyboard(lang)
        )
        return ORDER_MENU

    elif text in (t('ru', 'btn_miniapp'), t('en', 'btn_miniapp')):
        miniapp_url = db.get_config('miniapp_url', db.DEFAULT_MINIAPP_URL)
        await update.message.reply_text(
            f"🌐 OWAY Cargo Mini App:\n{miniapp_url}",
            reply_markup=order_menu_keyboard(lang)
        )
        return ORDER_MENU

    elif text in (t('ru', 'btn_change_lang'), t('en', 'btn_change_lang')):
        await update.message.reply_text(t(lang, 'choose_language'), reply_markup=lang_keyboard())
        return LANG_SELECT

    elif text in (t('ru', 'main_menu'), t('en', 'main_menu')):
        return await start(update, context)

    else:
        phone = client['phone'] if client else '—'
        await update.message.reply_text(
            t(lang, 'order_menu', phone=phone),
            reply_markup=order_menu_keyboard(lang)
        )
        return ORDER_MENU


# ──────────────────── SEND MENU (USA clients — sending to CIS) ────────────────────

async def send_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text
    client = db.get_client(update.effective_user.id)

    if text in (t('ru', 'btn_track'), t('en', 'btn_track')):
        await update.message.reply_text(t(lang, 'enter_tracking'), reply_markup=back_keyboard(lang))
        context.user_data['track_return'] = 'SEND'
        return CLIENT_TRACK

    elif text in (t('ru', 'btn_history'), t('en', 'btn_history')):
        await _show_history(update, context, lang, send_menu_keyboard(lang))
        return SEND_MENU

    elif text in (t('ru', 'btn_calculator'), t('en', 'btn_calculator')):
        await update.message.reply_text(t(lang, 'calc_enter_weight'), reply_markup=back_keyboard(lang))
        context.user_data['calc_return'] = 'SEND'
        return CLIENT_CALC_W

    elif text in (t('ru', 'btn_find_dropoff'), t('en', 'btn_find_dropoff')):
        # Show all partners (US drop-off points)
        partners = db.get_all_partners()
        if not partners:
            await update.message.reply_text(t(lang, 'no_dropoffs'), reply_markup=send_menu_keyboard(lang))
        else:
            lines = [t(lang, 'dropoffs_list')]
            for p in partners:
                lines.append(t(lang, 'dropoff_line', name=p['name'], location=p['location']))
            await update.message.reply_text('\n'.join(lines), reply_markup=send_menu_keyboard(lang))
        return SEND_MENU

    elif text in (t('ru', 'btn_faq'), t('en', 'btn_faq')):
        await update.message.reply_text(
            t(lang, 'faq_send'),
            reply_markup=send_menu_keyboard(lang)
        )
        return SEND_MENU

    elif text in (t('ru', 'btn_support'), t('en', 'btn_support')):
        await update.message.reply_text(
            t(lang, 'support_message'),
            reply_markup=send_menu_keyboard(lang)
        )
        return SEND_MENU

    elif text in (t('ru', 'btn_miniapp'), t('en', 'btn_miniapp')):
        miniapp_url = db.get_config('miniapp_url', db.DEFAULT_MINIAPP_URL)
        await update.message.reply_text(
            f"🌐 OWAY Cargo Mini App:\n{miniapp_url}",
            reply_markup=send_menu_keyboard(lang)
        )
        return SEND_MENU

    elif text in (t('ru', 'btn_change_lang'), t('en', 'btn_change_lang')):
        await update.message.reply_text(t(lang, 'choose_language'), reply_markup=lang_keyboard())
        return LANG_SELECT

    elif text in (t('ru', 'main_menu'), t('en', 'main_menu')):
        return await start(update, context)

    else:
        phone = client['phone'] if client else '—'
        await update.message.reply_text(
            t(lang, 'send_menu', phone=phone),
            reply_markup=send_menu_keyboard(lang)
        )
        return SEND_MENU


# ──────────────────── SHARED HISTORY HELPER ────────────────────

async def _show_history(update, context, lang, reply_markup):
    parcels = db.get_client_parcels(update.effective_user.id)
    if not parcels:
        await update.message.reply_text(t(lang, 'no_parcels'), reply_markup=reply_markup)
    else:
        lines = [t(lang, 'parcel_history')]
        for p in parcels:
            partner = db.get_partner_by_id(p['partner_id'])
            pname = partner['name'] if partner else '—'
            lines.append(
                f"• {p['tracking']} | {status_label(lang, p['status'])} | {pname} | ${p['price']}"
            )
        await update.message.reply_text('\n'.join(lines), reply_markup=reply_markup)


# ──────────────────── LEGACY CLIENT MENU (fallback) ────────────────────

async def client_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Kept for backwards compat — redirects to type select."""
    lang = get_lang(context, update.effective_user.id)
    client = db.get_client(update.effective_user.id)

    if client and client['client_type']:
        # Route to proper menu
        if client['client_type'] == 'ORDER':
            await update.message.reply_text(
                t(lang, 'order_menu', phone=client['phone']),
                reply_markup=order_menu_keyboard(lang)
            )
            return ORDER_MENU
        else:
            await update.message.reply_text(
                t(lang, 'send_menu', phone=client['phone']),
                reply_markup=send_menu_keyboard(lang)
            )
            return SEND_MENU

    await update.message.reply_text(
        t(lang, 'client_type_select'),
        reply_markup=client_type_keyboard(lang)
    )
    return CLIENT_TYPE_SELECT


# ──────────────────── TRACKING (shared between menus) ────────────────────

async def client_track(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text.strip()
    client = db.get_client(update.effective_user.id)
    track_return = context.user_data.get('track_return', 'ORDER')
    reply_markup = order_menu_keyboard(lang) if track_return == 'ORDER' else send_menu_keyboard(lang)
    return_state = ORDER_MENU if track_return == 'ORDER' else SEND_MENU

    if text in (t('ru', 'back'), t('en', 'back')):
        phone = client['phone'] if client else '—'
        if track_return == 'ORDER':
            await update.message.reply_text(t(lang, 'order_menu', phone=phone), reply_markup=reply_markup)
        else:
            await update.message.reply_text(t(lang, 'send_menu', phone=phone), reply_markup=reply_markup)
        return return_state

    parcel = db.get_parcel_by_tracking(text)
    if not parcel:
        await update.message.reply_text(
            t(lang, 'parcel_not_found', tracking=text),
            reply_markup=reply_markup
        )
        return return_state

    partner = db.get_partner_by_id(parcel['partner_id'])
    dims = f"{parcel['length']}×{parcel['width']}×{parcel['height']} cm"
    country_code = parcel['destination_country'] or 'KG'
    country_name = t(lang, f'country_{country_code}')
    info = t(lang, 'parcel_info',
             tracking=parcel['tracking'],
             country=country_name,
             status=status_label(lang, parcel['status']),
             partner=partner['name'] if partner else '—',
             weight=parcel['chargeable_weight'],
             dims=dims,
             price=parcel['price'],
             date=parcel['created_at'][:10])

    events = db.get_parcel_timeline(parcel['id'])
    timeline = build_timeline(lang, events)
    full_message = info + '\n\n' + timeline if timeline else info

    await update.message.reply_text(full_message, reply_markup=reply_markup)

    if parcel['photo_file_id']:
        await update.message.reply_photo(
            photo=parcel['photo_file_id'],
            caption=t(lang, 'parcel_photo')
        )
    return return_state


# ──────────────────── CALCULATOR HELPERS ────────────────────

_HELP_TRIGGERS = {
    'how', 'how?', 'example', 'what', 'format',
    'как', 'как?', 'не понял', 'пример', 'формат', 'что',
}

def _is_help_query(text: str) -> bool:
    return text.strip().lower() in _HELP_TRIGGERS


def _parse_weight(text: str):
    """Return (kg_value, display_string) or None on failure."""
    import re
    text = text.strip()
    m = re.match(
        r'^([\d]+[.,]?[\d]*)\s*'
        r'(kg|кг|lb|lbs|pound|pounds|фунт|фунтов|фунта)?$',
        text, re.IGNORECASE
    )
    if not m:
        return None
    value = float(m.group(1).replace(',', '.'))
    unit = (m.group(2) or '').lower()
    if unit in ('lb', 'lbs', 'pound', 'pounds', 'фунт', 'фунтов', 'фунта'):
        kg = round(value * 0.453592, 3)
        display = f'{value} lb = {kg} кг'
    else:
        kg = round(value, 3)
        display = f'{value} кг'
    return kg, display


def _parse_dims(text: str):
    """Return (l, w, h) in cm or None on failure."""
    import re
    text = text.strip()
    # Detect unit suffix
    unit_match = re.search(r'\b(cm|см|in|inch|inches)\b', text, re.IGNORECASE)
    unit = unit_match.group(1).lower() if unit_match else 'cm'
    # Remove unit text
    text_clean = re.sub(r'\b(cm|см|in|inch|inches)\b', '', text, flags=re.IGNORECASE)
    # Split on separators: x, х (cyrillic), *, space
    parts = re.split(r'[xх*\s]+', text_clean.strip(), flags=re.IGNORECASE)
    parts = [p.replace(',', '.') for p in parts if p.strip()]
    if len(parts) != 3:
        return None
    try:
        nums = [float(p) for p in parts]
    except ValueError:
        return None
    if unit in ('in', 'inch', 'inches'):
        nums = [round(n * 2.54, 2) for n in nums]
    return tuple(nums)  # (l, w, h) in cm


# ──────────────────── CALCULATOR ────────────────────

async def calc_weight(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text.strip()

    if text in (t('ru', 'back'), t('en', 'back')):
        client = db.get_client(update.effective_user.id)
        calc_return = context.user_data.get('calc_return', 'SEND')
        phone = client['phone'] if client else '—'
        if calc_return == 'ORDER':
            await update.message.reply_text(t(lang, 'order_menu', phone=phone), reply_markup=order_menu_keyboard(lang))
            return ORDER_MENU
        await update.message.reply_text(t(lang, 'send_menu', phone=phone), reply_markup=send_menu_keyboard(lang))
        return SEND_MENU

    if _is_help_query(text):
        await update.message.reply_text(t(lang, 'calc_weight_help'))
        return CLIENT_CALC_W

    result = _parse_weight(text)
    if result is None:
        await update.message.reply_text(t(lang, 'calc_weight_error'))
        return CLIENT_CALC_W

    kg, display = result
    context.user_data['calc_weight'] = kg
    await update.message.reply_text(
        t(lang, 'calc_weight_accepted', input=display, kg=kg),
        reply_markup=back_keyboard(lang)
    )
    await update.message.reply_text(t(lang, 'calc_enter_dims'), reply_markup=back_keyboard(lang))
    return CLIENT_CALC_L


async def calc_dims(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Single handler for dimension input (replaces separate L/W/H steps)."""
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text.strip()

    if text in (t('ru', 'back'), t('en', 'back')):
        await update.message.reply_text(t(lang, 'calc_enter_weight'), reply_markup=back_keyboard(lang))
        return CLIENT_CALC_W

    if _is_help_query(text):
        await update.message.reply_text(t(lang, 'calc_dims_help'))
        return CLIENT_CALC_L

    result = _parse_dims(text)
    if result is None:
        await update.message.reply_text(t(lang, 'calc_dims_error'))
        return CLIENT_CALC_L

    l, w, h = result
    context.user_data['calc_l'] = l
    context.user_data['calc_w'] = w
    context.user_data['calc_h'] = h

    # Show accepted confirmation
    raw_input = text
    await update.message.reply_text(
        t(lang, 'calc_dims_accepted', input=raw_input, l=l, w=w, h=h)
    )
    await update.message.reply_text(
        t(lang, 'calc_choose_country'),
        reply_markup=country_keyboard(lang)
    )
    return CLIENT_CALC_COUNTRY


async def calc_country(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text.strip()
    calc_return = context.user_data.get('calc_return', 'SEND')

    # Back → return to dims step
    if text in (t('ru', 'back'), t('en', 'back')):
        await update.message.reply_text(t(lang, 'calc_enter_dims'), reply_markup=back_keyboard(lang))
        return CLIENT_CALC_L

    # "Recalculate" → restart from weight
    if text in (t('ru', 'btn_recalculate'), t('en', 'btn_recalculate')):
        await update.message.reply_text(t(lang, 'calc_enter_weight'), reply_markup=back_keyboard(lang))
        return CLIENT_CALC_W

    # "Contact manager" → show support contacts and return to menu
    if text in (t('ru', 'btn_contact_manager'), t('en', 'btn_contact_manager')):
        client = db.get_client(update.effective_user.id)
        phone = client['phone'] if client else '—'
        await update.message.reply_text(t(lang, 'support_text'))
        if calc_return == 'ORDER':
            await update.message.reply_text(t(lang, 'order_menu', phone=phone), reply_markup=order_menu_keyboard(lang))
            return ORDER_MENU
        elif calc_return == 'SEND':
            await update.message.reply_text(t(lang, 'send_menu', phone=phone), reply_markup=send_menu_keyboard(lang))
            return SEND_MENU
        await update.message.reply_text(t(lang, 'client_menu', phone=phone), reply_markup=client_menu_keyboard(lang))
        return CLIENT_MENU

    country_map = {}
    for code in db.DIRECT_COUNTRIES + db.TRANSIT_COUNTRIES:
        country_map[t('ru', f'country_{code}')] = code
        country_map[t('en', f'country_{code}')] = code

    chosen = country_map.get(text)
    if not chosen:
        await update.message.reply_text(t(lang, 'invalid_input'), reply_markup=country_keyboard(lang))
        return CLIENT_CALC_COUNTRY

    w_actual = context.user_data['calc_weight']
    l = context.user_data['calc_l']
    w = context.user_data['calc_w']
    h = context.user_data['calc_h']
    vol, chargeable, price = db.calculate_price(w_actual, l, w, h, chosen)
    rate = db.RATES.get(chosen, 12.0)
    country_name = t(lang, f'country_{chosen}')

    await update.message.reply_text(
        t(lang, 'calc_result',
          country=country_name, rate=rate,
          actual=w_actual, vol=vol, chargeable=chargeable, price=price),
        reply_markup=calc_result_keyboard(lang)
    )
    # Stay in CALC_COUNTRY so user can tap Recalculate or Contact manager
    return CLIENT_CALC_COUNTRY


# ──────────────────── US ADDRESS VERIFICATION ────────────────────

async def address_verify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text.strip()

    if text in (t('ru', 'back'), t('en', 'back')):
        client = db.get_client(update.effective_user.id)
        phone = client['phone'] if client else '—'
        await update.message.reply_text(
            t(lang, 'order_menu', phone=phone),
            reply_markup=order_menu_keyboard(lang)
        )
        return ORDER_MENU

    website_id = text.strip()
    wu = db.get_website_user(website_id)
    if not wu:
        await update.message.reply_text(
            t(lang, 'address_not_found', website_id=website_id),
            reply_markup=back_keyboard(lang)
        )
        return ADDRESS_VERIFY

    # Link website user to this telegram account
    db.set_client_website_id(update.effective_user.id, website_id)
    db.link_website_user_telegram(website_id, update.effective_user.id)

    address = db.get_config('us_warehouse_address', db.DEFAULT_US_ADDRESS)
    client = db.get_client(update.effective_user.id)
    phone = client['phone'] if client else '—'
    await update.message.reply_text(
        t(lang, 'your_us_address', address=address),
        reply_markup=order_menu_keyboard(lang)
    )
    return ORDER_MENU


# ──────────────────── SHOPPING ASSISTANT ────────────────────

async def shopping_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text.strip()

    if text in (t('ru', 'back'), t('en', 'back')):
        client = db.get_client(update.effective_user.id)
        phone = client['phone'] if client else '—'
        await update.message.reply_text(
            t(lang, 'order_menu', phone=phone),
            reply_markup=order_menu_keyboard(lang)
        )
        return ORDER_MENU

    client = db.get_client(update.effective_user.id)
    if not client:
        return await start(update, context)

    db.create_shopping_request(
        client_telegram_id=update.effective_user.id,
        client_name=client['name'],
        client_phone=client['phone'],
        request_text=text
    )

    await update.message.reply_text(
        t(lang, 'shopping_received', phone=client['phone']),
        reply_markup=order_menu_keyboard(lang)
    )

    # Notify all admins
    admin_ids = db.get_admin_telegram_ids()
    notify_text = t('ru', 'notify_shopping_new',
                    name=client['name'],
                    phone=client['phone'],
                    request=text)
    for admin_id in admin_ids:
        try:
            await context.bot.send_message(chat_id=admin_id, text=notify_text)
        except Exception as e:
            logger.warning(f"Could not notify admin {admin_id}: {e}")

    return ORDER_MENU


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
    await update.message.reply_text(
        t(lang, 'accept_choose_country'),
        reply_markup=country_keyboard(lang)
    )
    return ACCEPT_COUNTRY


async def accept_country(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text.strip()

    if text in (t('ru', 'back'), t('en', 'back')):
        await update.message.reply_text(t(lang, 'accept_enter_client_phone'), reply_markup=back_keyboard(lang))
        return ACCEPT_CLIENT_PHONE

    country_map = {}
    for code in db.DIRECT_COUNTRIES + db.TRANSIT_COUNTRIES:
        country_map[t('ru', f'country_{code}')] = code
        country_map[t('en', f'country_{code}')] = code

    chosen = country_map.get(text)
    if not chosen:
        await update.message.reply_text(t(lang, 'invalid_input'), reply_markup=country_keyboard(lang))
        return ACCEPT_COUNTRY

    context.user_data['accept_country'] = chosen

    w = context.user_data['accept_weight']
    l = context.user_data['accept_l']
    ww = context.user_data['accept_w']
    h = context.user_data['accept_h']
    phone = context.user_data['accept_client_phone']
    vol, chargeable, price = db.calculate_price(w, l, ww, h, chosen)
    context.user_data['accept_vol'] = vol
    context.user_data['accept_chargeable'] = chargeable
    context.user_data['accept_price'] = price

    country_name = t(lang, f'country_{chosen}')
    await update.message.reply_text(
        t(lang, 'accept_confirm',
          phone=phone, country=country_name, weight=w, l=l, w=ww, h=h,
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
        destination_country=context.user_data.get('accept_country', 'KG'),
    )

    await update.message.reply_text(
        t(lang, 'parcel_accepted', tracking=parcel['tracking']),
        reply_markup=partner_menu_keyboard(lang)
    )

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

    for p in handed:
        if p['client_telegram_id']:
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


# ──────────────────── DRIVER ────────────────────

async def driver_code_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    code = update.message.text.strip()
    driver = db.get_driver_by_code(code)
    if not driver:
        await update.message.reply_text(t(lang, 'driver_invalid_code'))
        return DRIVER_CODE_STATE
    db.link_driver_telegram(driver['id'], update.effective_user.id)
    context.user_data['driver_id'] = driver['id']
    await update.message.reply_text(
        t(lang, 'driver_welcome', name=driver['name']),
        reply_markup=driver_menu_keyboard(lang)
    )
    return DRIVER_MENU


async def driver_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text

    if text in (t('ru', 'btn_my_deliveries'), t('en', 'btn_my_deliveries')):
        parcels = db.get_parcels_for_driver()
        if not parcels:
            await update.message.reply_text(t(lang, 'no_deliveries'), reply_markup=driver_menu_keyboard(lang))
        else:
            lines = [t(lang, 'deliveries_list')]
            for p in parcels:
                country = t(lang, f"country_{p['destination_country'] or 'KG'}")
                lines.append(f"• {p['tracking']} | {country} | {p['client_phone']} | {p['chargeable_weight']}кг")
            await update.message.reply_text('\n'.join(lines), reply_markup=driver_menu_keyboard(lang))
        return DRIVER_MENU

    elif text in (t('ru', 'btn_mark_delivered'), t('en', 'btn_mark_delivered')):
        await update.message.reply_text(t(lang, 'driver_enter_tracking'), reply_markup=back_keyboard(lang))
        return DRIVER_DELIVER

    elif text in (t('ru', 'main_menu'), t('en', 'main_menu')):
        return await start(update, context)

    else:
        await update.message.reply_text(t(lang, 'driver_menu'), reply_markup=driver_menu_keyboard(lang))
        return DRIVER_MENU


async def driver_deliver(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text.strip()

    if text in (t('ru', 'back'), t('en', 'back')):
        await update.message.reply_text(t(lang, 'driver_menu'), reply_markup=driver_menu_keyboard(lang))
        return DRIVER_MENU

    parcel = db.get_parcel_by_tracking(text)
    if not parcel or parcel['status'] != 'with_driver':
        await update.message.reply_text(
            t(lang, 'driver_parcel_not_found', tracking=text),
            reply_markup=driver_menu_keyboard(lang)
        )
        return DRIVER_DELIVER

    updated = db.mark_parcel_delivered(text)
    await update.message.reply_text(
        t(lang, 'driver_delivered_ok', tracking=text),
        reply_markup=driver_menu_keyboard(lang)
    )

    if updated and updated['client_telegram_id']:
        client = db.get_client(updated['client_telegram_id'])
        client_lang = client['lang'] if client else 'ru'
        try:
            await context.bot.send_message(
                chat_id=updated['client_telegram_id'],
                text=t(client_lang, 'notify_delivered', tracking=text)
            )
        except Exception as e:
            logger.warning(f"Could not notify client: {e}")

    return DRIVER_MENU


# ──────────────────── ADMIN ────────────────────

async def admin_code_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    code = update.message.text.strip()
    if code != db.ADMIN_CODE:
        await update.message.reply_text(t(lang, 'admin_invalid_code'))
        return ADMIN_CODE_STATE
    context.user_data['is_admin'] = True
    db.add_admin_telegram_id(update.effective_user.id)
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

    elif text in (t('ru', 'btn_update_status'), t('en', 'btn_update_status')):
        await update.message.reply_text(t(lang, 'admin_enter_tracking'), reply_markup=back_keyboard(lang))
        return ADMIN_UPDATE_TRACKING

    elif text in (t('ru', 'btn_broadcast'), t('en', 'btn_broadcast')):
        await update.message.reply_text(t(lang, 'broadcast_enter_msg'), reply_markup=back_keyboard(lang))
        return ADMIN_BROADCAST

    elif text in (t('ru', 'btn_set_address'), t('en', 'btn_set_address')):
        current = db.get_config('us_warehouse_address', db.DEFAULT_US_ADDRESS)
        await update.message.reply_text(
            t(lang, 'set_address_enter', current=current),
            reply_markup=back_keyboard(lang)
        )
        return ADMIN_SET_ADDRESS

    elif text in (t('ru', 'btn_add_website_user'), t('en', 'btn_add_website_user')):
        await update.message.reply_text(t(lang, 'add_wu_id_enter'), reply_markup=back_keyboard(lang))
        return ADMIN_ADD_WU_ID

    elif text in (t('ru', 'btn_view_requests'), t('en', 'btn_view_requests')):
        requests = db.get_new_shopping_requests()
        if not requests:
            await update.message.reply_text(t(lang, 'view_requests_empty'), reply_markup=admin_menu_keyboard(lang))
        else:
            lines = [t(lang, 'view_requests_header')]
            for r in requests:
                lines.append(t(lang, 'request_line',
                                id=r['id'],
                                client=r['client_name'],
                                phone=r['client_phone'],
                                text=r['request_text'][:100],
                                date=r['created_at'][:16]))
            await update.message.reply_text('\n'.join(lines), reply_markup=admin_menu_keyboard(lang))
        return ADMIN_MENU

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


# ──────────────────── ADMIN STATUS UPDATE ────────────────────

async def admin_update_tracking(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text.strip()

    if text in (t('ru', 'back'), t('en', 'back')):
        await update.message.reply_text(t(lang, 'admin_menu'), reply_markup=admin_menu_keyboard(lang))
        return ADMIN_MENU

    parcel = db.get_parcel_by_tracking(text)
    if not parcel:
        await update.message.reply_text(
            t(lang, 'admin_parcel_not_found', tracking=text),
            reply_markup=back_keyboard(lang)
        )
        return ADMIN_UPDATE_TRACKING

    context.user_data['update_tracking'] = parcel['tracking']
    context.user_data['update_route_type'] = parcel['route_type'] or 'DIRECT'
    await update.message.reply_text(
        t(lang, 'admin_choose_status',
          tracking=parcel['tracking'],
          status=status_label(lang, parcel['status'])),
        reply_markup=status_choice_keyboard(lang, parcel['route_type'] or 'DIRECT')
    )
    return ADMIN_UPDATE_STATUS


async def admin_update_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text.strip()

    if text in (t('ru', 'back'), t('en', 'back')):
        await update.message.reply_text(t(lang, 'admin_menu'), reply_markup=admin_menu_keyboard(lang))
        return ADMIN_MENU

    route_type = context.user_data.get('update_route_type', 'DIRECT')
    chosen_status = None
    for s in db.statuses_for_route(route_type):
        if text == status_label(lang, s):
            chosen_status = s
            break

    if not chosen_status:
        await update.message.reply_text(t(lang, 'invalid_input'),
                                        reply_markup=status_choice_keyboard(lang, route_type))
        return ADMIN_UPDATE_STATUS

    tracking = context.user_data.get('update_tracking')
    parcel = db.update_parcel_status(tracking, chosen_status)

    await update.message.reply_text(
        t(lang, 'admin_status_updated',
          tracking=tracking,
          status=status_label(lang, chosen_status)),
        reply_markup=admin_menu_keyboard(lang)
    )

    if parcel and parcel['client_telegram_id']:
        client = db.get_client(parcel['client_telegram_id'])
        client_lang = client['lang'] if client else 'ru'
        try:
            await context.bot.send_message(
                chat_id=parcel['client_telegram_id'],
                text=t(client_lang, 'notify_status_changed',
                       tracking=tracking,
                       status=status_label(client_lang, chosen_status))
            )
        except Exception as e:
            logger.warning(f"Could not notify client: {e}")

    return ADMIN_MENU


# ──────────────────── ADMIN BROADCAST ────────────────────

async def admin_broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text.strip()

    if text in (t('ru', 'back'), t('en', 'back')):
        await update.message.reply_text(t(lang, 'admin_menu'), reply_markup=admin_menu_keyboard(lang))
        return ADMIN_MENU

    clients = db.get_all_clients()
    sent = 0
    failed = 0
    for c in clients:
        try:
            await context.bot.send_message(chat_id=c['telegram_id'], text=text)
            sent += 1
        except Exception:
            failed += 1

    await update.message.reply_text(
        t(lang, 'broadcast_sent', sent=sent, failed=failed),
        reply_markup=admin_menu_keyboard(lang)
    )
    return ADMIN_MENU


# ──────────────────── ADMIN SET US WAREHOUSE ADDRESS ────────────────────

async def admin_set_address(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text.strip()

    if text in (t('ru', 'back'), t('en', 'back')):
        await update.message.reply_text(t(lang, 'admin_menu'), reply_markup=admin_menu_keyboard(lang))
        return ADMIN_MENU

    db.set_config('us_warehouse_address', text)
    await update.message.reply_text(
        t(lang, 'address_updated'),
        reply_markup=admin_menu_keyboard(lang)
    )
    return ADMIN_MENU


# ──────────────────── ADMIN ADD WEBSITE USER ────────────────────

async def admin_add_wu_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text.strip()

    if text in (t('ru', 'back'), t('en', 'back')):
        await update.message.reply_text(t(lang, 'admin_menu'), reply_markup=admin_menu_keyboard(lang))
        return ADMIN_MENU

    context.user_data['new_wu_id'] = text
    await update.message.reply_text(
        t(lang, 'add_wu_name_enter', website_id=text),
        reply_markup=back_keyboard(lang)
    )
    return ADMIN_ADD_WU_NAME


async def admin_add_wu_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text.strip()

    if text in (t('ru', 'back'), t('en', 'back')):
        await update.message.reply_text(t(lang, 'add_wu_id_enter'), reply_markup=back_keyboard(lang))
        return ADMIN_ADD_WU_ID

    website_id = context.user_data.get('new_wu_id', '')
    success = db.add_website_user(website_id, text)
    if not success:
        await update.message.reply_text(t(lang, 'wu_id_taken'), reply_markup=admin_menu_keyboard(lang))
    else:
        await update.message.reply_text(
            t(lang, 'wu_added', website_id=website_id, name=text),
            reply_markup=admin_menu_keyboard(lang)
        )
    return ADMIN_MENU


# ──────────────────── STAFF ENTRY COMMANDS (/admin /partner /driver) ────────────────────

async def cmd_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Hidden command for admin access — not shown in bot menu."""
    context.user_data.clear()
    lang = get_lang(context, update.effective_user.id)
    await update.message.reply_text(t(lang, 'admin_enter_code'), reply_markup=ReplyKeyboardRemove())
    return ADMIN_CODE_STATE


async def cmd_partner(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Hidden command for partner access — not shown in bot menu."""
    context.user_data.clear()
    lang = get_lang(context, update.effective_user.id)
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


async def cmd_driver(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Hidden command for driver access — not shown in bot menu."""
    context.user_data.clear()
    lang = get_lang(context, update.effective_user.id)
    driver = db.get_driver_by_telegram(update.effective_user.id)
    if driver:
        context.user_data['driver_id'] = driver['id']
        await update.message.reply_text(
            t(lang, 'driver_welcome', name=driver['name']),
            reply_markup=driver_menu_keyboard(lang)
        )
        return DRIVER_MENU
    await update.message.reply_text(t(lang, 'driver_enter_code'), reply_markup=ReplyKeyboardRemove())
    return DRIVER_CODE_STATE


# ──────────────────── FALLBACK ────────────────────

async def fallback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await start(update, context)


# ──────────────────── FLASK KEEP-ALIVE + MINI APP API ────────────────────

def create_flask_app():
    flask_app = Flask(__name__)

    @flask_app.route('/')
    def health():
        return 'OK', 200

    @flask_app.route('/track/<tracking>')
    def track_api(tracking):
        parcel = db.get_parcel_by_tracking(tracking.upper())
        if not parcel:
            return jsonify({'error': 'not_found'}), 404
        partner = db.get_partner_by_id(parcel['partner_id'])
        events = db.get_parcel_timeline(parcel['id'])
        return jsonify({
            'tracking': parcel['tracking'],
            'status': parcel['status'],
            'country': parcel['destination_country'],
            'route_type': parcel['route_type'],
            'weight': parcel['chargeable_weight'],
            'price': parcel['price'],
            'partner': partner['name'] if partner else '—',
            'created_at': parcel['created_at'],
            'events': [
                {'status': e['status'], 'created_at': e['created_at']}
                for e in events
            ]
        })

    @flask_app.route('/calculate')
    def calculate_api():
        try:
            weight = float(flask_request.args.get('weight', 0))
            length = float(flask_request.args.get('length', 0))
            width = float(flask_request.args.get('width', 0))
            height = float(flask_request.args.get('height', 0))
            country = flask_request.args.get('country', 'KG').upper()
        except ValueError:
            return jsonify({'error': 'invalid_params'}), 400

        if country not in db.RATES:
            return jsonify({'error': 'invalid_country'}), 400

        vol, chargeable, price = db.calculate_price(weight, length, width, height, country)
        return jsonify({
            'actual': weight,
            'volumetric': vol,
            'chargeable': chargeable,
            'rate': db.RATES[country],
            'price': price,
            'country': country,
        })

    @flask_app.route('/rates')
    def rates_api():
        return jsonify(db.RATES)

    @flask_app.route('/miniapp')
    def miniapp():
        """Serve the mini app HTML."""
        import os
        miniapp_path = os.path.join(os.path.dirname(__file__), 'miniapp', 'index.html')
        if os.path.exists(miniapp_path):
            with open(miniapp_path, 'r', encoding='utf-8') as f:
                return f.read(), 200, {'Content-Type': 'text/html; charset=utf-8'}
        return 'Mini App not found', 404

    return flask_app


def run_flask():
    flask_app = create_flask_app()
    port = int(os.environ.get('PORT', 8080))
    flask_app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)


# ──────────────────── MAIN ────────────────────

def main():
    db.init_db()
    logger.info("Database initialized.")

    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    logger.info("Flask server started on port 8080.")

    application = Application.builder().token(BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler('start', start),
            CommandHandler('admin', cmd_admin),
            CommandHandler('partner', cmd_partner),
            CommandHandler('driver', cmd_driver),
        ],
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
            CLIENT_TYPE_SELECT: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, client_type_select)
            ],
            CLIENT_MENU: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, client_menu_handler)
            ],
            ORDER_MENU: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, order_menu_handler)
            ],
            SEND_MENU: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, send_menu_handler)
            ],
            CLIENT_TRACK: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, client_track)
            ],
            CLIENT_CALC_W: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, calc_weight)
            ],
            CLIENT_CALC_L: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, calc_dims)
            ],
            CLIENT_CALC_COUNTRY: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, calc_country)
            ],
            ADDRESS_VERIFY: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, address_verify)
            ],
            SHOPPING_REQUEST: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, shopping_request)
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
            ACCEPT_COUNTRY: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, accept_country)
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
            ADMIN_UPDATE_TRACKING: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, admin_update_tracking)
            ],
            ADMIN_UPDATE_STATUS: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, admin_update_status)
            ],
            ADMIN_BROADCAST: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, admin_broadcast)
            ],
            ADMIN_SET_ADDRESS: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, admin_set_address)
            ],
            ADMIN_ADD_WU_ID: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, admin_add_wu_id)
            ],
            ADMIN_ADD_WU_NAME: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, admin_add_wu_name)
            ],
            DRIVER_CODE_STATE: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, driver_code_handler)
            ],
            DRIVER_MENU: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, driver_menu_handler)
            ],
            DRIVER_DELIVER: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, driver_deliver)
            ],
        },
        fallbacks=[
            CommandHandler('start', start),
            MessageHandler(filters.ALL, fallback),
        ],
        allow_reentry=True,
    )

    application.add_handler(conv_handler)

    logger.info("OWAY Cargo bot is starting...")
    application.run_polling(drop_pending_updates=True)


if __name__ == '__main__':
    main()
