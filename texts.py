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
        'btn_referral': '👥 Пригласить друга',
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
        'referral_info': (
            '👥 Пригласи друга — получите бонус оба!\n\n'
            '🎁 Ты получишь: 1 кг бесплатной доставки\n'
            '🎁 Друг получит: скидку 10% на первый заказ\n\n'
            '⚠️ Бонус начисляется только после того как посылка друга доставлена — '
            'никакого скама, всё честно.\n\n'
            '🔗 Твоя личная ссылка:\n{link}\n\n'
            '📊 Статистика:\n'
            '• Приглашено друзей: {invited}\n'
            '• Бонусов получено: {bonuses} кг'
        ),
        'notify_referral_bonus_referrer': (
            '🎉 Твой друг получил посылку!\n\n'
            'Тебе начислен бонус: +1 кг бесплатной доставки 🎁\n\n'
            'Бонус будет применён к твоему следующему заказу автоматически. '
            'Напомни менеджеру при оформлении.'
        ),
        'notify_referral_bonus_referred': (
            '🎉 Поздравляем с первой доставкой!\n\n'
            'Тебе начислен реферальный бонус: скидка 10% на следующий заказ 🎁\n\n'
            'Напомни менеджеру при оформлении следующей посылки.'
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
        'btn_referral': '👥 Invite a Friend',
        'referral_info': (
            '👥 Invite a friend — you both get a bonus!\n\n'
            '🎁 You get: 1 kg free shipping\n'
            '🎁 Friend gets: 10% off first order\n\n'
            '⚠️ Bonus is credited only after your friend\'s first parcel is delivered — '
            'fair and transparent.\n\n'
            '🔗 Your personal link:\n{link}\n\n'
            '📊 Stats:\n'
            '• Friends invited: {invited}\n'
            '• Bonuses earned: {bonuses} kg'
        ),
        'notify_referral_bonus_referrer': (
            '🎉 Your friend received their parcel!\n\n'
            'Your bonus: +1 kg free shipping 🎁\n\n'
            'The bonus will be applied to your next order. '
            'Remind the manager when placing your next shipment.'
        ),
        'notify_referral_bonus_referred': (
            '🎉 Congratulations on your first delivery!\n\n'
            'Your referral bonus: 10% off your next order 🎁\n\n'
            'Remind the manager when placing your next shipment.'
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
    },

    # ────────────────────────────────────────────────────────────
    # КЫРГЫЗЧА (ky)
    # ────────────────────────────────────────────────────────────
    'ky': {
        # General
        'choose_language': '🌐 Тилди тандаңыз / Choose language:\n\n🇷🇺 Русский · 🇬🇧 English · 🇰🇬 Кыргызча · 🇰🇿 Қазақша · 🇺🇿 O\'zbek',
        'welcome': 'OWAY Cargo\'го кош келиңиз! 🚚\nРолуңузду тандаңыз:',
        'choose_role': 'Ролуңузду тандаңыз:',
        'btn_client': '📦 Кардар',
        'btn_partner': '🏪 Өнөктөш (кабыл алуу пункту)',
        'btn_driver': '🚗 Айдоочу',
        'btn_admin': '⚙️ Администратор',
        'back': '⬅️ Артка',
        'cancel': '❌ Жокко чыгаруу',
        'main_menu': '🏠 Башкы меню',
        'invalid_input': 'Туура эмес киргизүү. Кайра аракет кылыңыз.',

        # Client registration
        'client_enter_name': 'Атыңызды жазыңыз:',
        'client_enter_phone': 'Телефон номериңизди бөлүшүү үчүн төмөнкү баскычты басыңыз:',
        'btn_share_phone': '📱 Номеримди жөнөтүү',
        'phone_not_yours': '❌ Бул сиздин номериңиз эмес. Өз номериңизди бөлүшүү үчүн баскычты басыңыз.',
        'client_registered': '✅ Каттоо аяктады! Кош келиңиз, {name}!',
        'client_already_registered': '✅ Сиз мурунтан каттоодон өткөнсүз. Кош келиңиз, {name}!',

        # Client type selection
        'client_type_select': (
            '👋 OWAY Cargo\'го кош келиңиз!\n\n'
            'Эмне кылгыңыз келет?\n\n'
            '🛒 АКШдан заказ кылуу — АКШдан товар сатып алып, өлкөңүзгө алуу\n\n'
            '📦 АКШдан жөнөтүү — сиз АКШда жашайсыз жана жөнөтмө жиберкиңиз келет'
        ),
        'btn_order_type': '🛒 АКШдан заказ кылуу',
        'btn_send_type': '📦 АКШдан жөнөтүү',

        # Order menu
        'order_menu': '🛒 АКШдан заказ кылуу\nТелефонуңуз: {phone}',
        'btn_my_address': '🏠 АКШдагы дарегим',
        'btn_shopping': '🛍️ Шопинг-жардамчы',
        'btn_faq': '❓ Көп берилүүчү суроолор',
        'btn_miniapp': '🌐 Колдонмону ачуу',

        # Send menu
        'send_menu': '📦 АКШдан жөнөтүү\nТелефонуңуз: {phone}',
        'btn_find_dropoff': '📍 Кабыл алуу пункттары',

        # Shared buttons
        'btn_track': '🔍 Жөнөтмөнү издөө',
        'btn_history': '📋 Жөнөтмөлөр тарыхы',
        'btn_calculator': '💰 Баа калькулятору',
        'btn_support': '💬 Колдоо',
        'btn_change_lang': '🌐 Тилди өзгөртүү',
        'btn_referral': '👥 Досту чакыруу',
        'btn_recalculate': '🔄 Кайра эсептөө',
        'btn_contact_manager': '📞 Менеджерге байланышуу',

        # Legacy
        'client_menu': '📦 Кардар менюсу\nТелефонуңуз: {phone}',

        # Tracking
        'enter_tracking': 'Трек-номерди жазыңыз:',
        'parcel_not_found': '❌ {tracking} трек-номери менен жөнөтмө табылган жок.',
        'parcel_info': (
            '📦 Жөнөтмө: {tracking}\n'
            '🌍 Өлкө: {country}\n'
            '📍 Статус: {status}\n'
            '🏪 Кабыл алуу пункту: {partner}\n'
            '⚖️ Салмагы: {weight} кг\n'
            '📏 Өлчөмдөрү: {dims}\n'
            '💰 Баасы: ${price}\n'
            '📅 Кабыл алынган: {date}'
        ),
        'parcel_photo': '🖼️ Жөнөтмөнүн сүрөтү:',
        'no_photo': 'Сүрөт жок.',
        'no_parcels': 'Сизде жөнөтмө жок.',
        'parcel_history': '📋 Жөнөтмөлөрүңүз:',

        # Calculator
        'calc_enter_weight': (
            '⚖️ Жөнөтмөнүн салмагын жазыңыз:\n\n'
            'Мисалдар: 15.3, 15,3, 15.3 кг, 26 lb\n'
            '(кг же фунт — автоматтык түрдө которулат)'
        ),
        'calc_weight_accepted': '✅ Кабыл алынды: {input} = {kg} кг',
        'calc_weight_help': (
            'Салмакты төмөнкү форматтардын биринде жазыңыз:\n'
            '• 15.3\n• 15,3\n• 15 кг\n• 26 lb'
        ),
        'calc_enter_dims': (
            '📐 Өлчөмдөрдү бир сапка жазыңыз (У×Т×Б):\n\n'
            'Мисалдар:\n'
            '• 40x30x20\n'
            '• 40x30x20 cm\n'
            '• 16x12x10 in'
        ),
        'calc_dims_accepted': '✅ Кабыл алынды: {input} = {l}×{w}×{h} см',
        'calc_dims_help': (
            'Өлчөмдөрдү бир сапка жазыңыз:\n'
            '40x30x20 см  же  16x12x10 in\n\n'
            'Бөлгүчтөр: x, ×, *, боштук'
        ),
        'calc_dims_error': (
            '❓ Өлчөмдөрдү окуй алган жокмун.\n\n'
            'Форматта жазыңыз: 40x30x20 же 16x12x10 in'
        ),
        'calc_weight_error': (
            '❓ Салмакты окуй алган жокмун.\n\n'
            'Форматта жазыңыз: 15.3 кг же 26 lb'
        ),
        'calc_choose_country': '🌍 Жеткирүү өлкөсүн тандаңыз:',
        'calc_result': (
            '💰 Баа эсеби:\n\n'
            '🌍 Өлкө: {country}\n'
            '💲 Тариф: ${rate}/кг\n'
            '⚖️ Чыныгы салмак: {actual} кг\n'
            '📦 Көлөмдүк салмак: {vol} кг\n'
            '✅ Эсептик салмак: {chargeable} кг\n'
            '💵 Жалпы: ${price}'
        ),

        # Support
        'support_message': (
            '💬 OWAY Cargo колдоо кызматы\n\n'
            '🌍 КМШ кардарлары:\n'
            'WhatsApp: +996 709 969621\n'
            '📲 t.me/+996709969621\n\n'
            '🇺🇸 АКШ кардарлары:\n'
            'WhatsApp: +1 213 276 6898\n'
            '📲 t.me/+12132766898'
        ),

        # Statuses — DIRECT
        'status_accepted': '✅ АКШда кабыл алынды',
        'status_in_transit': '✈️ Жолдо',
        'status_arrived': '📍 Жеткирүү өлкөсүнө келди',
        'status_customs': '🛃 Бажы текшерүүсүндө',
        'status_ready': '📦 Алууга даяр',
        'status_delivered': '🏠 Жеткирилди',

        # Statuses — TRANSIT
        'status_transit_zone': '🔄 Транзит зонада',
        'status_arrived_moscow': '📍 Москвага келди',
        'status_with_driver': '🚚 Жеткирүүгө берилди (СДЭК)',

        # Countries
        'accept_choose_country': '🌍 Жеткирүү өлкөсүн тандаңыз:',
        'country_KG': '🇰🇬 Кыргызстан',
        'country_KZ': '🇰🇿 Казакстан',
        'country_UZ': '🇺🇿 Өзбекстан',
        'country_RU': '🇷🇺 Россия',
        'country_BY': '🇧🇾 Беларусь',

        # Timeline
        'parcel_timeline': '🕐 Статус тарыхы:',
        'timeline_line': '{icon} {status} — {date}',

        # Admin status update
        'btn_update_status': '🔄 Жөнөтмө статусун жаңыртуу',
        'admin_enter_tracking': 'Жөнөтмөнүн трек-номерин жазыңыз:',
        'admin_parcel_not_found': '❌ {tracking} жөнөтмөсү табылган жок.',
        'admin_choose_status': (
            'Жөнөтмө: {tracking}\n'
            'Учурдагы статус: {status}\n\n'
            'Жаңы статусту тандаңыз:'
        ),
        'admin_status_updated': '✅ {tracking} жөнөтмөсүнүн статусу жаңыртылды:\n{status}',
        'notify_status_changed': (
            '📬 Жөнөтмөңүз боюнча жаңылоо!\n\n'
            '🔢 Трек-номер: {tracking}\n'
            '📦 Жаңы статус: {status}\n\n'
            'Жөнөтмөнү көзөмөлдөңүз: /start'
        ),
        'btn_referral': '👥 Досту чакыруу',
        'referral_info': (
            '👥 Досуңузду чакырыңыз — экөөңүз тең бонус алыңыз!\n\n'
            '🎁 Сизге: 1 кг акысыз жеткирүү\n'
            '🎁 Досуңузга: биринчи заказга 10% арзандатуу\n\n'
            '⚠️ Бонус досуңуздун биринчи жөнөтмөсү жеткирилгенден кийин гана берилет.\n\n'
            '🔗 Жеке шилтемеңиз:\n{link}\n\n'
            '📊 Статистика:\n'
            '• Чакырылган достор: {invited}\n'
            '• Алынган бонустар: {bonuses} кг'
        ),
        'notify_referral_bonus_referrer': (
            '🎉 Досуңуз жөнөтмөсүн алды!\n\n'
            'Сиздин бонус: +1 кг акысыз жеткирүү 🎁\n\n'
            'Бонус кийинки заказыңызда колдонулат. '
            'Заказ берүүдө менеджерге эскертиңиз.'
        ),
        'notify_referral_bonus_referred': (
            '🎉 Биринчи жеткирүүңүз менен куттуктайбыз!\n\n'
            'Реферал бонусуңуз: кийинки заказга 10% арзандатуу 🎁\n\n'
            'Кийинки жөнөтмө заказ берүүдө менеджерге эскертиңиз.'
        ),
        'notify_shopping_new': (
            '🛍 Жаңы сатып алуу заявкасы!\n\n'
            '👤 Кардар: {name}\n'
            '📞 Телефон: {phone}\n'
            '📝 Суроо-талап:\n{request}'
        ),

        # US Address
        'address_enter_id': (
            '🔑 owaycargo.com сайтынан IDңизди жазыңыз\n\n'
            'Эгер сайтта каттоодон өтө элек болсоңуз — owaycargo.com сайтына кирип, аккаунт түзүңүз.\n'
            'Каттоодон кийин IDңиз жеке кабинетте жеткиликтүү болот.'
        ),
        'address_not_found': (
            '❌ {website_id} ID системада табылган жок.\n\n'
            'IDни туура жазганыңызды текшериңиз же колдоо кызматына кайрылыңыз:\n'
            'WhatsApp: +996 709 969621'
        ),
        'your_us_address': (
            '🏠 АКШдагы жөнөтмө алуу дарегиңиз:\n\n'
            '{address}\n\n'
            '📝 Америка интернет-дүкөндөрүнөн заказ берүүдө бул даректи көрсөтүңүз.\n'
            '📦 Кампабызга жеткенден кийин жөнөтмөңүздү КМШдагы дарегиңизге жөнөтөбүз.'
        ),
        'address_already_set': (
            '✅ Аккаунтуңуз сайтка байланышкан.\n\n'
            '🏠 АКШдагы дарегиңиз:\n\n{address}'
        ),

        # Shopping assistant
        'shopping_intro': (
            '🛍️ OWAY Cargo Шопинг-жардамчы\n\n'
            'АКШдан каалаган товарды сиз үчүн сатып алабыз!\n\n'
            'Билдирүүңүздө көрсөтүңүз:\n'
            '• Товарга шилтеме же дүкөндүн аталышы\n'
            '• Товар сүрөттөмөсү (түсү, өлчөмү, модели)\n'
            '• Каалаган бюджет ($)\n\n'
            '💰 Кызмат акысы: товар наркынын 10%\n'
            '⏱ Менеджер жообу: 24 сааттын ичинде'
        ),
        'shopping_enter_request': '✍️ Суроо-талабыңызды толук жазыңыз:',
        'shopping_received': (
            '✅ Суроо-талабыңыз кабыл алынды!\n\n'
            'Менеджерибиз жакын арада {phone} номериңиз менен байланышат.\n\n'
            'OWAY Cargo\'ну тандаганыңыз үчүн рахмат! 🚚'
        ),
        'btn_my_requests': '🛍 Менин заявкаларым',
        'my_requests_empty': 'Сатып алуу заявкаларыңыз жок.',
        'my_requests_header': '🛍 Заявкаларыңыз:\n',
        'request_status_new': '🟡 Жаңы',
        'request_status_in_progress': '🔵 Иштелүүдө',
        'request_status_done': '✅ Аткарылды',
        'request_status_cancelled': '❌ Жокко чыгарылды',
        'my_request_line': '#{id} {status}\n📝 {text}\n📅 {date}\n',
        'notify_request_updated': (
            '🛍 Заявкаңыз #{id} боюнча жаңылоо:\n\n'
            '📝 {text}\n'
            '📦 Жаңы статус: {status}'
        ),
        'shopping_notify_admin': (
            '🛍️ Жаңы шопинг-жардамчы суроо-талабы!\n\n'
            '👤 Кардар: {name}\n'
            '📱 Телефон: {phone}\n'
            '📝 Суроо-талап:\n{request}'
        ),

        # FAQ ORDER
        'faq_order': (
            '❓ Көп берилүүчү суроолор — АКШдан заказ кылуу\n\n'
            '1️⃣ АКШдагы дарекни кантип алам?\n'
            'owaycargo.com сайтында катталыңыз → жеке ID алыңыз → '
            'ботто «АКШдагы дарегим» аркылуу жазыңыз. Кампанын дареги көрсөтүлөт.\n\n'
            '2️⃣ Жөнөтмөнү кантип көзөмөлдөйм?\n'
            '«Жөнөтмөнү издөө» баскычын басыңыз, трек-номерди жазыңыз. '
            'Трек-номер жөнөтмө кабыл алынганда берилет.\n\n'
            '3️⃣ Жеткирүү канча турат?\n'
            '🇰🇬 Кыргызстан, 🇰🇿 Казакстан, 🇺🇿 Өзбекстан: $12/кг\n'
            '🇷🇺 Россия, 🇧🇾 Беларусь: $18/кг\n'
            'Көлөмдүк же чыныгы салмак боюнча эсептелет (чоңу).\n\n'
            '4️⃣ Жеткирүү канча убакытта?\n'
            '🇰🇬 Кыргызстан: 7–9 жумуш күнү.\n'
            '🇰🇿 Казакстан / 🇺🇿 Өзбекстан: 10–14 жумуш күнү.\n'
            '🇷🇺 Россия / 🇧🇾 Беларусь: 15–21 жумуш күнү.\n\n'
            '5️⃣ Шопинг-жардамчы деген эмне?\n'
            'Менеджерибиз АКШдан каалаган товарды сиз үчүн сатып алат. '
            'Комиссия — товар баасынын 10%. '
            '«Шопинг-жардамчы» аркылуу жазыңыз.\n\n'
            '6️⃣ Кайсы товарлар тыюу салынган?\n'
            'Тыюу салынган: курал-жарак, баңги заттар, коркунучтуу заттар, '
            'бузулуучу азык-түлүк, жаныбарлар.\n\n'
            '7️⃣ Колдоо байланыштары:\n'
            '🌍 КМШ: WhatsApp +996 709 969621\n'
            '🇺🇸 АКШ: WhatsApp +1 213 276 6898'
        ),

        # FAQ SEND
        'faq_send': (
            '❓ Көп берилүүчү суроолор — АКШдан жөнөтүү\n\n'
            '1️⃣ Жөнөтмөнү кайда тапшырам?\n'
            'Менюдагы «Кабыл алуу пункттары» аркылуу жакынкы пунктту табыңыз. '
            'Кызматкер жөнөтмөнү кабыл алат, таразалайт жана трек-номер берет.\n\n'
            '2️⃣ Жеткирүү канча турат?\n'
            '🇰🇬 Кыргызстан, 🇰🇿 Казакстан, 🇺🇿 Өзбекстан: $12/кг\n'
            '🇷🇺 Россия, 🇧🇾 Беларусь: $18/кг\n'
            'Так эсеп үчүн «Калькулятор» колдонуңуз.\n\n'
            '3️⃣ Кандай документтер керек?\n'
            'Алуучунун телефон номери гана. '
            'Кымбат товарлар үчүн чек/инвойс талап кылынышы мүмкүн.\n\n'
            '4️⃣ Жөнөтмөнү кантип таңгалайм?\n'
            'Ишенимдүү таңгалаңыз: куту, скотч, морт нерселер үчүн пузырчатый плёнка. '
            'Кийим-кечелерди пакетке салууга болот.\n\n'
            '5️⃣ Кайсы товарларды жөнөтүүгө болбойт?\n'
            'Тыюу салынган: курал-жарак, ок-дарылар, 100 мл ашык суюктуктар, '
            'аэрозолдор, коркунучтуу химикаттар.\n\n'
            '6️⃣ Алуучу жөнөтмөнү кантип көзөмөлдөйт?\n'
            'Алуучу ушул ботто катталат жана трек-номерди жазат. '
            'Ар бир статус өзгөргөндө билдирүү келет.\n\n'
            '7️⃣ Колдоо байланыштары:\n'
            '🇺🇸 АКШ: WhatsApp +1 213 276 6898\n'
            '🌍 КМШ: WhatsApp +996 709 969621'
        ),

        # Drop-off
        'dropoffs_list': '📍 АКШдагы жөнөтмө кабыл алуу пункттары:',
        'dropoff_line': '• {name} — {location}',
        'no_dropoffs': 'АКШдагы кабыл алуу пункттары кошула элек.\nБизге байланышыңыз: +1 213 276 6898',

        # Partner
        'partner_enter_code': 'Өнөктөш кодун жазыңыз:',
        'partner_invalid_code': '❌ Туура эмес өнөктөш коду.',
        'partner_welcome': '🏪 Кош келиңиз, {name}!\nПункт: {location}',
        'partner_menu': '🏪 Өнөктөш менюсу\n📍 {name} — {location}',
        'btn_accept_parcel': '📥 Жөнөтмө кабыл алуу',
        'btn_my_parcels': '📋 Менин жөнөтмөлөрүм',
        'btn_handoff': '🚚 Айдоочуга берүү',
        'btn_stats': '📊 Статистика',

        # Accept parcel
        'accept_send_photo': '📸 Жөнөтмөнүн сүрөтүн тартыңыз:',
        'accept_enter_weight': 'Жөнөтмөнүн салмагын жазыңыз (кг):',
        'accept_enter_length': 'Узундугун жазыңыз (см):',
        'accept_enter_width': 'Туурасын жазыңыз (см):',
        'accept_enter_height': 'Бийиктигин жазыңыз (см):',
        'accept_enter_client_phone': '📱 Кардардын телефон номерин жазыңыз:',
        'accept_confirm': (
            '✅ Жөнөтмө кабыл алууну ырастаңыз:\n\n'
            '📱 Кардар: {phone}\n'
            '🌍 Өлкө: {country}\n'
            '⚖️ Салмагы: {weight} кг\n'
            '📏 Өлчөмдөрү: {l}×{w}×{h} см\n'
            '📦 Көлөмдүк салмак: {vol} кг\n'
            '✅ Эсептик салмак: {chargeable} кг\n'
            '💰 Баасы: ${price}'
        ),
        'btn_confirm': '✅ Ырастоо',
        'parcel_accepted': '✅ Жөнөтмө кабыл алынды!\nТрек-номер: {tracking}',
        'invalid_number': '❌ Туура сан жазыңыз.',

        'no_parcels_at_point': 'Пунктуңузда жөнөтмө жок.',
        'parcels_at_point': '📋 Пунктуңуздагы жөнөтмөлөр:',
        'parcel_line': '• {tracking} | {weight}кг | ${price} | {status}',

        'no_parcels_to_handoff': '❌ Айдоочуга берүүгө жөнөтмө жок.',
        'handoff_confirm': '🚚 {count} жөнөтмөнү айдоочуга берүүнү каалайсызбы?',
        'handoff_done': '✅ {count} жөнөтмө айдоочуга берилди!',
        'handoff_notify': '🚚 Сиздин жөнөтмө {tracking} айдоочуга берилди жана жолдо!',

        'partner_stats': (
            '📊 7 күндүк статистика\n\n'
            '📦 Кабыл алынган жөнөтмөлөр: {count}\n'
            '⚖️ Жалпы салмак: {weight} кг\n'
            '💰 Жалпы кирше: ${revenue}\n'
            '🎁 Сыйлыгыңыз (10%): ${reward}'
        ),

        # Admin
        'admin_enter_code': 'Администратор кодун жазыңыз:',
        'admin_invalid_code': '❌ Туура эмес администратор коду.',
        'admin_welcome': '⚙️ OWAY Cargo администратор панели',
        'admin_menu': '⚙️ Администратор панели',
        'btn_network_stats': '📊 Тармак статистикасы',
        'btn_list_partners': '🏪 Өнөктөштөр тизмеси',
        'btn_add_partner': '➕ Өнөктөш кошуу',
        'btn_broadcast': '📢 Кардарларга жөнөтүү',
        'btn_set_address': '🏠 Кампа дарегин өзгөртүү',
        'btn_add_website_user': '👤 Сайт колдонуучу ID кошуу',
        'btn_view_requests': '🛍️ Шопинг заявкалары',
        'btn_update_request': '✏️ Заявка статусун жаңыртуу',
        'admin_update_request_enter_id': 'Заявка номерин жазыңыз (мисалы: 3):',
        'admin_request_not_found': '❌ #{id} заявкасы табылган жок.',
        'admin_request_found': (
            '📋 Заявка #{id}\n'
            '👤 {client} | {phone}\n'
            '📝 {text}\n'
            '📅 {date}\n'
            '📦 Статус: {status}\n\n'
            'Жаңы статусту тандаңыз:'
        ),
        'admin_request_updated': '✅ #{id} заявкасы жаңыртылды: {status}',

        'network_stats': (
            '📊 Тармак статистикасы (акыркы 7 күн)\n\n'
            '📦 Жалпы жөнөтмөлөр: {total}\n'
            '🚚 Жолдо: {in_transit}\n'
            '✅ Жеткирилди: {delivered}\n'
            '⚖️ Жалпы салмак: {weight} кг\n'
            '💰 Жалпы кирше: ${revenue}\n'
            '🏪 Активдүү пункттар: {partners}'
        ),

        'partners_list': '🏪 Өнөктөштөр тизмеси:',
        'partner_line': '• {name} | {location} | Код: {code} | Жөнөтмөлөр: {count}',
        'no_partners': 'Өнөктөштөр табылган жок.',

        'add_partner_name': 'Пункттун аталышын жазыңыз:',
        'add_partner_location': 'Пункттун дарегин жазыңыз:',
        'add_partner_code': 'Өнөктөш кодун жазыңыз (уникалдуу):',
        'partner_code_exists': '❌ Мындай код бар.',
        'partner_added': '✅ Өнөктөш кошулду!\nАталышы: {name}\nДареги: {location}\nКод: {code}',

        'broadcast_enter_msg': (
            '📢 Жөнөтүү текстин жазыңыз:\n\n'
            'Билдирүү бардык катталган кардарларга жөнөтүлөт.'
        ),
        'broadcast_sent': '✅ Жөнөтүү аткарылды!\nЖөнөтүлдү: {sent} | Ката: {failed}',

        'set_address_enter': (
            '🏠 АКШдагы кампанын жаңы дарегин жазыңыз:\n\n'
            'Учурдагы дарек:\n{current}'
        ),
        'address_updated': '✅ Кампа дареги жаңыртылды!',

        'add_wu_id_enter': '👤 owaycargo.com сайтынан колдонуучу IDсин жазыңыз:',
        'add_wu_name_enter': 'Колдонуучунун атын жазыңыз (ID: {website_id}):',
        'wu_added': '✅ Колдонуучу кошулду!\nID: {website_id}\nАты: {name}',
        'wu_id_taken': '❌ Бул ID менен колдонуучу бар.',

        'view_requests_empty': '🛍️ Жаңы шопинг заявкалары жок.',
        'view_requests_header': '🛍️ Жаңы шопинг заявкалары:\n',
        'request_line': '#{id} | {client} | {phone}\n📝 {text}\n📅 {date}\n',

        'notify_accepted': (
            '📦 Жөнөтмөңүз OWAY пунктунда кабыл алынды!\n\n'
            '🔢 Трек-номер: {tracking}\n'
            '📍 Кабыл алуу пункту: {partner}\n'
            '⚖️ Эсептик салмак: {weight} кг\n'
            '💰 Жеткирүү баасы: ${price}\n'
            '🕐 Болжолдуу мөөнөт: {delivery_days}\n\n'
            'Жөнөтмөнү көзөмөлдөңүз: /start → Жөнөтмөнү издөө'
        ),
        'delivery_days_kg': '7–9 жумуш күнү',
        'delivery_days_kz': '10–14 жумуш күнү',
        'delivery_days_uz': '10–14 жумуш күнү',
        'delivery_days_ru': '15–21 жумуш күнү',
        'delivery_days_by': '15–21 жумуш күнү',

        # Driver
        'driver_enter_code': 'Айдоочу кодун жазыңыз:',
        'driver_invalid_code': '❌ Туура эмес айдоочу коду.',
        'driver_welcome': '🚗 Кош келиңиз, {name}!',
        'driver_menu': '🚗 Айдоочу менюсу',
        'btn_my_deliveries': '📋 Менин жеткирүүлөрүм',
        'btn_mark_delivered': '✅ Жеткирилди деп белгилөө',
        'no_deliveries': 'Жеткирүүгө жөнөтмө жок.',
        'deliveries_list': '📋 Жеткирүү үчүн жөнөтмөлөр:',
        'driver_enter_tracking': 'Жеткирилген жөнөтмөнүн трек-номерин жазыңыз:',
        'driver_delivered_ok': '✅ {tracking} жөнөтмөсү жеткирилди деп белгиленди!',
        'driver_parcel_not_found': '❌ {tracking} жөнөтмөсү табылган жок же жеткирилген.',
        'notify_delivered': '🏠 Сиздин {tracking} жөнөтмөңүз жеткирилди! OWAY Cargo\'ну тандаганыңыз үчүн рахмат.',
    },

    # ────────────────────────────────────────────────────────────
    # ҚАЗАҚША (kk)
    # ────────────────────────────────────────────────────────────
    'kk': {
        # General
        'choose_language': '🌐 Тілді таңдаңыз / Choose language:\n\n🇷🇺 Русский · 🇬🇧 English · 🇰🇬 Кыргызча · 🇰🇿 Қазақша · 🇺🇿 O\'zbek',
        'welcome': 'OWAY Cargo-ға қош келдіңіз! 🚚\nРөліңізді таңдаңыз:',
        'choose_role': 'Рөліңізді таңдаңыз:',
        'btn_client': '📦 Клиент',
        'btn_partner': '🏪 Серіктес (қабылдау пункті)',
        'btn_driver': '🚗 Жүргізуші',
        'btn_admin': '⚙️ Әкімші',
        'back': '⬅️ Артқа',
        'cancel': '❌ Бас тарту',
        'main_menu': '🏠 Басты мәзір',
        'invalid_input': 'Қате енгізу. Қайталап көріңіз.',

        # Client registration
        'client_enter_name': 'Атыңызды жазыңыз:',
        'client_enter_phone': 'Телефон нөміріңізді бөлісу үшін төмендегі батырманы басыңыз:',
        'btn_share_phone': '📱 Нөмірімді жіберу',
        'phone_not_yours': '❌ Бұл сіздің нөміріңіз емес. Өз нөміріңізді бөлісу үшін батырманы басыңыз.',
        'client_registered': '✅ Тіркелу аяқталды! Қош келдіңіз, {name}!',
        'client_already_registered': '✅ Сіз бұрыннан тіркелгенсіз. Қош келдіңіз, {name}!',

        # Client type selection
        'client_type_select': (
            '👋 OWAY Cargo-ға қош келдіңіз!\n\n'
            'Не істегіңіз келеді?\n\n'
            '🛒 АҚШ-тан тапсырыс беру — АҚШ-тан тауар сатып алып, еліңізге алу\n\n'
            '📦 АҚШ-тан жіберу — сіз АҚШ-та тұрасыз және жөнелтім жібергіңіз келеді'
        ),
        'btn_order_type': '🛒 АҚШ-тан тапсырыс беру',
        'btn_send_type': '📦 АҚШ-тан жіберу',

        # Order menu
        'order_menu': '🛒 АҚШ-тан тапсырыс беру\nТелефоныңыз: {phone}',
        'btn_my_address': '🏠 АҚШ-тағы мекенжайым',
        'btn_shopping': '🛍️ Шопинг-көмекші',
        'btn_faq': '❓ Жиі қойылатын сұрақтар',
        'btn_miniapp': '🌐 Қосымшаны ашу',

        # Send menu
        'send_menu': '📦 АҚШ-тан жіберу\nТелефоныңыз: {phone}',
        'btn_find_dropoff': '📍 Қабылдау пункттері',

        # Shared buttons
        'btn_track': '🔍 Жөнелтімді іздеу',
        'btn_history': '📋 Жөнелтімдер тарихы',
        'btn_calculator': '💰 Баға калькуляторы',
        'btn_support': '💬 Қолдау',
        'btn_change_lang': '🌐 Тілді өзгерту',
        'btn_referral': '👥 Досты шақыру',
        'btn_recalculate': '🔄 Қайта есептеу',
        'btn_contact_manager': '📞 Менеджерге хабарласу',

        # Legacy
        'client_menu': '📦 Клиент мәзірі\nТелефоныңыз: {phone}',

        # Tracking
        'enter_tracking': 'Трек-нөмірді жазыңыз:',
        'parcel_not_found': '❌ {tracking} трек-нөмірімен жөнелтім табылмады.',
        'parcel_info': (
            '📦 Жөнелтім: {tracking}\n'
            '🌍 Ел: {country}\n'
            '📍 Мәртебе: {status}\n'
            '🏪 Қабылдау пункті: {partner}\n'
            '⚖️ Салмағы: {weight} кг\n'
            '📏 Өлшемдері: {dims}\n'
            '💰 Бағасы: ${price}\n'
            '📅 Қабылданған: {date}'
        ),
        'parcel_photo': '🖼️ Жөнелтім суреті:',
        'no_photo': 'Сурет жоқ.',
        'no_parcels': 'Сізде жөнелтім жоқ.',
        'parcel_history': '📋 Жөнелтімдеріңіз:',

        # Calculator
        'calc_enter_weight': (
            '⚖️ Жөнелтімнің салмағын жазыңыз:\n\n'
            'Мысалдар: 15.3, 15,3, 15.3 кг, 26 lb\n'
            '(кг немесе фунт — автоматты түрде аударылады)'
        ),
        'calc_weight_accepted': '✅ Қабылданды: {input} = {kg} кг',
        'calc_weight_help': (
            'Салмақты келесі форматтардың бірінде жазыңыз:\n'
            '• 15.3\n• 15,3\n• 15 кг\n• 26 lb'
        ),
        'calc_enter_dims': (
            '📐 Өлшемдерді бір жолға жазыңыз (Ұ×Е×Б):\n\n'
            'Мысалдар:\n'
            '• 40x30x20\n'
            '• 40x30x20 cm\n'
            '• 16x12x10 in'
        ),
        'calc_dims_accepted': '✅ Қабылданды: {input} = {l}×{w}×{h} см',
        'calc_dims_help': (
            'Өлшемдерді бір жолға жазыңыз:\n'
            '40x30x20 см  немесе  16x12x10 in\n\n'
            'Бөлгіштер: x, ×, *, бос орын'
        ),
        'calc_dims_error': (
            '❓ Өлшемдерді оқи алмадым.\n\n'
            'Форматта жазыңыз: 40x30x20 немесе 16x12x10 in'
        ),
        'calc_weight_error': (
            '❓ Салмақты оқи алмадым.\n\n'
            'Форматта жазыңыз: 15.3 кг немесе 26 lb'
        ),
        'calc_choose_country': '🌍 Жеткізу елін таңдаңыз:',
        'calc_result': (
            '💰 Баға есебі:\n\n'
            '🌍 Ел: {country}\n'
            '💲 Тариф: ${rate}/кг\n'
            '⚖️ Нақты салмақ: {actual} кг\n'
            '📦 Көлемдік салмақ: {vol} кг\n'
            '✅ Есептік салмақ: {chargeable} кг\n'
            '💵 Барлығы: ${price}'
        ),

        # Support
        'support_message': (
            '💬 OWAY Cargo қолдау қызметі\n\n'
            '🌍 ТМД клиенттері:\n'
            'WhatsApp: +996 709 969621\n'
            '📲 t.me/+996709969621\n\n'
            '🇺🇸 АҚШ клиенттері:\n'
            'WhatsApp: +1 213 276 6898\n'
            '📲 t.me/+12132766898'
        ),

        # Statuses — DIRECT
        'status_accepted': '✅ АҚШ-та қабылданды',
        'status_in_transit': '✈️ Жолда',
        'status_arrived': '📍 Жеткізу еліне келді',
        'status_customs': '🛃 Кеден тексеруінде',
        'status_ready': '📦 Алуға дайын',
        'status_delivered': '🏠 Жеткізілді',

        # Statuses — TRANSIT
        'status_transit_zone': '🔄 Транзит аймағында',
        'status_arrived_moscow': '📍 Мәскеуге келді',
        'status_with_driver': '🚚 Жеткізуге берілді (СДЭК)',

        # Countries
        'accept_choose_country': '🌍 Жеткізу елін таңдаңыз:',
        'country_KG': '🇰🇬 Қырғызстан',
        'country_KZ': '🇰🇿 Қазақстан',
        'country_UZ': '🇺🇿 Өзбекстан',
        'country_RU': '🇷🇺 Ресей',
        'country_BY': '🇧🇾 Беларусь',

        # Timeline
        'parcel_timeline': '🕐 Мәртебе тарихы:',
        'timeline_line': '{icon} {status} — {date}',

        # Admin status update
        'btn_update_status': '🔄 Жөнелтім мәртебесін жаңарту',
        'admin_enter_tracking': 'Жөнелтімнің трек-нөмірін жазыңыз:',
        'admin_parcel_not_found': '❌ {tracking} жөнелтімі табылмады.',
        'admin_choose_status': (
            'Жөнелтім: {tracking}\n'
            'Ағымдағы мәртебе: {status}\n\n'
            'Жаңа мәртебені таңдаңыз:'
        ),
        'admin_status_updated': '✅ {tracking} жөнелтімінің мәртебесі жаңартылды:\n{status}',
        'notify_status_changed': (
            '📬 Жөнелтіміңіз бойынша жаңарту!\n\n'
            '🔢 Трек-нөмір: {tracking}\n'
            '📦 Жаңа мәртебе: {status}\n\n'
            'Жөнелтімді бақылаңыз: /start'
        ),
        'btn_referral': '👥 Досты шақыру',
        'referral_info': (
            '👥 Досыңызды шақырыңыз — екеуіңіз де бонус алыңыз!\n\n'
            '🎁 Сізге: 1 кг тегін жеткізу\n'
            '🎁 Досыңызға: бірінші тапсырысқа 10% жеңілдік\n\n'
            '⚠️ Бонус досыңыздың бірінші жөнелтімі жеткізілгеннен кейін ғана беріледі.\n\n'
            '🔗 Жеке сілтемеңіз:\n{link}\n\n'
            '📊 Статистика:\n'
            '• Шақырылған достар: {invited}\n'
            '• Алынған бонустар: {bonuses} кг'
        ),
        'notify_referral_bonus_referrer': (
            '🎉 Досыңыз жөнелтімін алды!\n\n'
            'Сіздің бонус: +1 кг тегін жеткізу 🎁\n\n'
            'Бонус келесі тапсырысыңызда қолданылады. '
            'Тапсырыс беру кезінде менеджерге ескертіңіз.'
        ),
        'notify_referral_bonus_referred': (
            '🎉 Бірінші жеткізуіңізбен құттықтаймыз!\n\n'
            'Реферал бонусыңыз: келесі тапсырысқа 10% жеңілдік 🎁\n\n'
            'Келесі жөнелтім тапсырыс беру кезінде менеджерге ескертіңіз.'
        ),
        'notify_shopping_new': (
            '🛍 Жаңа сатып алу өтінімі!\n\n'
            '👤 Клиент: {name}\n'
            '📞 Телефон: {phone}\n'
            '📝 Сұраныс:\n{request}'
        ),

        # US Address
        'address_enter_id': (
            '🔑 owaycargo.com сайтынан ID-ңізді жазыңыз\n\n'
            'Егер сайтта тіркелмеген болсаңыз — owaycargo.com сайтына кіріп, аккаунт жасаңыз.\n'
            'Тіркелгеннен кейін ID-ңіз жеке кабинетте қолжетімді болады.'
        ),
        'address_not_found': (
            '❌ {website_id} ID жүйеде табылмады.\n\n'
            'ID-ді дұрыс жазғаныңызды тексеріңіз немесе қолдау қызметіне хабарласыңыз:\n'
            'WhatsApp: +996 709 969621'
        ),
        'your_us_address': (
            '🏠 АҚШ-тағы жөнелтім алу мекенжайыңыз:\n\n'
            '{address}\n\n'
            '📝 Америка интернет-дүкендерінен тапсырыс беру кезінде осы мекенжайды көрсетіңіз.\n'
            '📦 Қоймамызға жеткеннен кейін жөнелтіміңізді ТМД-дағы мекенжайыңызға жібереміз.'
        ),
        'address_already_set': (
            '✅ Аккаунтыңыз сайтқа байланысқан.\n\n'
            '🏠 АҚШ-тағы мекенжайыңыз:\n\n{address}'
        ),

        # Shopping assistant
        'shopping_intro': (
            '🛍️ OWAY Cargo Шопинг-көмекші\n\n'
            'АҚШ-тан кез келген тауарды сіз үшін сатып аламыз!\n\n'
            'Хабарламаңызда көрсетіңіз:\n'
            '• Тауарға сілтеме немесе дүкен атауы\n'
            '• Тауар сипаттамасы (түсі, өлшемі, моделі)\n'
            '• Қалаған бюджет ($)\n\n'
            '💰 Қызмет құны: тауар бағасының 10%\n'
            '⏱ Менеджер жауабы: 24 сағат ішінде'
        ),
        'shopping_enter_request': '✍️ Сұранысыңызды толық жазыңыз:',
        'shopping_received': (
            '✅ Сұранысыңыз қабылданды!\n\n'
            'Менеджеріміз жақын арада {phone} нөміріңіз арқылы хабарласады.\n\n'
            'OWAY Cargo-ны таңдағаныңыз үшін рахмет! 🚚'
        ),
        'btn_my_requests': '🛍 Менің өтінімдерім',
        'my_requests_empty': 'Сатып алу өтінімдеріңіз жоқ.',
        'my_requests_header': '🛍 Өтінімдеріңіз:\n',
        'request_status_new': '🟡 Жаңа',
        'request_status_in_progress': '🔵 Орындалуда',
        'request_status_done': '✅ Орындалды',
        'request_status_cancelled': '❌ Бас тартылды',
        'my_request_line': '#{id} {status}\n📝 {text}\n📅 {date}\n',
        'notify_request_updated': (
            '🛍 Өтініміңіз #{id} бойынша жаңарту:\n\n'
            '📝 {text}\n'
            '📦 Жаңа мәртебе: {status}'
        ),
        'shopping_notify_admin': (
            '🛍️ Жаңа шопинг-көмекші сұранысы!\n\n'
            '👤 Клиент: {name}\n'
            '📱 Телефон: {phone}\n'
            '📝 Сұраныс:\n{request}'
        ),

        # FAQ ORDER
        'faq_order': (
            '❓ Жиі қойылатын сұрақтар — АҚШ-тан тапсырыс беру\n\n'
            '1️⃣ АҚШ-тағы мекенжайды қалай аламын?\n'
            'owaycargo.com сайтында тіркеліңіз → жеке ID алыңыз → '
            'ботта «АҚШ-тағы мекенжайым» арқылы жазыңыз. Қойма мекенжайы көрсетіледі.\n\n'
            '2️⃣ Жөнелтімді қалай бақылаймын?\n'
            '«Жөнелтімді іздеу» батырмасын басыңыз, трек-нөмірді жазыңыз. '
            'Трек-нөмір жөнелтім қабылданғанда беріледі.\n\n'
            '3️⃣ Жеткізу қанша тұрады?\n'
            '🇰🇬 Қырғызстан, 🇰🇿 Қазақстан, 🇺🇿 Өзбекстан: $12/кг\n'
            '🇷🇺 Ресей, 🇧🇾 Беларусь: $18/кг\n'
            'Көлемдік немесе нақты салмақ бойынша есептеледі (үлкені).\n\n'
            '4️⃣ Жеткізу қанша уақыт алады?\n'
            '🇰🇬 Қырғызстан: 7–9 жұмыс күні.\n'
            '🇰🇿 Қазақстан / 🇺🇿 Өзбекстан: 10–14 жұмыс күні.\n'
            '🇷🇺 Ресей / 🇧🇾 Беларусь: 15–21 жұмыс күні.\n\n'
            '5️⃣ Шопинг-көмекші дегеніміз не?\n'
            'Менеджеріміз АҚШ-тан кез келген тауарды сіз үшін сатып алады. '
            'Комиссия — тауар бағасының 10%. '
            '«Шопинг-көмекші» арқылы жазыңыз.\n\n'
            '6️⃣ Қандай тауарларға тыйым салынған?\n'
            'Тыйым салынған: қару-жарақ, есірткі, қауіпті заттар, '
            'тез бұзылатын тамақ, жануарлар.\n\n'
            '7️⃣ Қолдау байланыстары:\n'
            '🌍 ТМД: WhatsApp +996 709 969621\n'
            '🇺🇸 АҚШ: WhatsApp +1 213 276 6898'
        ),

        # FAQ SEND
        'faq_send': (
            '❓ Жиі қойылатын сұрақтар — АҚШ-тан жіберу\n\n'
            '1️⃣ Жөнелтімді қайда тапсырамын?\n'
            'Мәзірдегі «Қабылдау пункттері» арқылы жақын пунктті табыңыз. '
            'Қызметкер жөнелтімді қабылдайды, өлшейді және трек-нөмір береді.\n\n'
            '2️⃣ Жеткізу қанша тұрады?\n'
            '🇰🇬 Қырғызстан, 🇰🇿 Қазақстан, 🇺🇿 Өзбекстан: $12/кг\n'
            '🇷🇺 Ресей, 🇧🇾 Беларусь: $18/кг\n'
            'Нақты есеп үшін «Калькулятор» қолданыңыз.\n\n'
            '3️⃣ Қандай құжаттар қажет?\n'
            'Тек алушының телефон нөмірі. '
            'Қымбат тауарлар үшін чек/инвойс қажет болуы мүмкін.\n\n'
            '4️⃣ Жөнелтімді қалай орайын?\n'
            'Сенімді түрде ораңыз: қорап, скотч, сынғыш заттар үшін қабыршық пленка. '
            'Киімдерді пакетке салуға болады.\n\n'
            '5️⃣ Қандай тауарларды жіберуге болмайды?\n'
            'Тыйым салынған: қару-жарақ, оқ-дәрі, 100 мл-ден артық сұйықтықтар, '
            'аэрозольдер, қауіпті химикаттар.\n\n'
            '6️⃣ Алушы жөнелтімді қалай бақылайды?\n'
            'Алушы осы ботта тіркеледі және трек-нөмірді жазады. '
            'Әр мәртебе өзгергенде хабарлама келеді.\n\n'
            '7️⃣ Қолдау байланыстары:\n'
            '🇺🇸 АҚШ: WhatsApp +1 213 276 6898\n'
            '🌍 ТМД: WhatsApp +996 709 969621'
        ),

        # Drop-off
        'dropoffs_list': '📍 АҚШ-тағы жөнелтім қабылдау пункттері:',
        'dropoff_line': '• {name} — {location}',
        'no_dropoffs': 'АҚШ-тағы қабылдау пункттері әлі қосылмаған.\nБізге хабарласыңыз: +1 213 276 6898',

        # Partner
        'partner_enter_code': 'Серіктес кодын жазыңыз:',
        'partner_invalid_code': '❌ Қате серіктес коды.',
        'partner_welcome': '🏪 Қош келдіңіз, {name}!\nПункт: {location}',
        'partner_menu': '🏪 Серіктес мәзірі\n📍 {name} — {location}',
        'btn_accept_parcel': '📥 Жөнелтім қабылдау',
        'btn_my_parcels': '📋 Менің жөнелтімдерім',
        'btn_handoff': '🚚 Жүргізушіге беру',
        'btn_stats': '📊 Статистика',

        # Accept parcel
        'accept_send_photo': '📸 Жөнелтімнің суретін түсіріңіз:',
        'accept_enter_weight': 'Жөнелтімнің салмағын жазыңыз (кг):',
        'accept_enter_length': 'Ұзындығын жазыңыз (см):',
        'accept_enter_width': 'Енін жазыңыз (см):',
        'accept_enter_height': 'Биіктігін жазыңыз (см):',
        'accept_enter_client_phone': '📱 Клиенттің телефон нөмірін жазыңыз:',
        'accept_confirm': (
            '✅ Жөнелтім қабылдауды растаңыз:\n\n'
            '📱 Клиент: {phone}\n'
            '🌍 Ел: {country}\n'
            '⚖️ Салмағы: {weight} кг\n'
            '📏 Өлшемдері: {l}×{w}×{h} см\n'
            '📦 Көлемдік салмақ: {vol} кг\n'
            '✅ Есептік салмақ: {chargeable} кг\n'
            '💰 Бағасы: ${price}'
        ),
        'btn_confirm': '✅ Растау',
        'parcel_accepted': '✅ Жөнелтім қабылданды!\nТрек-нөмір: {tracking}',
        'invalid_number': '❌ Дұрыс сан жазыңыз.',

        'no_parcels_at_point': 'Пунктіңізде жөнелтім жоқ.',
        'parcels_at_point': '📋 Пунктіңіздегі жөнелтімдер:',
        'parcel_line': '• {tracking} | {weight}кг | ${price} | {status}',

        'no_parcels_to_handoff': '❌ Жүргізушіге беруге жөнелтім жоқ.',
        'handoff_confirm': '🚚 {count} жөнелтімді жүргізушіге бергіңіз келе ме?',
        'handoff_done': '✅ {count} жөнелтім жүргізушіге берілді!',
        'handoff_notify': '🚚 Сіздің {tracking} жөнелтіміңіз жүргізушіге берілді және жолда!',

        'partner_stats': (
            '📊 7 күндік статистика\n\n'
            '📦 Қабылданған жөнелтімдер: {count}\n'
            '⚖️ Жалпы салмақ: {weight} кг\n'
            '💰 Жалпы табыс: ${revenue}\n'
            '🎁 Сыйақыңыз (10%): ${reward}'
        ),

        # Admin
        'admin_enter_code': 'Әкімші кодын жазыңыз:',
        'admin_invalid_code': '❌ Қате әкімші коды.',
        'admin_welcome': '⚙️ OWAY Cargo әкімші панелі',
        'admin_menu': '⚙️ Әкімші панелі',
        'btn_network_stats': '📊 Желі статистикасы',
        'btn_list_partners': '🏪 Серіктестер тізімі',
        'btn_add_partner': '➕ Серіктес қосу',
        'btn_broadcast': '📢 Клиенттерге жіберу',
        'btn_set_address': '🏠 Қойма мекенжайын өзгерту',
        'btn_add_website_user': '👤 Сайт қолданушы ID қосу',
        'btn_view_requests': '🛍️ Шопинг өтінімдері',
        'btn_update_request': '✏️ Өтінім мәртебесін жаңарту',
        'admin_update_request_enter_id': 'Өтінім нөмірін жазыңыз (мысалы: 3):',
        'admin_request_not_found': '❌ #{id} өтінімі табылмады.',
        'admin_request_found': (
            '📋 Өтінім #{id}\n'
            '👤 {client} | {phone}\n'
            '📝 {text}\n'
            '📅 {date}\n'
            '📦 Мәртебе: {status}\n\n'
            'Жаңа мәртебені таңдаңыз:'
        ),
        'admin_request_updated': '✅ #{id} өтінімі жаңартылды: {status}',

        'network_stats': (
            '📊 Желі статистикасы (соңғы 7 күн)\n\n'
            '📦 Барлық жөнелтімдер: {total}\n'
            '🚚 Жолда: {in_transit}\n'
            '✅ Жеткізілді: {delivered}\n'
            '⚖️ Жалпы салмақ: {weight} кг\n'
            '💰 Жалпы табыс: ${revenue}\n'
            '🏪 Белсенді пункттер: {partners}'
        ),

        'partners_list': '🏪 Серіктестер тізімі:',
        'partner_line': '• {name} | {location} | Код: {code} | Жөнелтімдер: {count}',
        'no_partners': 'Серіктестер табылмады.',

        'add_partner_name': 'Пункт атауын жазыңыз:',
        'add_partner_location': 'Пункт мекенжайын жазыңыз:',
        'add_partner_code': 'Серіктес кодын жазыңыз (бірегей):',
        'partner_code_exists': '❌ Бұл код бар.',
        'partner_added': '✅ Серіктес қосылды!\nАтауы: {name}\nМекенжайы: {location}\nКод: {code}',

        'broadcast_enter_msg': (
            '📢 Жіберу мәтінін жазыңыз:\n\n'
            'Хабарлама барлық тіркелген клиенттерге жіберіледі.'
        ),
        'broadcast_sent': '✅ Жіберу орындалды!\nЖіберілді: {sent} | Қате: {failed}',

        'set_address_enter': (
            '🏠 АҚШ-тағы қойманың жаңа мекенжайын жазыңыз:\n\n'
            'Ағымдағы мекенжай:\n{current}'
        ),
        'address_updated': '✅ Қойма мекенжайы жаңартылды!',

        'add_wu_id_enter': '👤 owaycargo.com сайтынан қолданушы ID жазыңыз:',
        'add_wu_name_enter': 'Қолданушы атын жазыңыз (ID: {website_id}):',
        'wu_added': '✅ Қолданушы қосылды!\nID: {website_id}\nАты: {name}',
        'wu_id_taken': '❌ Бұл ID-мен қолданушы бар.',

        'view_requests_empty': '🛍️ Жаңа шопинг өтінімдері жоқ.',
        'view_requests_header': '🛍️ Жаңа шопинг өтінімдері:\n',
        'request_line': '#{id} | {client} | {phone}\n📝 {text}\n📅 {date}\n',

        'notify_accepted': (
            '📦 Жөнелтіміңіз OWAY пунктінде қабылданды!\n\n'
            '🔢 Трек-нөмір: {tracking}\n'
            '📍 Қабылдау пункті: {partner}\n'
            '⚖️ Есептік салмақ: {weight} кг\n'
            '💰 Жеткізу бағасы: ${price}\n'
            '🕐 Болжалды мерзім: {delivery_days}\n\n'
            'Жөнелтімді бақылаңыз: /start → Жөнелтімді іздеу'
        ),
        'delivery_days_kg': '7–9 жұмыс күні',
        'delivery_days_kz': '10–14 жұмыс күні',
        'delivery_days_uz': '10–14 жұмыс күні',
        'delivery_days_ru': '15–21 жұмыс күні',
        'delivery_days_by': '15–21 жұмыс күні',

        # Driver
        'driver_enter_code': 'Жүргізуші кодын жазыңыз:',
        'driver_invalid_code': '❌ Қате жүргізуші коды.',
        'driver_welcome': '🚗 Қош келдіңіз, {name}!',
        'driver_menu': '🚗 Жүргізуші мәзірі',
        'btn_my_deliveries': '📋 Менің жеткізулерім',
        'btn_mark_delivered': '✅ Жеткізілді деп белгілеу',
        'no_deliveries': 'Жеткізуге жөнелтім жоқ.',
        'deliveries_list': '📋 Жеткізу үшін жөнелтімдер:',
        'driver_enter_tracking': 'Жеткізілген жөнелтімнің трек-нөмірін жазыңыз:',
        'driver_delivered_ok': '✅ {tracking} жөнелтімі жеткізілді деп белгіленді!',
        'driver_parcel_not_found': '❌ {tracking} жөнелтімі табылмады немесе жеткізілген.',
        'notify_delivered': '🏠 Сіздің {tracking} жөнелтіміңіз жеткізілді! OWAY Cargo-ны таңдағаныңыз үшін рахмет.',
    },

    # ────────────────────────────────────────────────────────────
    # O'ZBEK (uz)
    # ────────────────────────────────────────────────────────────
    'uz': {
        # General
        'choose_language': '🌐 Tilni tanlang / Choose language:\n\n🇷🇺 Русский · 🇬🇧 English · 🇰🇬 Кыргызча · 🇰🇿 Қазақша · 🇺🇿 O\'zbek',
        'welcome': 'OWAY Cargo\'ga xush kelibsiz! 🚚\nRolingizni tanlang:',
        'choose_role': 'Rolingizni tanlang:',
        'btn_client': '📦 Mijoz',
        'btn_partner': '🏪 Hamkor (qabul punkti)',
        'btn_driver': '🚗 Haydovchi',
        'btn_admin': '⚙️ Administrator',
        'back': '⬅️ Orqaga',
        'cancel': '❌ Bekor qilish',
        'main_menu': '🏠 Bosh menyu',
        'invalid_input': 'Noto\'g\'ri kiritish. Qaytadan urinib ko\'ring.',

        # Client registration
        'client_enter_name': 'Ismingizni yozing:',
        'client_enter_phone': 'Telefon raqamingizni ulashish uchun quyidagi tugmani bosing:',
        'btn_share_phone': '📱 Raqamimni yuborish',
        'phone_not_yours': '❌ Bu sizning raqamingiz emas. O\'z raqamingizni ulashish uchun tugmani bosing.',
        'client_registered': '✅ Ro\'yxatdan o\'tish yakunlandi! Xush kelibsiz, {name}!',
        'client_already_registered': '✅ Siz allaqachon ro\'yxatdan o\'tgansiz. Xush kelibsiz, {name}!',

        # Client type selection
        'client_type_select': (
            '👋 OWAY Cargo\'ga xush kelibsiz!\n\n'
            'Nima qilmoqchisiz?\n\n'
            '🛒 AQSh\'dan buyurtma berish — AQSh\'dan tovar sotib olib, mamlakatingizga olish\n\n'
            '📦 AQSh\'dan jo\'natish — siz AQSh\'dasiz va jo\'natma yuborgingiz keladi'
        ),
        'btn_order_type': '🛒 AQSh\'dan buyurtma berish',
        'btn_send_type': '📦 AQSh\'dan jo\'natish',

        # Order menu
        'order_menu': '🛒 AQSh\'dan buyurtma berish\nTelefoningiz: {phone}',
        'btn_my_address': '🏠 AQSh\'dagi manzilim',
        'btn_shopping': '🛍️ Shopping yordamchi',
        'btn_faq': '❓ Ko\'p beriladigan savollar',
        'btn_miniapp': '🌐 Ilovani ochish',

        # Send menu
        'send_menu': '📦 AQSh\'dan jo\'natish\nTelefoningiz: {phone}',
        'btn_find_dropoff': '📍 Qabul punktlari',

        # Shared buttons
        'btn_track': '🔍 Jo\'natmani izlash',
        'btn_history': '📋 Jo\'natmalar tarixi',
        'btn_calculator': '💰 Narx kalkulyatori',
        'btn_support': '💬 Qo\'llab-quvvatlash',
        'btn_change_lang': '🌐 Tilni o\'zgartirish',
        'btn_referral': '👥 Do\'stni taklif qilish',
        'btn_recalculate': '🔄 Qayta hisoblash',
        'btn_contact_manager': '📞 Menejerga bog\'lanish',

        # Legacy
        'client_menu': '📦 Mijoz menyusi\nTelefoningiz: {phone}',

        # Tracking
        'enter_tracking': 'Trek-raqamni yozing:',
        'parcel_not_found': '❌ {tracking} trek-raqamli jo\'natma topilmadi.',
        'parcel_info': (
            '📦 Jo\'natma: {tracking}\n'
            '🌍 Mamlakat: {country}\n'
            '📍 Holat: {status}\n'
            '🏪 Qabul punkti: {partner}\n'
            '⚖️ Og\'irligi: {weight} kg\n'
            '📏 O\'lchamlari: {dims}\n'
            '💰 Narxi: ${price}\n'
            '📅 Qabul qilingan: {date}'
        ),
        'parcel_photo': '🖼️ Jo\'natma surati:',
        'no_photo': 'Surat yo\'q.',
        'no_parcels': 'Sizda jo\'natma yo\'q.',
        'parcel_history': '📋 Jo\'natmalaringiz:',

        # Calculator
        'calc_enter_weight': (
            '⚖️ Jo\'natmaning og\'irligini yozing:\n\n'
            'Misollar: 15.3, 15,3, 15.3 kg, 26 lb\n'
            '(kg yoki funt — avtomatik ravishda o\'giriladi)'
        ),
        'calc_weight_accepted': '✅ Qabul qilindi: {input} = {kg} kg',
        'calc_weight_help': (
            'Og\'irlikni quyidagi formatlardan birida yozing:\n'
            '• 15.3\n• 15,3\n• 15 kg\n• 26 lb'
        ),
        'calc_enter_dims': (
            '📐 O\'lchamlarni bitta qatorda yozing (U×K×B):\n\n'
            'Misollar:\n'
            '• 40x30x20\n'
            '• 40x30x20 cm\n'
            '• 16x12x10 in'
        ),
        'calc_dims_accepted': '✅ Qabul qilindi: {input} = {l}×{w}×{h} sm',
        'calc_dims_help': (
            'O\'lchamlarni bitta qatorda yozing:\n'
            '40x30x20 sm  yoki  16x12x10 in\n\n'
            'Ajratuvchilar: x, ×, *, bo\'shliq'
        ),
        'calc_dims_error': (
            '❓ O\'lchamlarni o\'qiy olmadim.\n\n'
            'Formatda yozing: 40x30x20 yoki 16x12x10 in'
        ),
        'calc_weight_error': (
            '❓ Og\'irlikni o\'qiy olmadim.\n\n'
            'Formatda yozing: 15.3 kg yoki 26 lb'
        ),
        'calc_choose_country': '🌍 Yetkazib berish mamlakatini tanlang:',
        'calc_result': (
            '💰 Narx hisobi:\n\n'
            '🌍 Mamlakat: {country}\n'
            '💲 Tarif: ${rate}/kg\n'
            '⚖️ Haqiqiy og\'irlik: {actual} kg\n'
            '📦 Hajmiy og\'irlik: {vol} kg\n'
            '✅ Hisob og\'irligi: {chargeable} kg\n'
            '💵 Jami: ${price}'
        ),

        # Support
        'support_message': (
            '💬 OWAY Cargo qo\'llab-quvvatlash xizmati\n\n'
            '🌍 MDH mijozlari:\n'
            'WhatsApp: +996 709 969621\n'
            '📲 t.me/+996709969621\n\n'
            '🇺🇸 AQSh mijozlari:\n'
            'WhatsApp: +1 213 276 6898\n'
            '📲 t.me/+12132766898'
        ),

        # Statuses — DIRECT
        'status_accepted': '✅ AQSh\'da qabul qilindi',
        'status_in_transit': '✈️ Yo\'lda',
        'status_arrived': '📍 Yetkazib berish mamlakatiga yetib keldi',
        'status_customs': '🛃 Bojxona tekshiruvida',
        'status_ready': '📦 Olishga tayyor',
        'status_delivered': '🏠 Yetkazib berildi',

        # Statuses — TRANSIT
        'status_transit_zone': '🔄 Tranzit zonada',
        'status_arrived_moscow': '📍 Moskvaga yetib keldi',
        'status_with_driver': '🚚 Yetkazib berishga berildi (SDEK)',

        # Countries
        'accept_choose_country': '🌍 Yetkazib berish mamlakatini tanlang:',
        'country_KG': '🇰🇬 Qirg\'iziston',
        'country_KZ': '🇰🇿 Qozog\'iston',
        'country_UZ': '🇺🇿 O\'zbekiston',
        'country_RU': '🇷🇺 Rossiya',
        'country_BY': '🇧🇾 Belarus',

        # Timeline
        'parcel_timeline': '🕐 Holat tarixi:',
        'timeline_line': '{icon} {status} — {date}',

        # Admin status update
        'btn_update_status': '🔄 Jo\'natma holatini yangilash',
        'admin_enter_tracking': 'Jo\'natmaning trek-raqamini yozing:',
        'admin_parcel_not_found': '❌ {tracking} jo\'natmasi topilmadi.',
        'admin_choose_status': (
            'Jo\'natma: {tracking}\n'
            'Joriy holat: {status}\n\n'
            'Yangi holatni tanlang:'
        ),
        'admin_status_updated': '✅ {tracking} jo\'natmasining holati yangilandi:\n{status}',
        'notify_status_changed': (
            '📬 Jo\'natmangiz bo\'yicha yangilanish!\n\n'
            '🔢 Trek-raqam: {tracking}\n'
            '📦 Yangi holat: {status}\n\n'
            'Jo\'natmani kuzating: /start'
        ),
        'btn_referral': '👥 Do\'stni taklif qilish',
        'referral_info': (
            '👥 Do\'stingizni taklif qiling — ikkalangiz ham bonus oling!\n\n'
            '🎁 Sizga: 1 kg bepul yetkazib berish\n'
            '🎁 Do\'stingizga: birinchi buyurtmaga 10% chegirma\n\n'
            '⚠️ Bonus do\'stingizning birinchi jo\'natmasi yetkazib berilgandan keyingina beriladi.\n\n'
            '🔗 Shaxsiy havolangiz:\n{link}\n\n'
            '📊 Statistika:\n'
            '• Taklif qilingan do\'stlar: {invited}\n'
            '• Olingan bonuslar: {bonuses} kg'
        ),
        'notify_referral_bonus_referrer': (
            '🎉 Do\'stingiz jo\'natmasini oldi!\n\n'
            'Sizning bonus: +1 kg bepul yetkazib berish 🎁\n\n'
            'Bonus keyingi buyurtmangizda qo\'llaniladi. '
            'Buyurtma berishda menejerga eslatib qo\'ying.'
        ),
        'notify_referral_bonus_referred': (
            '🎉 Birinchi yetkazib berish bilan tabriklaymiz!\n\n'
            'Referal bonusingiz: keyingi buyurtmaga 10% chegirma 🎁\n\n'
            'Keyingi jo\'natma buyurtma berishda menejerga eslatib qo\'ying.'
        ),
        'notify_shopping_new': (
            '🛍 Yangi sotib olish arizasi!\n\n'
            '👤 Mijoz: {name}\n'
            '📞 Telefon: {phone}\n'
            '📝 So\'rov:\n{request}'
        ),

        # US Address
        'address_enter_id': (
            '🔑 owaycargo.com saytidan ID\'ngizni yozing\n\n'
            'Agar saytda ro\'yxatdan o\'tmagan bo\'lsangiz — owaycargo.com saytiga kirib, akkaunt yarating.\n'
            'Ro\'yxatdan o\'tgandan keyin ID\'ngiz shaxsiy kabinetda mavjud bo\'ladi.'
        ),
        'address_not_found': (
            '❌ {website_id} ID tizimda topilmadi.\n\n'
            'ID\'ni to\'g\'ri yozganingizni tekshiring yoki qo\'llab-quvvatlash xizmatiga murojaat qiling:\n'
            'WhatsApp: +996 709 969621'
        ),
        'your_us_address': (
            '🏠 AQSh\'dagi jo\'natma olish manzilingiz:\n\n'
            '{address}\n\n'
            '📝 Amerika internet-do\'konlaridan buyurtma berishda shu manzilni ko\'rsating.\n'
            '📦 Omborimizga yetib kelgandan keyin jo\'natmangizni MDH\'dagi manzilingizga yuboramiz.'
        ),
        'address_already_set': (
            '✅ Akkauntingiz saytga bog\'langan.\n\n'
            '🏠 AQSh\'dagi manzilingiz:\n\n{address}'
        ),

        # Shopping assistant
        'shopping_intro': (
            '🛍️ OWAY Cargo Shopping yordamchi\n\n'
            'AQSh\'dan istalgan tovarni siz uchun sotib olamiz!\n\n'
            'Xabaringizda ko\'rsating:\n'
            '• Tovarga havola yoki do\'kon nomi\n'
            '• Tovar tavsifi (rangi, o\'lchami, modeli)\n'
            '• Kerakli byudjet ($)\n\n'
            '💰 Xizmat narxi: tovar narxining 10%\n'
            '⏱ Menejer javobi: 24 soat ichida'
        ),
        'shopping_enter_request': '✍️ So\'rovingizni batafsil yozing:',
        'shopping_received': (
            '✅ So\'rovingiz qabul qilindi!\n\n'
            'Menejerimiz tez orada {phone} raqamingiz orqali bog\'lanadi.\n\n'
            'OWAY Cargo\'ni tanlaganingiz uchun rahmat! 🚚'
        ),
        'btn_my_requests': '🛍 Mening arizalarim',
        'my_requests_empty': 'Sotib olish arizalaringiz yo\'q.',
        'my_requests_header': '🛍 Arizalaringiz:\n',
        'request_status_new': '🟡 Yangi',
        'request_status_in_progress': '🔵 Bajarilmoqda',
        'request_status_done': '✅ Bajarildi',
        'request_status_cancelled': '❌ Bekor qilindi',
        'my_request_line': '#{id} {status}\n📝 {text}\n📅 {date}\n',
        'notify_request_updated': (
            '🛍 Arizangiz #{id} bo\'yicha yangilanish:\n\n'
            '📝 {text}\n'
            '📦 Yangi holat: {status}'
        ),
        'shopping_notify_admin': (
            '🛍️ Yangi shopping yordamchi so\'rovi!\n\n'
            '👤 Mijoz: {name}\n'
            '📱 Telefon: {phone}\n'
            '📝 So\'rov:\n{request}'
        ),

        # FAQ ORDER
        'faq_order': (
            '❓ Ko\'p beriladigan savollar — AQSh\'dan buyurtma berish\n\n'
            '1️⃣ AQSh\'dagi manzilni qanday olaman?\n'
            'owaycargo.com saytida ro\'yxatdan o\'ting → shaxsiy ID oling → '
            'botda «AQSh\'dagi manzilim» orqali yozing. Ombor manzili ko\'rsatiladi.\n\n'
            '2️⃣ Jo\'natmani qanday kuzataman?\n'
            '«Jo\'natmani izlash» tugmasini bosing, trek-raqamni yozing. '
            'Trek-raqam jo\'natma qabul qilinganda beriladi.\n\n'
            '3️⃣ Yetkazib berish qancha turadi?\n'
            '🇰🇬 Qirg\'iziston, 🇰🇿 Qozog\'iston, 🇺🇿 O\'zbekiston: $12/kg\n'
            '🇷🇺 Rossiya, 🇧🇾 Belarus: $18/kg\n'
            'Hajmiy yoki haqiqiy og\'irlik bo\'yicha hisoblanadi (kattasi).\n\n'
            '4️⃣ Yetkazib berish qancha vaqt oladi?\n'
            '🇰🇬 Qirg\'iziston: 7–9 ish kuni.\n'
            '🇰🇿 Qozog\'iston / 🇺🇿 O\'zbekiston: 10–14 ish kuni.\n'
            '🇷🇺 Rossiya / 🇧🇾 Belarus: 15–21 ish kuni.\n\n'
            '5️⃣ Shopping yordamchi nima?\n'
            'Menejerimiz AQSh\'dan istalgan tovarni siz uchun sotib oladi. '
            'Komissiya — tovar narxining 10%. '
            '«Shopping yordamchi» orqali yozing.\n\n'
            '6️⃣ Qaysi tovarlarga taqiq qo\'yilgan?\n'
            'Taqiqlangan: qurol, giyohvand moddalar, xavfli moddalar, '
            'tez buziladigan oziq-ovqat, hayvonlar.\n\n'
            '7️⃣ Qo\'llab-quvvatlash aloqalari:\n'
            '🌍 MDH: WhatsApp +996 709 969621\n'
            '🇺🇸 AQSh: WhatsApp +1 213 276 6898'
        ),

        # FAQ SEND
        'faq_send': (
            '❓ Ko\'p beriladigan savollar — AQSh\'dan jo\'natish\n\n'
            '1️⃣ Jo\'natmani qayerga topshiraman?\n'
            'Menyudagi «Qabul punktlari» orqali yaqin punktni toping. '
            'Xodim jo\'natmani qabul qiladi, tortadi va trek-raqam beradi.\n\n'
            '2️⃣ Yetkazib berish qancha turadi?\n'
            '🇰🇬 Qirg\'iziston, 🇰🇿 Qozog\'iston, 🇺🇿 O\'zbekiston: $12/kg\n'
            '🇷🇺 Rossiya, 🇧🇾 Belarus: $18/kg\n'
            'Aniq hisob uchun «Kalkulyator» foydalaning.\n\n'
            '3️⃣ Qanday hujjatlar kerak?\n'
            'Faqat qabul qiluvchining telefon raqami. '
            'Qimmat tovarlar uchun chek/invoys talab qilinishi mumkin.\n\n'
            '4️⃣ Jo\'natmani qanday o\'rayman?\n'
            'Ishonchli o\'rang: quti, skotch, mo\'rt narsalar uchun pufakchali plyonka. '
            'Kiyimlarni paketga solish mumkin.\n\n'
            '5️⃣ Qaysi tovarlarni jo\'natib bo\'lmaydi?\n'
            'Taqiqlangan: qurol, o\'q-dorilar, 100 ml dan ortiq suyuqliklar, '
            'aerozollar, xavfli kimyoviy moddalar.\n\n'
            '6️⃣ Qabul qiluvchi jo\'natmani qanday kuzatadi?\n'
            'Qabul qiluvchi shu botda ro\'yxatdan o\'tadi va trek-raqamni yozadi. '
            'Har bir holat o\'zgarganda xabar keladi.\n\n'
            '7️⃣ Qo\'llab-quvvatlash aloqalari:\n'
            '🇺🇸 AQSh: WhatsApp +1 213 276 6898\n'
            '🌍 MDH: WhatsApp +996 709 969621'
        ),

        # Drop-off
        'dropoffs_list': '📍 AQSh\'dagi jo\'natma qabul punktlari:',
        'dropoff_line': '• {name} — {location}',
        'no_dropoffs': 'AQSh\'dagi qabul punktlari hali qo\'shilmagan.\nBiz bilan bog\'laning: +1 213 276 6898',

        # Partner
        'partner_enter_code': 'Hamkor kodini yozing:',
        'partner_invalid_code': '❌ Noto\'g\'ri hamkor kodi.',
        'partner_welcome': '🏪 Xush kelibsiz, {name}!\nPunkt: {location}',
        'partner_menu': '🏪 Hamkor menyusi\n📍 {name} — {location}',
        'btn_accept_parcel': '📥 Jo\'natma qabul qilish',
        'btn_my_parcels': '📋 Mening jo\'natmalarim',
        'btn_handoff': '🚚 Haydovchiga berish',
        'btn_stats': '📊 Statistika',

        # Accept parcel
        'accept_send_photo': '📸 Jo\'natmaning suratini oling:',
        'accept_enter_weight': 'Jo\'natmaning og\'irligini yozing (kg):',
        'accept_enter_length': 'Uzunligini yozing (sm):',
        'accept_enter_width': 'Kengligini yozing (sm):',
        'accept_enter_height': 'Balandligini yozing (sm):',
        'accept_enter_client_phone': '📱 Mijozning telefon raqamini yozing:',
        'accept_confirm': (
            '✅ Jo\'natma qabul qilishni tasdiqlang:\n\n'
            '📱 Mijoz: {phone}\n'
            '🌍 Mamlakat: {country}\n'
            '⚖️ Og\'irligi: {weight} kg\n'
            '📏 O\'lchamlari: {l}×{w}×{h} sm\n'
            '📦 Hajmiy og\'irlik: {vol} kg\n'
            '✅ Hisob og\'irligi: {chargeable} kg\n'
            '💰 Narxi: ${price}'
        ),
        'btn_confirm': '✅ Tasdiqlash',
        'parcel_accepted': '✅ Jo\'natma qabul qilindi!\nTrek-raqam: {tracking}',
        'invalid_number': '❌ To\'g\'ri raqam yozing.',

        'no_parcels_at_point': 'Punktingizda jo\'natma yo\'q.',
        'parcels_at_point': '📋 Punktingizdagi jo\'natmalar:',
        'parcel_line': '• {tracking} | {weight}kg | ${price} | {status}',

        'no_parcels_to_handoff': '❌ Haydovchiga berishga jo\'natma yo\'q.',
        'handoff_confirm': '🚚 {count} ta jo\'natmani haydovchiga bermoqchimisiz?',
        'handoff_done': '✅ {count} ta jo\'natma haydovchiga berildi!',
        'handoff_notify': '🚚 Sizning {tracking} jo\'natmangiz haydovchiga berildi va yo\'lda!',

        'partner_stats': (
            '📊 7 kunlik statistika\n\n'
            '📦 Qabul qilingan jo\'natmalar: {count}\n'
            '⚖️ Umumiy og\'irlik: {weight} kg\n'
            '💰 Umumiy daromad: ${revenue}\n'
            '🎁 Sizning mukofotingiz (10%): ${reward}'
        ),

        # Admin
        'admin_enter_code': 'Administrator kodini yozing:',
        'admin_invalid_code': '❌ Noto\'g\'ri administrator kodi.',
        'admin_welcome': '⚙️ OWAY Cargo administrator paneli',
        'admin_menu': '⚙️ Administrator paneli',
        'btn_network_stats': '📊 Tarmoq statistikasi',
        'btn_list_partners': '🏪 Hamkorlar ro\'yxati',
        'btn_add_partner': '➕ Hamkor qo\'shish',
        'btn_broadcast': '📢 Mijozlarga yuborish',
        'btn_set_address': '🏠 Ombor manzilini o\'zgartirish',
        'btn_add_website_user': '👤 Sayt foydalanuvchi ID qo\'shish',
        'btn_view_requests': '🛍️ Shopping arizalari',
        'btn_update_request': '✏️ Ariza holatini yangilash',
        'admin_update_request_enter_id': 'Ariza raqamini yozing (masalan: 3):',
        'admin_request_not_found': '❌ #{id} arizasi topilmadi.',
        'admin_request_found': (
            '📋 Ariza #{id}\n'
            '👤 {client} | {phone}\n'
            '📝 {text}\n'
            '📅 {date}\n'
            '📦 Holat: {status}\n\n'
            'Yangi holatni tanlang:'
        ),
        'admin_request_updated': '✅ #{id} arizasi yangilandi: {status}',

        'network_stats': (
            '📊 Tarmoq statistikasi (oxirgi 7 kun)\n\n'
            '📦 Barcha jo\'natmalar: {total}\n'
            '🚚 Yo\'lda: {in_transit}\n'
            '✅ Yetkazib berildi: {delivered}\n'
            '⚖️ Umumiy og\'irlik: {weight} kg\n'
            '💰 Umumiy daromad: ${revenue}\n'
            '🏪 Faol punktlar: {partners}'
        ),

        'partners_list': '🏪 Hamkorlar ro\'yxati:',
        'partner_line': '• {name} | {location} | Kod: {code} | Jo\'natmalar: {count}',
        'no_partners': 'Hamkorlar topilmadi.',

        'add_partner_name': 'Punkt nomini yozing:',
        'add_partner_location': 'Punkt manzilini yozing:',
        'add_partner_code': 'Hamkor kodini yozing (noyob):',
        'partner_code_exists': '❌ Bunday kod mavjud.',
        'partner_added': '✅ Hamkor qo\'shildi!\nNomi: {name}\nManzili: {location}\nKod: {code}',

        'broadcast_enter_msg': (
            '📢 Yuborish matnini yozing:\n\n'
            'Xabar barcha ro\'yxatdan o\'tgan mijozlarga yuboriladi.'
        ),
        'broadcast_sent': '✅ Yuborish bajarildi!\nYuborildi: {sent} | Xato: {failed}',

        'set_address_enter': (
            '🏠 AQSh\'dagi omborning yangi manzilini yozing:\n\n'
            'Joriy manzil:\n{current}'
        ),
        'address_updated': '✅ Ombor manzili yangilandi!',

        'add_wu_id_enter': '👤 owaycargo.com saytidan foydalanuvchi ID yozing:',
        'add_wu_name_enter': 'Foydalanuvchi ismini yozing (ID: {website_id}):',
        'wu_added': '✅ Foydalanuvchi qo\'shildi!\nID: {website_id}\nIsmi: {name}',
        'wu_id_taken': '❌ Bu ID bilan foydalanuvchi mavjud.',

        'view_requests_empty': '🛍️ Yangi shopping arizalari yo\'q.',
        'view_requests_header': '🛍️ Yangi shopping arizalari:\n',
        'request_line': '#{id} | {client} | {phone}\n📝 {text}\n📅 {date}\n',

        'notify_accepted': (
            '📦 Jo\'natmangiz OWAY punktida qabul qilindi!\n\n'
            '🔢 Trek-raqam: {tracking}\n'
            '📍 Qabul punkti: {partner}\n'
            '⚖️ Hisob og\'irligi: {weight} kg\n'
            '💰 Yetkazib berish narxi: ${price}\n'
            '🕐 Taxminiy muddat: {delivery_days}\n\n'
            'Jo\'natmani kuzating: /start → Jo\'natmani izlash'
        ),
        'delivery_days_kg': '7–9 ish kuni',
        'delivery_days_kz': '10–14 ish kuni',
        'delivery_days_uz': '10–14 ish kuni',
        'delivery_days_ru': '15–21 ish kuni',
        'delivery_days_by': '15–21 ish kuni',

        # Driver
        'driver_enter_code': 'Haydovchi kodini yozing:',
        'driver_invalid_code': '❌ Noto\'g\'ri haydovchi kodi.',
        'driver_welcome': '🚗 Xush kelibsiz, {name}!',
        'driver_menu': '🚗 Haydovchi menyusi',
        'btn_my_deliveries': '📋 Mening yetkazib berishlarim',
        'btn_mark_delivered': '✅ Yetkazib berildi deb belgilash',
        'no_deliveries': 'Yetkazib berishga jo\'natma yo\'q.',
        'deliveries_list': '📋 Yetkazib berish uchun jo\'natmalar:',
        'driver_enter_tracking': 'Yetkazib berilgan jo\'natmaning trek-raqamini yozing:',
        'driver_delivered_ok': '✅ {tracking} jo\'natmasi yetkazib berildi deb belgilandi!',
        'driver_parcel_not_found': '❌ {tracking} jo\'natmasi topilmadi yoki yetkazib berilgan.',
        'notify_delivered': '🏠 Sizning {tracking} jo\'natmangiz yetkazib berildi! OWAY Cargo\'ni tanlaganingiz uchun rahmat.',
    },
}


# All languages used in the system
ALL_LANGS = ('ru', 'en', 'ky', 'kk', 'uz')


def t(lang: str, key: str, **kwargs) -> str:
    """Get translated text. Fallback: lang → ru → en → raw key."""
    lang_dict = TEXTS.get(lang)
    text = None
    if lang_dict:
        text = lang_dict.get(key)
    if text is None:
        text = TEXTS['ru'].get(key)
    if text is None:
        text = TEXTS['en'].get(key, key)
    if kwargs:
        try:
            return text.format(**kwargs)
        except (KeyError, IndexError):
            return text
    return text


def btn_all(key: str) -> tuple:
    """Return a tuple of all translations for a button key, for matching user input."""
    return tuple(dict.fromkeys(TEXTS[lang].get(key, '') for lang in ALL_LANGS if TEXTS[lang].get(key)))
