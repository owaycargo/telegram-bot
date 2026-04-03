# OWAY CARGO — Полная спецификация Telegram-бота

> Документ для переноса бота на TypeScript monorepo.
> Описывает каждую функцию, flow, базу данных, API и бизнес-логику.

---

## Стек (текущий)

| Компонент | Технология |
|---|---|
| Фреймворк бота | python-telegram-bot 20.8 |
| Архитектура | ConversationHandler (42 состояния, FSM) |
| БД | SQLite (WAL mode), sqlite3.Row |
| HTTP-сервер | Flask 3.1.3 (keep-alive + REST API, PORT 8080) |
| Деплой | Railway (auto-deploy on push to `main`) |
| Языки интерфейса | RU, EN (KY/KZ/UZ пока фоллбэк на RU) |
| Клиентское приложение | client.owaycargo.com (Convex), открывается как Telegram WebApp |

---

## Роли и точки входа

| Роль | Команда | Аутентификация | Видимость |
|---|---|---|---|
| Клиент | `/start` | Регистрация (имя + телефон) | Публичная |
| Партнёр (пункт приёма) | `/partner` | Код партнёра (выдаёт админ) | Скрытая |
| Водитель | `/driver` | Код водителя | Скрытая |
| Админ | `/admin` | ADMIN_CODE (env/hardcoded) | Скрытая |

> В `/start` показывается ТОЛЬКО кнопка "Клиент". Команды staff-ролей скрыты — вводятся вручную.

---

## Conversation States (42 состояния)

```
LANG_SELECT → ROLE_SELECT →
  CLIENT_NAME → CLIENT_PHONE → CLIENT_TYPE_SELECT →
    ORDER_MENU (CIS клиент)
    SEND_MENU (USA клиент)
    CLIENT_MENU (legacy, без типа)

CLIENT_TRACK (общий для ORDER/SEND)
CLIENT_CALC_W → CLIENT_CALC_L → CLIENT_CALC_COUNTRY (калькулятор)
ADDRESS_VERIFY (верификация US-адреса)
SHOPPING_REQUEST (шопинг-помощник)

PARTNER_CODE → PARTNER_MENU
  ACCEPT_PHOTO → ACCEPT_WEIGHT → ACCEPT_LENGTH → ACCEPT_WIDTH → ACCEPT_HEIGHT →
    ACCEPT_CLIENT_PHONE → ACCEPT_COUNTRY → ACCEPT_CONFIRM
  HANDOFF_CONFIRM

ADMIN_CODE_STATE → ADMIN_MENU
  ADD_PARTNER_NAME → ADD_PARTNER_LOCATION → ADD_PARTNER_CODE
  ADMIN_UPDATE_TRACKING → ADMIN_UPDATE_STATUS
  ADMIN_BROADCAST
  ADMIN_SET_ADDRESS
  ADMIN_ADD_WU_ID → ADMIN_ADD_WU_NAME
  ADMIN_UPDATE_REQUEST

DRIVER_CODE_STATE → DRIVER_MENU → DRIVER_DELIVER
```

---

## Flow 1: Регистрация клиента

### /start (новый пользователь)
1. Показать маскота (mascot-wink.png)
2. Если пришёл по реферальной ссылке (`?start=ref_XXXXXX`) — сохранить `referred_by`
3. Если уже зарегистрирован — перейти в его меню (ORDER_MENU / SEND_MENU)
4. Новый пользователь → выбор языка (RU / EN / KG / KZ / UZ)
5. Выбор роли (только "Клиент")
6. Ввод имени (текст)
7. Отправка телефона (кнопка request_contact — **только свой номер**, проверка user_id)
8. Регистрация в БД + привязка существующих посылок по телефону
9. Если `referred_by` — сохранить реферала
10. Выбор типа клиента:
    - **🛒 Заказать из США** → ORDER (клиент в СНГ)
    - **📦 Отправить из США** → SEND (клиент в США)

### /start (возвращающийся)
1. Показать маскота
2. Приветствие по имени → сразу в меню по `client_type`

---

## Flow 2: Меню ORDER (клиент из СНГ)

