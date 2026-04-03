# OWAY Cargo — Telegram Bot

Telegram bot for OWAY Cargo delivery service. Ships goods from USA to CIS countries (Kyrgyzstan, Kazakhstan, Uzbekistan, Russia, Belarus).

## Tech Stack

- **Bot:** python-telegram-bot 20.8, ConversationHandler (42 states)
- **Database:** SQLite with WAL mode
- **Server:** Flask 3.1.3, keep-alive + REST API on PORT 8080
- **Mini App:** Telegram WebApp (HTML) in `miniapp/`
- **Deployment:** Railway (auto-deploy on push to `main`)
- **Python:** 3.12

## Project Structure

```
bot.py              — Main bot logic, 42 conversation states
database.py         — SQLite DB, migrations, config table, referral system
texts.py            — All UI strings (RU, EN), t() translation function
requirements.txt    — Python dependencies
runtime.txt         — Python 3.12 runtime
Procfile            — Railway entry point
miniapp/
  index.html        — Telegram Mini App (4 tabs: Track, Prices, FAQ, Support)
  images/
    mascots/        — 10 mascot PNGs (mascot-*.png)
    logos/           — OWAY Cargo logo variants
docs/               — Business docs, pitch, specs
```

## Features

### Client Features
- **Two client types:** ORDER (CIS clients buying from USA) and SEND (USA clients shipping to CIS)
- **Parcel tracking** by tracking number with status timeline
- **Price calculator** with weight/dimensions, supports kg/lb and cm/in
- **Shopping assistant** — OWAY buys items from USA on client's behalf (10% fee)
- **US address** — linked via owaycargo.com website ID
- **Referral program** — invite friends, bonus after first delivered parcel
- **Mini App** — opens client.owaycargo.com as Telegram Web App
- **5 languages:** Russian, English, Kyrgyz, Kazakh, Uzbek

### Staff Features (hidden commands)
- `/admin` — broadcast, network stats, manage partners, warehouse address, website users, shopping requests
- `/partner` — accept parcels, weigh, assign tracking, handoff to driver
- `/driver` — view deliveries, mark as delivered

### Delivery Routes & Pricing
| Country | Rate | Delivery Time |
|---------|------|---------------|
| Kyrgyzstan | $12/kg | 7–9 business days |
| Kazakhstan | $12/kg | 10–14 business days |
| Uzbekistan | $12/kg | 10–14 business days |
| Russia | $18/kg | 15–21 business days |
| Belarus | $18/kg | 15–21 business days |

## Referral System

- Deep link format: `?start=ref_XXXXXX`
- Referrer gets: +1 kg free shipping
- Referred gets: 10% off first order
- Bonus credited only after friend's first parcel is delivered
- Both parties notified via bot

## Deployment

Hosted on Railway. Auto-deploys on push to `main`.

- **Bot URL:** Railway internal service
- **Public URL:** `telegram-bot-production-a466.up.railway.app`
- **Mini App:** opens `https://client.owaycargo.com` via WebAppInfo
- **Images:** `https://telegram-bot-production-a466.up.railway.app/images/<path>`

## Environment Variables

Set in Railway dashboard:
- `BOT_TOKEN` — Telegram bot token from BotFather
- `ADMIN_CODE` — Admin access code
- `PORT` — Server port (default: 8080)

## Support Contacts

- USA: WhatsApp +1 213 276 6898
- CIS: WhatsApp +996 709 969621
