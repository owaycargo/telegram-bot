TEXTS = {
    'ru': {
        # General
        'choose_language': '🌐 Выберите язык / Choose language:\n\n🇷🇺 Русский · 🇬🇧 English · 🇰🇬 Кыргызча · 🇰🇿 Қазақша · 🇺🇿 O\'zbek',
        'welcome': 'Добро пожаловать в OWAY Cargo! 🚚\nВыберите вашу роль:',
        'choose_role': 'Выберите роль:',
        'btn_client': '📦 Клиент',
        'btn_partner': '🏪 Партнёр (пункт приёма)',
        'btn_driver': '🚗 Водитель',
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

        # Client type selection
        'client_type_select': (
            '👋 Добро пожаловать в OWAY Cargo!\n\n'
            'Выберите, что вы хотите сделать:\n\n'
            '🛒 Заказать из США — купить товар в США и получить в своей стране\n\n'
            '📦 Отправить из США — вы находитесь в США и хотите отправить посылку в СНГ'
        ),
        'btn_order_type': '🛒 Заказать из США',
        'btn_send_type': '📦 Отправить из США',

        # Order menu (CIS clients ordering from USA)
        'order_menu': '🛒 Заказать из США\nВаш телефон: {phone}',
        'btn_my_address': '🏠 Мой адрес в США',
        'btn_shopping': '🛍️ Шопинг-помощник',
        'btn_faq': '❓ Частые вопросы',
        'btn_miniapp': '🌐 Открыть приложение',

        # Send menu (USA clients sending to CIS)
        'send_menu': '📦 Отправить из США\nВаш телефон: {phone}',
        'btn_find_dropoff': '📍 Пункты приёма',

        # Shared client menu buttons
        'btn_track': '🔍 Отследить посылку',
        'btn_history': '📋 История посылок',
        'btn_calculator': '💰 Калькулятор цены',
        'btn_support': '💬 Поддержка',
        'btn_change_lang': '🌐 Сменить язык',
        'btn_recalculate': '🔄 Рассчитать ещё раз',
        'btn_contact_manager': '📞 Связаться с менеджером',

        # Legacy client_menu (kept for fallback)
        'client_menu': '📦 Меню клиента\nВаш телефон: {phone}',

        # Tracking
        'enter_tracking': 'Введите трек-номер:',
        'parcel_not_found': '❌ Посылка с трек-номером {tracking} не найдена.',
        'parcel_info': (
            '📦 Посылка: {tracking}\n'
            '🌍 Страна: {country}\n'
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
        'calc_enter_weight': (
            '⚖️ Введите вес посылки:\n\n'
            'Примеры: 15.3, 15,3, 15.3 кг, 26 lb\n'
            '(кг или фунты — переведу автоматически)'
        ),
        'calc_weight_accepted': '✅ Принято: {input} = {kg} кг',
        'calc_weight_help': (
            'Введите вес в одном из форматов:\n'
            '• 15.3\n• 15,3\n• 15 кг\n• 26 lb'
        ),
        'calc_enter_dims': (
            '📐 Введите габариты одной строкой (Д×Ш×В):\n\n'
            'Примеры:\n'
            '• 40x30x20\n'
            '• 40x30x20 cm\n'
            '• 16x12x10 in'
        ),
        'calc_dims_accepted': '✅ Принято: {input} = {l}×{w}×{h} см',
        'calc_dims_help': (
            'Введите габариты одной строкой:\n'
            '40x30x20 см  или  16x12x10 in\n\n'
            'Разделители: x, ×, *, пробел'
        ),
        'calc_dims_error': (
            '❓ Не смог разобрать габариты.\n\n'
            'Пришли в формате: 40x30x20 или 16x12x10 in'
        ),
        'calc_weight_error': (
            '❓ Не смог разобрать вес.\n\n'
            'Пришли в формате: 15.3 кг или 26 lb'
        ),
        'calc_choose_country': '🌍 Выберите страну назначения:',
        'calc_result': (
            '💰 Расчёт стоимости:\n\n'
            '🌍 Страна: {country}\n'
            '💲 Тариф: ${rate}/кг\n'
            '⚖️ Фактический вес: {actual} кг\n'
            '📦 Объёмный вес: {vol} кг\n'
            '✅ Расчётный вес: {chargeable} кг\n'
            '💵 Итого: ${price}'
        ),

        # Support
        'support_message': (
            '💬 Поддержка OWAY Cargo\n\n'
            '🌍 Клиенты из СНГ:\n'
            'WhatsApp: +996 709 969621\n'
            '📲 t.me/+996709969621\n\n'
            '🇺🇸 Клиенты из США:\n'
            'WhatsApp: +1 213 276 6898\n'
            '📲 t.me/+12132766898'
        ),

        # Statuses — DIRECT (KG, KZ, UZ)
        'status_accepted': '✅ Принята в США',
        'status_in_transit': '✈️ В пути',
        'status_arrived': '📍 Прибыла в страну назначения',
        'status_customs': '🛃 Проходит таможенное оформление',
        'status_ready': '📦 Готова к выдаче',
        'status_delivered': '🏠 Доставлена',

        # Statuses — TRANSIT (RU, BY) — Kyrgyzstan hidden
        'status_transit_zone': '🔄 В транзитной зоне',
        'status_arrived_moscow': '📍 Прибыла в Москву',
        'status_with_driver': '🚚 Передана в доставку (СДЭК)',

        # Country selection
        'accept_choose_country': '🌍 Выберите страну назначения:',
        'country_KG': '🇰🇬 Кыргызстан',
        'country_KZ': '🇰🇿 Казахстан',
        'country_UZ': '🇺🇿 Узбекистан',
        'country_RU': '🇷🇺 Россия',
        'country_BY': '🇧🇾 Беларусь',

        # Timeline
        'parcel_timeline': '🕐 История статусов:',
        'timeline_line': '{icon} {status} — {date}',

        # Admin status update
        'btn_update_status': '🔄 Обновить статус посылки',
        'admin_enter_tracking': 'Введите трек-номер посылки:',
        'admin_parcel_not_found': '❌ Посылка {tracking} не найдена.',
        'admin_choose_status': (
            'Посылка: {tracking}\n'
            'Текущий статус: {status}\n\n'
            'Выберите новый статус:'
        ),
        'admin_status_updated': '✅ Статус посылки {tracking} обновлён:\n{status}',
        'notify_status_changed': (
            '📬 Обновление по вашей посылке!\n\n'
            '🔢 Трек-номер: {tracking}\n'
            '📦 Новый статус: {status}\n\n'
            'Отслеживайте посылку в боте: /start'
        ),
        'notify_shopping_new': (
            '🛍 Новая заявка на покупку!\n\n'
            '👤 Клиент: {name}\n'
            '📞 Телефон: {phone}\n'
            '📝 Запрос:\n{request}'
        ),

        # US Address verification
        'address_enter_id': (
            '🔑 Введите ваш ID с сайта owaycargo.com\n\n'
            'Если вы ещё не зарегистрированы на сайте — перейдите на owaycargo.com и создайте аккаунт.\n'
            'После регистрации ваш ID будет доступен в личном кабинете.'
        ),
        'address_not_found': (
            '❌ ID {website_id} не найден в системе.\n\n'
            'Убедитесь, что вы правильно ввели ID, или обратитесь в поддержку:\n'
            'WhatsApp: +996 709 969621'
        ),
        'your_us_address': (
            '🏠 Ваш адрес для получения посылок в США:\n\n'
            '{address}\n\n'
            '📝 Укажите этот адрес при оформлении заказов в американских интернет-магазинах.\n'
            '📦 После доставки в наш склад мы отправим посылку на ваш адрес в СНГ.'
        ),
        'address_already_set': (
            '✅ Ваш аккаунт привязан к сайту.\n\n'
            '🏠 Ваш адрес в США:\n\n{address}'
        ),

        # Shopping assistant
        'shopping_intro': (
            '🛍️ Шопинг-помощник OWAY Cargo\n\n'
            'Мы купим любой товар из США за вас!\n\n'
            'Укажите в вашем сообщении:\n'
            '• Ссылку на товар или название магазина\n'
            '• Описание товара (цвет, размер, модель)\n'
            '• Желаемый бюджет (в $)\n\n'
            '💰 Комиссия за услугу: 10% от стоимости товара\n'
            '⏱ Ответ менеджера: в течение 24 часов'
        ),
        'shopping_enter_request': '✍️ Опишите ваш запрос подробно:',
        'shopping_received': (
            '✅ Ваш запрос принят!\n\n'
            'Наш менеджер свяжется с вами по номеру {phone} в ближайшее время.\n\n'
            'Спасибо за доверие OWAY Cargo! 🚚'
        ),
        'btn_my_requests': '🛍 Мои заявки',
        'my_requests_empty': 'У вас пока нет заявок на покупку.',
        'my_requests_header': '🛍 Ваши заявки:\n',
        'request_status_new': '🟡 Новая',
        'request_status_in_progress': '🔵 В работе',
        'request_status_done': '✅ Выполнена',
        'request_status_cancelled': '❌ Отменена',
        'my_request_line': '#{id} {status}\n📝 {text}\n📅 {date}\n',
        'notify_request_updated': (
            '🛍 Обновление по вашей заявке #{id}:\n\n'
            '📝 {text}\n'
            '📦 Новый статус: {status}'
        ),
        'shopping_notify_admin': (
            '🛍️ Новый запрос шопинг-помощника!\n\n'
            '👤 Клиент: {name}\n'
            '📱 Телефон: {phone}\n'
            '📝 Запрос:\n{request}'
        ),

        # FAQ for ORDER clients (CIS)
        'faq_order': (
            '❓ Частые вопросы — Заказать из США\n\n'
            '1️⃣ Как получить адрес в США?\n'
            'Зарегистрируйтесь на owaycargo.com → получите личный ID → '
            'введите его в боте через «Мой адрес в США». Адрес склада будет сразу показан.\n\n'
            '2️⃣ Как отследить посылку?\n'
            'Нажмите «Отследить посылку», введите трек-номер. '
            'Трек-номер вы получите при уведомлении о приёме.\n\n'
            '3️⃣ Сколько стоит доставка?\n'
            '🇰🇬 Кыргызстан, 🇰🇿 Казахстан, 🇺🇿 Узбекистан: $12/кг\n'
            '🇷🇺 Россия, 🇧🇾 Беларусь: $18/кг\n'
            'Расчёт по объёмному или фактическому весу (максимум из двух).\n\n'
            '4️⃣ Как долго идёт доставка?\n'
            '🇰🇬 Кыргызстан: 7–9 рабочих дней.\n'
            '🇰🇿 Казахстан / 🇺🇿 Узбекистан: 10–14 рабочих дней.\n'
            '🇷🇺 Россия / 🇧🇾 Беларусь: 15–21 рабочий день.\n\n'
            '5️⃣ Что такое Шопинг-помощник?\n'
            'Наш менеджер купит любой товар из США за вас. '
            'Комиссия — 10% от стоимости товара. '
            'Напишите запрос через «Шопинг-помощник».\n\n'
            '6️⃣ Какие товары запрещены?\n'
            'Нельзя отправлять: оружие, наркотики, опасные вещества, '
            'скоропортящиеся продукты, живые животные, '
            'товары с ограничениями на ввоз.\n\n'
            '7️⃣ Контакты поддержки:\n'
            '🌍 СНГ: WhatsApp +996 709 969621\n'
            '🇺🇸 США: WhatsApp +1 213 276 6898'
        ),

        # FAQ for SEND clients (USA)
        'faq_send': (
            '❓ Частые вопросы — Отправить из США\n\n'
            '1️⃣ Где сдать посылку?\n'
            'Найдите ближайший пункт через «Пункты приёма» в меню. '
            'Сотрудник пункта примет посылку, взвесит и выдаст трек-номер.\n\n'
            '2️⃣ Сколько стоит доставка?\n'
            '🇰🇬 Кыргызстан, 🇰🇿 Казахстан, 🇺🇿 Узбекистан: $12/кг\n'
            '🇷🇺 Россия, 🇧🇾 Беларусь: $18/кг\n'
            'Используйте «Калькулятор» для точного расчёта.\n\n'
            '3️⃣ Какие документы нужны?\n'
            'Нужен только номер телефона получателя. '
            'Для дорогостоящих товаров может потребоваться чек/инвойс.\n\n'
            '4️⃣ Как упаковать посылку?\n'
            'Упакуйте надёжно: коробка, скотч, пузырчатая плёнка для хрупких вещей. '
            'Одежду и мягкие вещи можно в пакет. '
            'Пункт помогает с упаковкой за доп. плату.\n\n'
            '5️⃣ Какие товары запрещены к отправке?\n'
            'Нельзя: оружие, боеприпасы, жидкости >100 мл (авиа), '
            'аэрозоли, опасные химикаты, скоропортящееся.\n\n'
            '6️⃣ Как получатель отслеживает посылку?\n'
            'Получатель регистрируется в этом же боте и вводит трек-номер '
            'в разделе «Отследить посылку». При каждом изменении статуса приходит уведомление.\n\n'
            '7️⃣ Контакты поддержки:\n'
            '🇺🇸 США: WhatsApp +1 213 276 6898\n'
            '🌍 СНГ: WhatsApp +996 709 969621'
        ),

        # Drop-off points
        'dropoffs_list': '📍 Пункты приёма посылок в США:',
        'dropoff_line': '• {name} — {location}',
        'no_dropoffs': 'Пункты приёма в США пока не добавлены.\nСвяжитесь с нами: +1 213 276 6898',

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
            '🌍 Страна: {country}\n'
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
        'btn_broadcast': '📢 Рассылка клиентам',
        'btn_set_address': '🏠 Изменить адрес склада',
        'btn_add_website_user': '👤 Добавить ID пользователя',
        'btn_view_requests': '🛍️ Заявки шопинга',
        'btn_update_request': '✏️ Обновить статус заявки',
        'admin_update_request_enter_id': 'Введите номер заявки (например: 3):',
        'admin_request_not_found': '❌ Заявка #{id} не найдена.',
        'admin_request_found': (
            '📋 Заявка #{id}\n'
            '👤 {client} | {phone}\n'
            '📝 {text}\n'
            '📅 {date}\n'
            '📦 Статус: {status}\n\n'
            'Выберите новый статус:'
        ),
        'admin_request_updated': '✅ Заявка #{id} обновлена: {status}',

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

        # Admin broadcast
        'broadcast_enter_msg': (
            '📢 Введите текст рассылки:\n\n'
            'Сообщение будет отправлено всем зарегистрированным клиентам.'
        ),
        'broadcast_sent': '✅ Рассылка выполнена!\nОтправлено: {sent} | Ошибок: {failed}',

        # Admin set warehouse address
        'set_address_enter': (
            '🏠 Введите новый адрес склада в США:\n\n'
            'Текущий адрес:\n{current}'
        ),
        'address_updated': '✅ Адрес склада обновлён!',

        # Admin add website user
        'add_wu_id_enter': '👤 Введите ID пользователя с сайта owaycargo.com:',
        'add_wu_name_enter': 'Введите имя пользователя (ID: {website_id}):',
        'wu_added': '✅ Пользователь добавлен!\nID: {website_id}\nИмя: {name}',
        'wu_id_taken': '❌ Пользователь с таким ID уже существует.',

        # Admin view shopping requests
        'view_requests_empty': '🛍️ Новых заявок шопинга нет.',
        'view_requests_header': '🛍️ Новые заявки шопинга:\n',
        'request_line': '#{id} | {client} | {phone}\n📝 {text}\n📅 {date}\n',

        # Notifications
        'notify_accepted': (
            '📦 Ваша посылка принята в пункте OWAY!\n\n'
            '🔢 Трек-номер: {tracking}\n'
            '📍 Пункт приёма: {partner}\n'
            '⚖️ Расчётный вес: {weight} кг\n'
            '💰 Стоимость доставки: ${price}\n'
            '🕐 Ожидаемый срок: {delivery_days}\n\n'
            'Отслеживайте посылку: /start → Отследить посылку'
        ),
        'delivery_days_kg': '7–9 рабочих дней',
        'delivery_days_kz': '10–14 рабочих дней',
        'delivery_days_uz': '10–14 рабочих дней',
        'delivery_days_ru': '15–21 рабочий день',
        'delivery_days_by': '15–21 рабочий день',

        # Driver
        'driver_enter_code': 'Введите код водителя:',
        'driver_invalid_code': '❌ Неверный код водителя.',
        'driver_welcome': '🚗 Добро пожаловать, {name}!',
        'driver_menu': '🚗 Меню водителя',
        'btn_my_deliveries': '📋 Мои доставки',
        'btn_mark_delivered': '✅ Отметить доставлено',
        'no_deliveries': 'Нет посылок для доставки.',
        'deliveries_list': '📋 Посылки для доставки:',
        'driver_enter_tracking': 'Введите трек-номер доставленной посылки:',
        'driver_delivered_ok': '✅ Посылка {tracking} отмечена как доставленная!',
        'driver_parcel_not_found': '❌ Посылка {tracking} не найдена или уже доставлена.',
        'notify_delivered': '🏠 Ваша посылка {tracking} доставлена! Спасибо, что выбрали OWAY Cargo.',
    },

    'en': {
        # General
        'choose_language': '🌐 Выберите язык / Choose language:\n\n🇷🇺 Русский · 🇬🇧 English · 🇰🇬 Кыргызча · 🇰🇿 Қазақша · 🇺🇿 O\'zbek',
        'welcome': 'Welcome to OWAY Cargo! 🚚\nChoose your role:',
        'choose_role': 'Choose your role:',
        'btn_client': '📦 Client',
        'btn_partner': '🏪 Partner (drop-off point)',
        'btn_driver': '🚗 Driver',
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

        # Client type selection
        'client_type_select': (
            '👋 Welcome to OWAY Cargo!\n\n'
            'What would you like to do?\n\n'
            '🛒 Order from USA — buy goods in the USA and receive them in your country\n\n'
            '📦 Send from USA — you are in the USA and want to send a package to CIS countries'
        ),
        'btn_order_type': '🛒 Order from USA',
        'btn_send_type': '📦 Send from USA',

        # Order menu (CIS clients)
        'order_menu': '🛒 Order from USA\nYour phone: {phone}',
        'btn_my_address': '🏠 My US Address',
        'btn_shopping': '🛍️ Shopping Assistant',
        'btn_faq': '❓ FAQ',
        'btn_miniapp': '🌐 Open App',

        # Send menu (USA clients)
        'send_menu': '📦 Send from USA\nYour phone: {phone}',
        'btn_find_dropoff': '📍 Drop-off Points',

        # Shared buttons
        'btn_track': '🔍 Track parcel',
        'btn_history': '📋 Parcel history',
        'btn_calculator': '💰 Price calculator',
        'btn_support': '💬 Support',
        'btn_change_lang': '🌐 Change language',
        'btn_recalculate': '🔄 Calculate again',
        'btn_contact_manager': '📞 Contact manager',

        # Legacy
        'client_menu': '📦 Client Menu\nYour phone: {phone}',

        # Tracking
        'enter_tracking': 'Enter tracking number:',
        'parcel_not_found': '❌ Parcel with tracking number {tracking} not found.',
        'parcel_info': (
            '📦 Parcel: {tracking}\n'
            '🌍 Country: {country}\n'
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
        'calc_enter_weight': (
            '⚖️ Enter package weight:\n\n'
            'Examples: 15.3, 15,3, 15.3 kg, 26 lb\n'
            '(kg or pounds — I\'ll convert automatically)'
        ),
        'calc_weight_accepted': '✅ Accepted: {input} = {kg} kg',
        'calc_weight_help': (
            'Enter weight in any format:\n'
            '• 15.3\n• 15,3\n• 15 kg\n• 26 lb'
        ),
        'calc_enter_dims': (
            '📐 Enter dimensions in one line (L×W×H):\n\n'
            'Examples:\n'
            '• 40x30x20\n'
            '• 40x30x20 cm\n'
            '• 16x12x10 in'
        ),
        'calc_dims_accepted': '✅ Accepted: {input} = {l}×{w}×{h} cm',
        'calc_dims_help': (
            'Enter dimensions in one line:\n'
            '40x30x20 cm  or  16x12x10 in\n\n'
            'Separators: x, ×, *, space'
        ),
        'calc_dims_error': (
            '❓ Could not parse dimensions.\n\n'
            'Please send: 40x30x20 or 16x12x10 in'
        ),
        'calc_weight_error': (
            '❓ Could not parse weight.\n\n'
            'Please send: 15.3 kg or 26 lb'
        ),
        'calc_choose_country': '🌍 Choose destination country:',
        'calc_result': (
            '💰 Price calculation:\n\n'
            '🌍 Country: {country}\n'
            '💲 Rate: ${rate}/kg\n'
            '⚖️ Actual weight: {actual} kg\n'
            '📦 Volumetric weight: {vol} kg\n'
            '✅ Chargeable weight: {chargeable} kg\n'
            '💵 Total: ${price}'
        ),

        # Support
        'support_message': (
            '💬 OWAY Cargo Support\n\n'
            '🌍 CIS clients:\n'
            'WhatsApp: +996 709 969621\n'
            '📲 t.me/+996709969621\n\n'
            '🇺🇸 USA clients:\n'
            'WhatsApp: +1 213 276 6898\n'
            '📲 t.me/+12132766898'
        ),

        # Statuses — DIRECT (KG, KZ, UZ)
        'status_accepted': '✅ Accepted in USA',
        'status_in_transit': '✈️ In transit',
        'status_arrived': '📍 Arrived in destination country',
        'status_customs': '🛃 Customs clearance',
        'status_ready': '📦 Ready for pickup',
        'status_delivered': '🏠 Delivered',

        # Statuses — TRANSIT (RU, BY)
        'status_transit_zone': '🔄 In transit zone',
        'status_arrived_moscow': '📍 Arrived in Moscow',
        'status_with_driver': '🚚 Handed to courier (CDEK)',

        # Country selection
        'accept_choose_country': '🌍 Choose destination country:',
        'country_KG': '🇰🇬 Kyrgyzstan',
        'country_KZ': '🇰🇿 Kazakhstan',
        'country_UZ': '🇺🇿 Uzbekistan',
        'country_RU': '🇷🇺 Russia',
        'country_BY': '🇧🇾 Belarus',

        # Timeline
        'parcel_timeline': '🕐 Status history:',
        'timeline_line': '{icon} {status} — {date}',

        # Admin status update
        'btn_update_status': '🔄 Update parcel status',
        'admin_enter_tracking': 'Enter parcel tracking number:',
        'admin_parcel_not_found': '❌ Parcel {tracking} not found.',
        'admin_choose_status': (
            'Parcel: {tracking}\n'
            'Current status: {status}\n\n'
            'Choose new status:'
        ),
        'admin_status_updated': '✅ Parcel {tracking} status updated:\n{status}',
        'notify_status_changed': (
            '📬 Update on your parcel!\n\n'
            '🔢 Tracking: {tracking}\n'
            '📦 New status: {status}\n\n'
            'Track your parcel in the bot: /start'
        ),
        'notify_shopping_new': (
            '🛍 New shopping request!\n\n'
            '👤 Client: {name}\n'
            '📞 Phone: {phone}\n'
            '📝 Request:\n{request}'
        ),

        # US Address verification
        'address_enter_id': (
            '🔑 Enter your ID from owaycargo.com\n\n'
            'If you have not registered on the website yet, go to owaycargo.com and create an account.\n'
            'After registration your ID will be available in your personal account.'
        ),
        'address_not_found': (
            '❌ ID {website_id} was not found in our system.\n\n'
            'Please check your ID or contact support:\n'
            'WhatsApp: +1 213 276 6898'
        ),
        'your_us_address': (
            '🏠 Your US address for receiving packages:\n\n'
            '{address}\n\n'
            '📝 Use this address when placing orders at American online stores.\n'
            '📦 Once your package arrives at our warehouse we will forward it to your CIS address.'
        ),
        'address_already_set': (
            '✅ Your account is linked to the website.\n\n'
            '🏠 Your US Address:\n\n{address}'
        ),

        # Shopping assistant
        'shopping_intro': (
            '🛍️ OWAY Cargo Shopping Assistant\n\n'
            'We will buy any item from the USA for you!\n\n'
            'Please include in your message:\n'
            '• Link to the product or store name\n'
            '• Product description (color, size, model)\n'
            '• Desired budget (in $)\n\n'
            '💰 Service fee: 10% of product cost\n'
            '⏱ Manager response: within 24 hours'
        ),
        'shopping_enter_request': '✍️ Describe your request in detail:',
        'shopping_received': (
            '✅ Your request has been received!\n\n'
            'Our manager will contact you at {phone} shortly.\n\n'
            'Thank you for choosing OWAY Cargo! 🚚'
        ),
        'btn_my_requests': '🛍 My requests',
        'my_requests_empty': 'You have no shopping requests yet.',
        'my_requests_header': '🛍 Your requests:\n',
        'request_status_new': '🟡 New',
        'request_status_in_progress': '🔵 In progress',
        'request_status_done': '✅ Done',
        'request_status_cancelled': '❌ Cancelled',
        'my_request_line': '#{id} {status}\n📝 {text}\n📅 {date}\n',
        'notify_request_updated': (
            '🛍 Update on your request #{id}:\n\n'
            '📝 {text}\n'
            '📦 New status: {status}'
        ),
        'shopping_notify_admin': (
            '🛍️ New Shopping Assistant request!\n\n'
            '👤 Client: {name}\n'
            '📱 Phone: {phone}\n'
            '📝 Request:\n{request}'
        ),

        # FAQ for ORDER clients (CIS)
        'faq_order': (
            '❓ FAQ — Order from USA\n\n'
            '1️⃣ How do I get a US address?\n'
            'Register at owaycargo.com → get your personal ID → '
            'enter it in the bot via "My US Address". The warehouse address will be shown immediately.\n\n'
            '2️⃣ How do I track my parcel?\n'
            'Press "Track parcel" and enter your tracking number. '
            'You will receive the tracking number when the parcel is accepted.\n\n'
            '3️⃣ How much does delivery cost?\n'
            '🇰🇬 Kyrgyzstan, 🇰🇿 Kazakhstan, 🇺🇿 Uzbekistan: $12/kg\n'
            '🇷🇺 Russia, 🇧🇾 Belarus: $18/kg\n'
            'Calculated by volumetric or actual weight (whichever is higher).\n\n'
            '4️⃣ How long does delivery take?\n'
            '🇰🇬 Kyrgyzstan: 7–9 business days.\n'
            '🇰🇿 Kazakhstan / 🇺🇿 Uzbekistan: 10–14 business days.\n'
            '🇷🇺 Russia / 🇧🇾 Belarus: 15–21 business days.\n\n'
            '5️⃣ What is the Shopping Assistant?\n'
            'Our manager will buy any product from the USA for you. '
            'Commission: 10% of the product price. '
            'Send your request via "Shopping Assistant".\n\n'
            '6️⃣ What items are prohibited?\n'
            'Prohibited: weapons, drugs, hazardous materials, '
            'perishable food, live animals, import-restricted items.\n\n'
            '7️⃣ Support contacts:\n'
            '🌍 CIS: WhatsApp +996 709 969621\n'
            '🇺🇸 USA: WhatsApp +1 213 276 6898'
        ),

        # FAQ for SEND clients (USA)
        'faq_send': (
            '❓ FAQ — Send from USA\n\n'
            '1️⃣ Where can I drop off my parcel?\n'
            'Find the nearest drop-off point via "Drop-off Points" in the menu. '
            'The staff will accept your parcel, weigh it and provide a tracking number.\n\n'
            '2️⃣ How much does shipping cost?\n'
            '🇰🇬 Kyrgyzstan, 🇰🇿 Kazakhstan, 🇺🇿 Uzbekistan: $12/kg\n'
            '🇷🇺 Russia, 🇧🇾 Belarus: $18/kg\n'
            'Use the "Calculator" for an exact quote.\n\n'
            '3️⃣ What documents do I need?\n'
            "Just the recipient's phone number. "
            'For high-value items, a receipt/invoice may be required.\n\n'
            '4️⃣ How should I pack my parcel?\n'
            'Pack securely: box, tape, bubble wrap for fragile items. '
            'Clothing and soft items can go in a bag. '
            'Drop-off point staff can assist with packaging for an extra fee.\n\n'
            '5️⃣ What items cannot be shipped?\n'
            'Prohibited: weapons, ammunition, liquids >100ml (air), '
            'aerosols, hazardous chemicals, perishables.\n\n'
            '6️⃣ How does the recipient track the parcel?\n'
            'The recipient registers in this bot and enters the tracking number '
            'in "Track parcel". Status notifications are sent automatically.\n\n'
            '7️⃣ Support contacts:\n'
            '🇺🇸 USA: WhatsApp +1 213 276 6898\n'
            '🌍 CIS: WhatsApp +996 709 969621'
        ),

        # Drop-off points
        'dropoffs_list': '📍 US Drop-off Points:',
        'dropoff_line': '• {name} — {location}',
        'no_dropoffs': 'No US drop-off points have been added yet.\nContact us: +1 213 276 6898',

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
            '🌍 Country: {country}\n'
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
        'btn_broadcast': '📢 Broadcast to clients',
        'btn_set_address': '🏠 Change warehouse address',
        'btn_add_website_user': '👤 Add website user ID',
        'btn_view_requests': '🛍️ Shopping requests',
        'btn_update_request': '✏️ Update request status',
        'admin_update_request_enter_id': 'Enter request number (e.g.: 3):',
        'admin_request_not_found': '❌ Request #{id} not found.',
        'admin_request_found': (
            '📋 Request #{id}\n'
            '👤 {client} | {phone}\n'
            '📝 {text}\n'
            '📅 {date}\n'
            '📦 Status: {status}\n\n'
            'Choose new status:'
        ),
        'admin_request_updated': '✅ Request #{id} updated: {status}',

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

        # Admin broadcast
        'broadcast_enter_msg': (
            '📢 Enter broadcast message:\n\n'
            'This message will be sent to all registered clients.'
        ),
        'broadcast_sent': '✅ Broadcast complete!\nSent: {sent} | Failed: {failed}',

        # Admin set warehouse address
        'set_address_enter': (
            '🏠 Enter new US warehouse address:\n\n'
            'Current address:\n{current}'
        ),
        'address_updated': '✅ Warehouse address updated!',

        # Admin add website user
        'add_wu_id_enter': '👤 Enter the user ID from owaycargo.com:',
        'add_wu_name_enter': 'Enter user name (ID: {website_id}):',
        'wu_added': '✅ User added!\nID: {website_id}\nName: {name}',
        'wu_id_taken': '❌ A user with this ID already exists.',

        # Admin view shopping requests
        'view_requests_empty': '🛍️ No new shopping requests.',
        'view_requests_header': '🛍️ New shopping requests:\n',
        'request_line': '#{id} | {client} | {phone}\n📝 {text}\n📅 {date}\n',

        # Notifications
        'notify_accepted': (
            '📦 Your parcel has been accepted at OWAY!\n\n'
            '🔢 Tracking: {tracking}\n'
            '📍 Drop-off point: {partner}\n'
            '⚖️ Chargeable weight: {weight} kg\n'
            '💰 Delivery cost: ${price}\n'
            '🕐 Estimated delivery: {delivery_days}\n\n'
            'Track your parcel: /start → Track parcel'
        ),
        'delivery_days_kg': '7–9 business days',
        'delivery_days_kz': '10–14 business days',
        'delivery_days_uz': '10–14 business days',
        'delivery_days_ru': '15–21 business days',
        'delivery_days_by': '15–21 business days',

        # Driver
        'driver_enter_code': 'Enter driver code:',
        'driver_invalid_code': '❌ Invalid driver code.',
        'driver_welcome': '🚗 Welcome, {name}!',
        'driver_menu': '🚗 Driver Menu',
        'btn_my_deliveries': '📋 My deliveries',
        'btn_mark_delivered': '✅ Mark as delivered',
        'no_deliveries': 'No parcels to deliver.',
        'deliveries_list': '📋 Parcels for delivery:',
        'driver_enter_tracking': 'Enter tracking number of delivered parcel:',
        'driver_delivered_ok': '✅ Parcel {tracking} marked as delivered!',
        'driver_parcel_not_found': '❌ Parcel {tracking} not found or already delivered.',
        'notify_delivered': '🏠 Your parcel {tracking} has been delivered! Thank you for choosing OWAY Cargo.',
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