Кнопки:
| Кнопка | Действие |
|---|---|
| 🔍 Отследить посылку | → ввод трек-номера → информация + timeline + фото |
| 📋 История посылок | Список всех посылок с трекингом, статусом, ценой |
| 🏠 Мой адрес в США | Верификация website_id → показ адреса склада |
| 🛍️ Шопинг-помощник | Свободный текст запроса → уведомление админам |
| 📋 Мои заявки | Список shopping_requests с ID, статусом, датой |
| 💰 Калькулятор цены | → вес → габариты → страна → результат |
| ❓ Частые вопросы | FAQ текст |
| 💬 Поддержка | Контакты WhatsApp (USA + CIS) |
| 👥 Пригласить друга | Реферальная ссылка + статистика |
| 🌐 Открыть приложение | WebApp button → client.owaycargo.com |
| 🌐 Сменить язык | → выбор языка |
| 🏠 Главное меню | → /start |

---

## Flow 3: Меню SEND (клиент из США)

Кнопки:
| Кнопка | Действие |
|---|---|
| 🔍 Отследить посылку | → ввод трек-номера |
| 📋 История посылок | Список посылок |
| 💰 Калькулятор цены | → вес → габариты → страна → результат |
| 📍 Пункты приёма | Список всех партнёров (имя, адрес) |
| ❓ Частые вопросы | FAQ текст |
| 💬 Поддержка | Контакты WhatsApp |
| 👥 Пригласить друга | Реферальная ссылка |
| 🌐 Открыть приложение | WebApp → client.owaycargo.com |
| 🌐 Сменить язык | → выбор языка |
| 🏠 Главное меню | → /start |

---

## Flow 4: Трекинг посылки

1. Клиент вводит трек-номер (формат: `OWYXXXXXXXX`)
2. Поиск в БД по `tracking`
3. Если найден — показать:
   - Трек-номер, страна, статус, пункт приёма, вес, размеры, цена, дата
   - Timeline событий (все `parcel_events` в хронологическом порядке)
   - Фото посылки (если есть `photo_file_id`)
4. Если не найден — сообщение об ошибке

---

## Flow 5: Калькулятор цены

### Шаг 1: Вес
- Ввод: число с единицами или без
- Поддерживает: `15.3`, `15,3`, `15.3 кг`, `26 lb`
- Автоконвертация фунтов → кг (× 0.453592)
- Подсказка по вводу: "как", "пример", "how", "example"

### Шаг 2: Габариты (одна строка)
- Формат: `Д×Ш×В`
- Поддерживает: `40x30x20`, `40x30x20 cm`, `16x12x10 in`
- Разделители: `x`, `х` (кириллица), `*`, пробел
- Автоконвертация дюймов → см (× 2.54)

### Шаг 3: Выбор страны
- 🇰🇬 Кыргызстан / 🇰🇿 Казахстан / 🇺🇿 Узбекистан / 🇷🇺 Россия / 🇧🇾 Беларусь

### Результат:
- Фактический вес, объёмный вес, расчётный вес, цена
- **Формула объёмного веса:** `Д × Ш × В / 5000`
- **Расчётный вес:** `max(фактический, объёмный)`
- **Цена:** `расчётный вес × тариф`
- Кнопки: Рассчитать ещё / Связаться с менеджером / Назад

---

## Flow 6: US Address (верификация)

1. Клиент нажимает "Мой адрес в США"
2. Если `website_id` уже привязан — показать адрес склада
3. Если нет — ввод website_id (из client.owaycargo.com)
4. Поиск в таблице `website_users`
5. Если найден — привязка `website_id` к клиенту + привязка `telegram_id` к website_user
6. Показ адреса склада из `config.us_warehouse_address`

---

## Flow 7: Шопинг-помощник

1. Клиент описывает что хочет купить (свободный текст)
2. Создание записи в `shopping_requests`
3. Уведомление ВСЕХ админов (по `admin_telegram_ids` из config)
4. Клиент может просматривать свои заявки (последние 10, с ID и статусом)
5. Админ меняет статус: `new` → `in_progress` / `done` / `cancelled`
6. При смене статуса — уведомление клиенту

---

## Flow 8: Реферальная система

### Механика:
- Каждый клиент получает уникальный реферальный код (6 символов, `ABCDEFGHJKLMNPQRSTUVWXYZ23456789`)
- Deep link: `t.me/owaycargo_bot?start=ref_XXXXXX`
- Нельзя реферить самого себя

### Бонусы (срабатывают при ПЕРВОЙ доставленной посылке приглашённого):
- **Пригласивший:** +1 кг бесплатно
- **Приглашённый:** 10% скидка на следующий заказ
- Оба получают уведомление
- `ref_bonus_given = 1` — бонус выдаётся только один раз

### Отображение:
- Реферальная ссылка
- Количество приглашённых
- Количество активированных бонусов

---

## Flow 9: Партнёр (пункт приёма)

