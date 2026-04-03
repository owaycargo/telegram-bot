# OWAY Cargo — Telegram Bot

Telegram бот для карго-сервиса OWAY Cargo. Доставка из USA в СНГ (Кыргызстан, Казахстан, Узбекистан, Россия, Беларусь).

## Tech Stack

- **Bot:** python-telegram-bot 20.8, ConversationHandler (42 states)
- **Database:** SQLite (WAL mode)
- **Server:** Flask 3.1.3, keep-alive + REST API, PORT 8080
- **Client App:** client.owaycargo.com (Convex backend), opens as Telegram WebApp
- **Deploy:** Railway (auto-deploy on push to `main`)
- **Python:** 3.12

## Structure

```
bot.py              — Main bot logic (42 conversation states)
database.py         — SQLite DB, migrations, config, referral system
texts.py            — UI strings (RU, EN, KY, KK, UZ), t() function
requirements.txt    — Dependencies
runtime.txt         — Python 3.12
Procfile            — Railway entry point
images/             — Mascots + logos
docs/               — Business docs (see below)
```

## Features

**Clients:** two types (ORDER/SEND), parcel tracking, price calculator (kg/lb, cm/in), shopping assistant (10% fee), US address via website ID, referral program, client app (client.owaycargo.com), 5 languages.

**Staff:** `/admin` (broadcast, stats, partners), `/partner` (accept parcels, weigh, tracking), `/driver` (deliveries, mark delivered).

## Referral System

- Deep link: `?start=ref_XXXXXX`
- Referrer: +1 kg free · Referred: 10% off first order
- Bonus after friend's first delivery · Both notified

## Deploy

Railway auto-deploy on push to `main`.

- **Public URL:** `telegram-bot-production-a466.up.railway.app`
- **Client App:** `https://client.owaycargo.com`
- **Images:** `https://telegram-bot-production-a466.up.railway.app/images/<path>`

## Environment Variables

Set in Railway: `BOT_TOKEN`, `ADMIN_CODE`, `PORT` (default 8080).

## Docs

| File | Content |
|---|---|
| [1_COMPANY.md](docs/1_COMPANY.md) | Миссия, команда, преимущества, тон, соцсети, контакты |
| [2_BUSINESS.md](docs/2_BUSINESS.md) | Тарифы, города, логистика, оплата, страховка, товары, B2B |
| [3_WEBSITE_SPEC.md](docs/3_WEBSITE_SPEC.md) | ТЗ на сайт: структура, SEO, дизайн, функционал |
| [4_MARKETING.md](docs/4_MARKETING.md) | Аудитория, каналы, контент, реклама, идеи, конкуренты |

## Support

- USA: WhatsApp +1 213 276 6898
- CIS: WhatsApp +996 709 969621
