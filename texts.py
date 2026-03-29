TEXTS = {
    'ru': {
        # General
        'choose_language': 'Выберите язык / Choose language:',
        'welcome': 'Добро пожаловать в OWAY Cargo! 🚚\nВыберите вашу роль:',
        'choose_role': 'Выберите роль:',
        'btn_client': '📦 Клиент',
        'btn_partner': '🏪 Партнёр (пункт приёма)',
        'btn_admin': '⚙️ Администратор',
        'back': '⬅️ Назад',
        'cancel': '❌ Отмена',
        'main_menu': '🏠 Главное меню',
        'invalid_input': 'Неверный ввод. Попробуйте снова.',

        # Client registration
        'client_enter_name': 'Введите ваше имя:',
        'client_enter_phone': 'Нажмите кнопку ниже, чтобы поделиться своим номером телефона:',
        'btn_share_phone': '📱 Отправить мой номер',
        'phone_not_yours': '❌ Это не ваш номер. Нажмите кнопку, чтобы поделиться своим номером.',
        'client_registered': '✅ Регистрация завершена! Добро пожаловать, {name}!',
        'client_already_registered': '✅ Вы уже зарегистрированы. Добро пожаловать, {name}!',

        # Client menu
        'client_menu': '📦 Меню клиента\nВаш телефон: {phone}',
        'btn_track': '🔍 Отследить посылку',
        'btn_history': '📋 История посылок',
        'btn_calculator': '💰 Калькулятор цены',
        'btn_change_lang': '🌐 Сменить язык',

        # Tracking
        'enter_tracking': 'Введите трек-номер:',
        'parcel_not_found': '❌ Посылка с трек-номером {tracking} не найдена.',
        'parcel_info': (
            '📦 Посылка: {tracking}\n'
            '📍 Статус: {status}\n'
            '🏪 Пункт приёма: {partner}\n'
            '⚖️ Вес: {weight} кг\n'
            '📏 Размеры: {dims}\n'
            '💰 Стоимость: ${price}\n'
            '📅 Принята: {date}'
        ),
        'parcel_photo': '🖼️ Фото посылки:',
        'no_photo': 'Фото отсутствует.',
        'no_parcels': 'У вас нет посылок.',
        'parcel_history': '📋 Ваши посылки:',

        # Calculator
        'calc_enter_weight': 'Введите фактический вес (кг):',
        'calc_enter_length': 'Введите длину (см):',
        'calc_enter_width': 'Введите ширину (см):',
        'calc_enter_height': 'Введите высоту (см):',
        'calc_result': (
            '💰 Расчёт стоимости:\n\n'
            '⚖️ Фактический вес: {actual} кг\n'
            '📦 Объёмный вес: {vol} кг\n'
            '✅ Расчётный вес: {chargeable} кг\n'
            '💵 Стоимость: ${price}'
        ),

        # Statuses
        'status_accepted': '✅ Принята',
        'status_in_transit': '🚚 В пути',
        'status_delivered': '✅ Доставлена',

        # Partner
        'partner_enter_code': 'Введите код партнёра:',
        'partner_invalid_code': '❌ Неверный код партнёра.',
        'partner_welcome': '🏪 Добро пожаловать, {name}!\nПункт: {location}',
        'partner_menu': '🏪 Меню партнёра\n📍 {name} — {location}',
        'btn_accept_parcel': '📥 Принять посылку',
        'btn_my_parcels': '📋 Мои посылки',
        'btn_handoff': '🚚 Передать водителю',
        'btn_stats': '📊 Статистика',

        # Accept parcel flow
        'accept_send_photo': '📸 Сделайте фото посылки:',
        'accept_enter_weight': 'Введите вес посылки (кг):',
        'accept_enter_length': 'Введите длину (см):',
        'accept_enter_width': 'Введите ширину (см):',
        'accept_enter_height': 'Введите высоту (см):',
        'accept_enter_client_phone': '📱 Введите номер телефона клиента:',
        'accept_confirm': (
            '✅ Подтвердите приём посылки:\n\n'
            '📱 Клиент: {phone}\n'
            '⚖️ Вес: {weight} кг\n'
            '📏 Размеры: {l}×{w}×{h} см\n'
            '📦 Объёмный вес: {vol} кг\n'
            '✅ Расчётный вес: {chargeable} кг\n'
            '💰 Стоимость: ${price}'
        ),
        'btn_confirm': '✅ Подтвердить',
        'parcel_accepted': '✅ Посылка принята!\nТрек-номер: {tracking}',
        'invalid_number': '❌ Введите корректное число.',

        # Partner parcels list
        'no_parcels_at_point': 'На вашем пункте нет посылок.',
        'parcels_at_point': '📋 Посылки на вашем пункте:',
        'parcel_line': '• {tracking} | {weight}кг | ${price} | {status}',

        # Handoff
        'no_parcels_to_handoff': '❌ Нет посылок для передачи водителю.',
        'handoff_confirm': '🚚 Передать {count} посылок(ки) водителю?',
        'handoff_done': '✅ {count} посылок(ки) переданы водителю!',
        'handoff_notify': '🚚 Ваша посылка {tracking} передана водителю и находится в пути!',

        # Stats
        'partner_stats': (
            '📊 Статистика за 7 дней\n\n'
            '📦 Принято посылок: {count}\n'
            '⚖️ Общий вес: {weight} кг\n'
            '💰 Общая стоимость: ${revenue}\n'
            '🎁 Ваше вознаграждение (10%): ${reward}'
        ),

        # Admin
        'admin_enter_code': 'Введите код администратора:',
        'admin_invalid_code': '❌ Неверный код администратора.',
        'admin_welcome': '⚙️ Панель администратора OWAY Cargo',
        'admin_menu': '⚙️ Панель администратора',
        'btn_network_stats': '📊 Статистика сети',
        'btn_list_partners': '🏪 Список партнёров',
        'btn_add_partner': '➕ Добавить партнёра',

        # Admin stats
        'network_stats': (
            '📊 Статистика сети (последние 7 дней)\n\n'
            '📦 Всего посылок: {total}\n'
            '🚚 В пути: {in_transit}\n'
            '✅ Доставлено: {delivered}\n'
            '⚖️ Общий вес: {weight} кг\n'
            '💰 Общая выручка: ${revenue}\n'
            '🏪 Активных пунктов: {partners}'
        ),

        # Partners list
        'partners_list': '🏪 Список партнёров:',
        'partner_line': '• {name} | {location} | Код: {code} | Посылок: {count}',
        'no_partners': 'Партнёры не найдены.',

        # Add partner
        'add_partner_name': 'Введите название пункта:',
        'add_partner_location': 'Введите адрес пункта:',
        'add_partner_code': 'Введите код партнёра (уникальный):',
        'partner_code_exists': '❌ Такой код уже существует.',
        'partner_added': '✅ Партнёр добавлен!\nНазвание: {name}\nАдрес: {location}\nКод: {code}',

        # Notifications
        'notify_accepted': '📦 Ваша посылка принята!\n\nТрек-номер: {tracking}\nПункт: {partner}\n⚖️ Вес: {weight} кг\n💰 Стоимость: ${price}',
    },

    'en': {
        # General
        'choose_language': 'Выберите язык / Choose language:',
        'welcome': 'Welcome to OWAY Cargo! 🚚\nChoose your role:',
        'choose_role': 'Choose your role:',
        'btn_client': '📦 Client',
        'btn_partner': '🏪 Partner (drop-off point)',
        'btn_admin': '⚙️ Administrator',
        'back': '⬅️ Back',
        'cancel': '❌ Cancel',
        'main_menu': '🏠 Main menu',
        'invalid_input': 'Invalid input. Please try again.',

        # Client registration
        'client_enter_name': 'Enter your name:',
        'client_enter_phone': 'Press the button below to share your phone number:',
        'btn_share_phone': '📱 Share my number',
        'phone_not_yours': '❌ That is not your number. Please use the button to share your own number.',
        'client_registered': '✅ Registration complete! Welcome, {name}!',
        'client_already_registered': '✅ You are already registered. Welcome, {name}!',

        # Client menu
        'client_menu': '📦 Client Menu\nYour phone: {phone}',
        'btn_track': '🔍 Track parcel',
        'btn_history': '📋 Parcel history',
        'btn_calculator': '💰 Price calculator',
        'btn_change_lang': '🌐 Change language',

        # Tracking
        'enter_tracking': 'Enter tracking number:',
        'parcel_not_found': '❌ Parcel with tracking number {tracking} not found.',
        'parcel_info': (
            '📦 Parcel: {tracking}\n'
            '📍 Status: {status}\n'
            '🏪 Drop-off point: {partner}\n'
            '⚖️ Weight: {weight} kg\n'
            '📏 Dimensions: {dims}\n'
            '💰 Price: ${price}\n'
            '📅 Accepted: {date}'
        ),
        'parcel_photo': '🖼️ Parcel photo:',
        'no_photo': 'No photo available.',
        'no_parcels': 'You have no parcels.',
        'parcel_history': '📋 Your parcels:',

        # Calculator
        'calc_enter_weight': 'Enter actual weight (kg):',
        'calc_enter_length': 'Enter length (cm):',
        'calc_enter_width': 'Enter width (cm):',
        'calc_enter_height': 'Enter height (cm):',
        'calc_result': (
            '💰 Price calculation:\n\n'
            '⚖️ Actual weight: {actual} kg\n'
            '📦 Volumetric weight: {vol} kg\n'
            '✅ Chargeable weight: {chargeable} kg\n'
            '💵 Price: ${price}'
        ),

        # Statuses
        'status_accepted': '✅ Accepted',
        'status_in_transit': '🚚 In transit',
        'status_delivered': '✅ Delivered',

        # Partner
        'partner_enter_code': 'Enter partner code:',
        'partner_invalid_code': '❌ Invalid partner code.',
        'partner_welcome': '🏪 Welcome, {name}!\nPoint: {location}',
        'partner_menu': '🏪 Partner Menu\n📍 {name} — {location}',
        'btn_accept_parcel': '📥 Accept parcel',
        'btn_my_parcels': '📋 My parcels',
        'btn_handoff': '🚚 Hand off to driver',
        'btn_stats': '📊 Statistics',

        # Accept parcel flow
        'accept_send_photo': '📸 Take a photo of the parcel:',
        'accept_enter_weight': 'Enter parcel weight (kg):',
        'accept_enter_length': 'Enter length (cm):',
        'accept_enter_width': 'Enter width (cm):',
        'accept_enter_height': 'Enter height (cm):',
        'accept_enter_client_phone': '📱 Enter client phone number:',
        'accept_confirm': (
            '✅ Confirm parcel acceptance:\n\n'
            '📱 Client: {phone}\n'
            '⚖️ Weight: {weight} kg\n'
            '📏 Dimensions: {l}×{w}×{h} cm\n'
            '📦 Volumetric weight: {vol} kg\n'
            '✅ Chargeable weight: {chargeable} kg\n'
            '💰 Price: ${price}'
        ),
        'btn_confirm': '✅ Confirm',
        'parcel_accepted': '✅ Parcel accepted!\nTracking number: {tracking}',
        'invalid_number': '❌ Please enter a valid number.',

        # Partner parcels list
        'no_parcels_at_point': 'No parcels at your point.',
        'parcels_at_point': '📋 Parcels at your point:',
        'parcel_line': '• {tracking} | {weight}kg | ${price} | {status}',

        # Handoff
        'no_parcels_to_handoff': '❌ No parcels to hand off to driver.',
        'handoff_confirm': '🚚 Hand off {count} parcel(s) to driver?',
        'handoff_done': '✅ {count} parcel(s) handed off to driver!',
        'handoff_notify': '🚚 Your parcel {tracking} has been handed to the driver and is on its way!',

        # Stats
        'partner_stats': (
            '📊 Statistics for last 7 days\n\n'
            '📦 Parcels accepted: {count}\n'
            '⚖️ Total weight: {weight} kg\n'
            '💰 Total revenue: ${revenue}\n'
            '🎁 Your reward (10%): ${reward}'
        ),

        # Admin
        'admin_enter_code': 'Enter admin code:',
        'admin_invalid_code': '❌ Invalid admin code.',
        'admin_welcome': '⚙️ OWAY Cargo Admin Panel',
        'admin_menu': '⚙️ Admin Panel',
        'btn_network_stats': '📊 Network statistics',
        'btn_list_partners': '🏪 Partners list',
        'btn_add_partner': '➕ Add partner',

        # Admin stats
        'network_stats': (
            '📊 Network Statistics (last 7 days)\n\n'
            '📦 Total parcels: {total}\n'
            '🚚 In transit: {in_transit}\n'
            '✅ Delivered: {delivered}\n'
            '⚖️ Total weight: {weight} kg\n'
            '💰 Total revenue: ${revenue}\n'
            '🏪 Active points: {partners}'
        ),

        # Partners list
        'partners_list': '🏪 Partners list:',
        'partner_line': '• {name} | {location} | Code: {code} | Parcels: {count}',
        'no_partners': 'No partners found.',

        # Add partner
        'add_partner_name': 'Enter point name:',
        'add_partner_location': 'Enter point address:',
        'add_partner_code': 'Enter partner code (must be unique):',
        'partner_code_exists': '❌ This code already exists.',
        'partner_added': '✅ Partner added!\nName: {name}\nAddress: {location}\nCode: {code}',

        # Notifications
        'notify_accepted': '📦 Your parcel has been accepted!\n\nTracking: {tracking}\nPoint: {partner}\n⚖️ Weight: {weight} kg\n💰 Price: ${price}',
    }
}


def t(lang: str, key: str, **kwargs) -> str:
    text = TEXTS.get(lang, TEXTS['en']).get(key, TEXTS['en'].get(key, key))
    if kwargs:
        try:
            return text.format(**kwargs)
        except (KeyError, IndexError):
            return text
    return text