### Аутентификация:
- `/partner` → ввод кода → привязка `telegram_id` к партнёру
- Повторный вход — автоматически по `telegram_id`

### Меню:
| Кнопка | Действие |
|---|---|
| 📦 Принять посылку | → Flow приёма |
| 📋 Мои посылки | Список посылок на точке |
| 🚛 Передать водителю | Массовая передача `accepted` → `with_driver` |
| 📊 Статистика | Посылки/вес/выручка/вознаграждение за 7 дней |
| 🏠 Главное меню | → /start |

### Flow приёма посылки:
1. **Фото посылки** (или пропустить текстом)
2. **Вес** (число, кг)
3. **Длина** (число, см)
4. **Ширина** (число, см)
5. **Высота** (число, см)
6. **Телефон клиента** (текст)
7. **Страна назначения** (выбор из 5)
8. **Подтверждение** — показать summary: телефон, страна, вес, габариты, объёмный вес, расчётный вес, цена
9. Создание посылки → генерация трек-номера
10. **Уведомление клиенту** (если найден по телефону): трекинг, пункт приёма, вес, цена, ожидаемый срок

### Передача водителю (Handoff):
1. Показать количество посылок со статусом `accepted`
2. Подтверждение → все `accepted` → `with_driver`
3. Уведомление каждому клиенту о передаче

### Статистика партнёра (за 7 дней):
- Количество посылок
- Общий вес
- Выручка
- Вознаграждение (10% от выручки)

---

## Flow 10: Водитель

### Аутентификация:
- `/driver` → ввод кода → привязка `telegram_id`
- Повторный вход — автоматически

### Меню:
| Кнопка | Действие |
|---|---|
| 📋 Мои доставки | Список `with_driver` посылок (трекинг, страна, телефон, вес) |
| ✅ Отметить доставку | Ввод трек-номера → `delivered` |
| 🏠 Главное меню | → /start |

### Доставка:
1. Ввод трек-номера
2. Проверка: посылка существует + статус `with_driver`
3. Статус → `delivered`
4. Уведомление клиенту
5. **Триггер реферального бонуса** (если это первая доставка приглашённого клиента)

---

## Flow 11: Админ

### Аутентификация:
- `/admin` → ввод ADMIN_CODE → `is_admin = True`
- `telegram_id` добавляется в `admin_telegram_ids` (для уведомлений)

### Меню:
| Кнопка | Действие |
|---|---|
| 📊 Статистика сети | За 7 дней: посылки, в пути, доставлено, вес, выручка, активные партнёры |
| 📋 Партнёры | Список всех партнёров + количество посылок |
| ➕ Добавить партнёра | Имя → адрес → код |
| 🔄 Обновить статус | Трек-номер → выбор статуса (зависит от route_type) |
| 📢 Рассылка | Текст → отправка всем клиентам |
| 🏠 Адрес склада | Показать/изменить адрес US warehouse |
| 👤 Добавить пользователя | Website ID → имя (для верификации US адреса) |
| 📋 Заявки | Список новых shopping_requests |
| ✏️ Обновить заявку | ID → выбор статуса → уведомление клиенту |
| 🏠 Главное меню | → /start |

### Обновление статуса посылки:
1. Ввод трек-номера
2. Показать текущий статус
3. Выбор нового статуса (список зависит от route_type: DIRECT или TRANSIT)
4. Обновление + запись в parcel_events
5. Уведомление клиенту
6. Если `delivered` — проверка реферального бонуса

---

## Статусы посылок

### DIRECT (KG, KZ, UZ):
| Статус | Иконка | Описание |
|---|---|---|
| `accepted` | ✅ | Принята на пункте |
| `in_transit` | ✈️ | В пути |
| `arrived` | 📍 | Прибыла в хаб |
| `customs` | 🛃 | На таможне |
| `ready` | 📦 | Готова к выдаче |
| `delivered` | 🏠 | Доставлена |

### TRANSIT (RU, BY):
| Статус | Иконка | Описание |
|---|---|---|
| `accepted` | ✅ | Принята на пункте |
| `in_transit` | ✈️ | В пути |
| `transit_zone` | 🔄 | Транзитная зона |
| `arrived_moscow` | 📍 | Прибыла в Москву |
| `with_driver` | 🚚 | У водителя |
| `delivered` | 🏠 | Доставлена |

---

## Тарифы и расчёт

| Страна | Код | Тариф | Срок | Маршрут |
|---|---|---|---|---|
| Кыргызстан | KG | $12/кг | 7–9 дней | DIRECT |
| Казахстан | KZ | $12/кг | 10–14 дней | DIRECT |
| Узбекистан | UZ | $12/кг | 10–14 дней | DIRECT |
| Россия | RU | $18/кг | 15–21 день | TRANSIT |
| Беларусь | BY | $18/кг | 15–21 день | TRANSIT |

**Формулы:**
```
volumetric_weight = (L × W × H) / 5000
chargeable_weight = max(actual_weight, volumetric_weight)
price = chargeable_weight × rate
```

---

## База данных — Схема

### clients
| Поле | Тип | Описание |
|---|---|---|
| id | INTEGER PK | Auto-increment |
| telegram_id | INTEGER UNIQUE | Telegram user ID |
| name | TEXT | Имя клиента |
| phone | TEXT | Телефон (с +) |
| lang | TEXT | Язык (ru/en) |
| client_type | TEXT | ORDER / SEND / NULL |
| website_id | TEXT | ID с client.owaycargo.com |
| referral_code | TEXT UNIQUE | 6-символьный код |
| referred_by | TEXT | Код того, кто пригласил |
| ref_bonus_given | INTEGER | 0/1 — бонус выдан |
| created_at | TEXT | datetime('now') |

### parcels
| Поле | Тип | Описание |
|---|---|---|
| id | INTEGER PK | Auto-increment |
| tracking | TEXT UNIQUE | Трек-номер (OWY + 8 символов) |
| client_phone | TEXT | Телефон клиента |
| client_telegram_id | INTEGER | TG ID (может быть NULL) |
| partner_id | INTEGER FK | Пункт приёма |
| destination_country | TEXT | KG/KZ/UZ/RU/BY |
| route_type | TEXT | DIRECT/TRANSIT |
| weight | REAL | Фактический вес (кг) |
| length | REAL | Длина (см) |
| width | REAL | Ширина (см) |
| height | REAL | Высота (см) |
| volumetric_weight | REAL | Объёмный вес |
| chargeable_weight | REAL | Расчётный вес |
| price | REAL | Стоимость ($) |
| photo_file_id | TEXT | Telegram file_id фото |
| status | TEXT | Текущий статус |
| created_at | TEXT | datetime('now') |

### parcel_events
| Поле | Тип | Описание |
|---|---|---|
| id | INTEGER PK | Auto-increment |
| parcel_id | INTEGER FK | Ссылка на посылку |
| status | TEXT | Статус события |
| note | TEXT | Комментарий (опционально) |
| created_at | TEXT | datetime('now') |

### partners
| Поле | Тип | Описание |
|---|---|---|
| id | INTEGER PK | Auto-increment |
| code | TEXT UNIQUE | Код для входа |
| name | TEXT | Название точки |
| location | TEXT | Адрес |
| telegram_id | INTEGER | TG ID партнёра |
| created_at | TEXT | datetime('now') |

### drivers
| Поле | Тип | Описание |
|---|---|---|
| id | INTEGER PK | Auto-increment |
| code | TEXT UNIQUE | Код для входа |
| name | TEXT | Имя водителя |
| telegram_id | INTEGER | TG ID водителя |
| created_at | TEXT | datetime('now') |

### config
| Поле | Тип | Описание |
|---|---|---|
| key | TEXT PK | Ключ |
| value | TEXT | Значение |

Используемые ключи:
- `us_warehouse_address` — адрес склада в США
- `miniapp_url` — URL клиентского приложения (client.owaycargo.com)
- `admin_telegram_ids` — список TG ID админов через запятую

### website_users
| Поле | Тип | Описание |
|---|---|---|
| id | INTEGER PK | Auto-increment |
| website_id | TEXT UNIQUE | ID на сайте |
| name | TEXT | Имя |
| telegram_id | INTEGER | TG ID (привязывается при верификации) |
| created_at | TEXT | datetime('now') |

### shopping_requests
| Поле | Тип | Описание |
|---|---|---|
| id | INTEGER PK | Auto-increment |
| client_telegram_id | INTEGER | TG ID клиента |
| client_name | TEXT | Имя |
| client_phone | TEXT | Телефон |
| request_text | TEXT | Описание запроса |
| status | TEXT | new / in_progress / done / cancelled |
| created_at | TEXT | datetime('now') |

---

## REST API (Flask)

| Метод | Эндпоинт | Описание |
|---|---|---|
| GET | `/` | Health check → `OK` |
| GET | `/track/<tracking>` | Трекинг посылки (JSON: tracking, status, country, weight, price, events) |
| GET | `/calculate?weight=&length=&width=&height=&country=` | Калькулятор (JSON: actual, volumetric, chargeable, rate, price) |
| GET | `/rates` | Тарифы по странам (JSON) |
| GET | `/images/<path>` | Статические изображения (маскоты, логотипы) |

---

## Уведомления (push через бота)

| Событие | Получатель | Содержание |
|---|---|---|
| Посылка принята | Клиент (по телефону) | Трекинг, пункт, вес, цена, срок доставки |
| Статус изменён | Клиент | Трекинг + новый статус |
| Передача водителю | Клиент | Трекинг + "передана курьеру" |
| Доставлена | Клиент | Трекинг + "доставлена" |
| Реферальный бонус | Пригласивший | +1 кг бесплатно |
| Реферальный бонус | Приглашённый | 10% скидка |
| Новая заявка шопинга | Все админы | Имя, телефон, текст запроса |
| Статус заявки изменён | Клиент | ID заявки, текст, новый статус |

---

## Языки и локализация

### Текущая реализация:
- ~175 ключей на каждый язык
- Функция `t(lang, key, **kwargs)` с fallback: `lang` → `en` → raw key
- Все строки в `texts.py` (dict `TEXTS`)
- Кнопки проверяются двуязычно: `t('ru', key)` и `t('en', key)`

### Языки:
| Код | Язык | Статус |
|---|---|---|
| ru | Русский | Полный |
| en | English | Полный |
| ky | Кыргызча | Фоллбэк на RU |
| kk | Қазақша | Фоллбэк на RU |
| uz | O'zbek | Фоллбэк на RU |

### Где используются строки:
- Меню, кнопки, сообщения, ошибки, FAQ, подтверждения
- Статусы посылок (`status_accepted`, `status_in_transit`, etc.)
- Названия стран (`country_KG`, `country_RU`, etc.)
- Сроки доставки (`delivery_days_kg`, etc.)

---

## Трек-номер

- Формат: `OWY` + 8 случайных символов (A-Z, 0-9)
- Генерация: `generate_tracking()` с проверкой уникальности в БД
- Пример: `OWYAB3K9X2M`

---

## Seed данные

При первом запуске создаются:
- Демо-партнёр: `DEMO001` / "Demo Point" / "Demo City, Demo Street 1"
- Демо-водитель: `DRIVER001` / "Driver 1"
- Config: `us_warehouse_address` (placeholder), `miniapp_url` (client.owaycargo.com)

---

## Environment Variables

| Переменная | Описание | Default |
|---|---|---|
| `BOT_TOKEN` | Telegram Bot Token | hardcoded (dev) |
| `ADMIN_CODE` | Код для входа в админку | `OWAYADMIN2024` |
| `PORT` | HTTP-порт для Flask | `8080` |

---

## Архитектура запуска

```
main()
├── db.init_db()           # SQLite init + migrations
├── Flask thread (daemon)  # HTTP API на PORT 8080
└── Application.run_polling()  # Long polling Telegram
```

- Flask работает в отдельном daemon-треде
- Bot использует long polling (не webhooks)
- Railway держит процесс через `Procfile: web: python bot.py`

---

## Маскоты

10 PNG файлов в `images/mascots/`:

| Файл | Использование |
|---|---|
| mascot-wink.png | Welcome при /start, поддержка USA |
| mascot-money.png | Калькулятор |
| mascot-love.png | Поддержка CIS |
| mascot-party.png | Посылка найдена |
| mascot-scared.png | — |
| mascot-sad.png | — |
| mascot-laugh.png | — |
| mascot-shush.png | — |
| mascot-cool.png | — |
| mascot-thinking.png | — |

---

## Бизнес-правила

1. **Телефон клиента** — только свой (проверка `contact.user_id == effective_user.id`)
2. **Привязка посылок** — при регистрации все посылки с совпадающим телефоном привязываются к `telegram_id`
3. **Реферал** — нельзя пригласить себя; бонус только после первой доставки; однократно
4. **Партнёр** — 10% от выручки (в статистике, не автоматические выплаты)
5. **Route type** — определяется автоматически по стране (`KG/KZ/UZ` = DIRECT, `RU/BY` = TRANSIT)
6. **Статусы** — разные цепочки для DIRECT и TRANSIT маршрутов
7. **Broadcast** — отправляется всем зарегистрированным клиентам без фильтров

---

_Обновлено: апрель 2026 · v1.0_
