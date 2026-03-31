import sqlite3
import random
import string
from datetime import datetime, timedelta
from typing import Optional

DB_PATH = 'oway_cargo.db'

ADMIN_CODE = 'OWAYADMIN2024'

# Countries and their route types
DIRECT_COUNTRIES = ['KG', 'KZ', 'UZ']   # Kyrgyzstan, Kazakhstan, Uzbekistan
TRANSIT_COUNTRIES = ['RU', 'BY']          # Russia, Belarus — route through Bishkek, hidden

COUNTRY_NAMES = {
    'KG': '🇰🇬 Кыргызстан',
    'KZ': '🇰🇿 Казахстан',
    'UZ': '🇺🇿 Узбекистан',
    'RU': '🇷🇺 Россия',
    'BY': '🇧🇾 Беларусь',
}

# Status flows per route type
DIRECT_STATUSES = ['accepted', 'in_transit', 'arrived', 'customs', 'ready', 'delivered']
TRANSIT_STATUSES = ['accepted', 'in_transit', 'transit_zone', 'arrived_moscow', 'with_driver', 'delivered']


# Pricing per kg by country (flat rate)
RATES = {
    'KG': 12.0,
    'KZ': 12.0,
    'UZ': 12.0,
    'RU': 18.0,
    'BY': 18.0,
}

DEFAULT_DRIVER_CODE = 'DRIVER001'


def route_type_for_country(country_code: str) -> str:
    return 'TRANSIT' if country_code in TRANSIT_COUNTRIES else 'DIRECT'


def statuses_for_route(route_type: str) -> list:
    return TRANSIT_STATUSES if route_type == 'TRANSIT' else DIRECT_STATUSES


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


def init_db():
    conn = get_conn()
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER UNIQUE NOT NULL,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        lang TEXT DEFAULT 'ru',
        created_at TEXT DEFAULT (datetime('now'))
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS partners (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL,
        location TEXT NOT NULL,
        telegram_id INTEGER,
        created_at TEXT DEFAULT (datetime('now'))
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS parcels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tracking TEXT UNIQUE NOT NULL,
        client_phone TEXT NOT NULL,
        client_telegram_id INTEGER,
        partner_id INTEGER NOT NULL,
        destination_country TEXT DEFAULT 'KG',
        route_type TEXT DEFAULT 'DIRECT',
        weight REAL NOT NULL,
        length REAL NOT NULL,
        width REAL NOT NULL,
        height REAL NOT NULL,
        volumetric_weight REAL NOT NULL,
        chargeable_weight REAL NOT NULL,
        price REAL NOT NULL,
        photo_file_id TEXT,
        status TEXT DEFAULT 'accepted',
        created_at TEXT DEFAULT (datetime('now')),
        FOREIGN KEY (partner_id) REFERENCES partners(id)
    )''')

    # Migrations for existing databases
    for col, default in [('destination_country', "'KG'"), ('route_type', "'DIRECT'")]:
        try:
            c.execute(f"ALTER TABLE parcels ADD COLUMN {col} TEXT DEFAULT {default}")
        except sqlite3.OperationalError:
            pass

    c.execute('''CREATE TABLE IF NOT EXISTS parcel_events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        parcel_id INTEGER NOT NULL,
        status TEXT NOT NULL,
        note TEXT,
        created_at TEXT DEFAULT (datetime('now')),
        FOREIGN KEY (parcel_id) REFERENCES parcels(id)
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS drivers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL,
        telegram_id INTEGER,
        created_at TEXT DEFAULT (datetime('now'))
    )''')

    # Seed demo partner and default driver
    c.execute("INSERT OR IGNORE INTO partners (code, name, location) VALUES (?, ?, ?)",
              ('DEMO001', 'Demo Point', 'Demo City, Demo Street 1'))
    c.execute("INSERT OR IGNORE INTO drivers (code, name) VALUES (?, ?)",
              (DEFAULT_DRIVER_CODE, 'Driver 1'))

    conn.commit()
    conn.close()


def generate_tracking() -> str:
    chars = string.ascii_uppercase + string.digits
    suffix = ''.join(random.choices(chars, k=8))
    return f'OWY{suffix}'


def calculate_price(weight: float, length: float, width: float, height: float, country: str = 'KG'):
    volumetric = (length * width * height) / 5000.0
    chargeable = max(weight, volumetric)
    rate = RATES.get(country, 12.0)
    price = chargeable * rate
    return round(volumetric, 2), round(chargeable, 2), round(price, 2)


# ──────────────────── CLIENTS ────────────────────

def get_client(telegram_id: int) -> Optional[sqlite3.Row]:
    conn = get_conn()
    row = conn.execute('SELECT * FROM clients WHERE telegram_id=?', (telegram_id,)).fetchone()
    conn.close()
    return row


def register_client(telegram_id: int, name: str, phone: str, lang: str = 'ru') -> sqlite3.Row:
    conn = get_conn()
    conn.execute(
        'INSERT OR REPLACE INTO clients (telegram_id, name, phone, lang) VALUES (?,?,?,?)',
        (telegram_id, name, phone, lang)
    )
    # Link any existing parcels that were accepted before client registered
    normalized = phone.replace(' ', '').replace('-', '')
    conn.execute(
        """UPDATE parcels SET client_telegram_id=?
           WHERE replace(replace(client_phone,' ',''),'-','')=?
           AND client_telegram_id IS NULL""",
        (telegram_id, normalized)
    )
    conn.commit()
    row = conn.execute('SELECT * FROM clients WHERE telegram_id=?', (telegram_id,)).fetchone()
    conn.close()
    return row


def update_client_lang(telegram_id: int, lang: str):
    conn = get_conn()
    conn.execute('UPDATE clients SET lang=? WHERE telegram_id=?', (lang, telegram_id))
    conn.commit()
    conn.close()


def get_client_by_phone(phone: str) -> Optional[sqlite3.Row]:
    conn = get_conn()
    normalized = phone.replace(' ', '').replace('-', '')
    row = conn.execute('SELECT * FROM clients WHERE replace(replace(phone," ",""),"-","")=?', (normalized,)).fetchone()
    conn.close()
    return row


# ──────────────────── PARTNERS ────────────────────

def get_partner_by_code(code: str) -> Optional[sqlite3.Row]:
    conn = get_conn()
    row = conn.execute('SELECT * FROM partners WHERE code=?', (code.upper(),)).fetchone()
    conn.close()
    return row


def get_partner_by_telegram(telegram_id: int) -> Optional[sqlite3.Row]:
    conn = get_conn()
    row = conn.execute('SELECT * FROM partners WHERE telegram_id=?', (telegram_id,)).fetchone()
    conn.close()
    return row


def link_partner_telegram(partner_id: int, telegram_id: int):
    conn = get_conn()
    conn.execute('UPDATE partners SET telegram_id=? WHERE id=?', (telegram_id, partner_id))
    conn.commit()
    conn.close()


def get_all_partners():
    conn = get_conn()
    rows = conn.execute('SELECT * FROM partners ORDER BY created_at DESC').fetchall()
    conn.close()
    return rows


def add_partner(code: str, name: str, location: str) -> bool:
    conn = get_conn()
    try:
        conn.execute('INSERT INTO partners (code, name, location) VALUES (?,?,?)',
                     (code.upper(), name, location))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        conn.close()
        return False


# ──────────────────── PARCELS ────────────────────

def _log_event(conn: sqlite3.Connection, parcel_id: int, status: str, note: str = None):
    conn.execute(
        'INSERT INTO parcel_events (parcel_id, status, note) VALUES (?,?,?)',
        (parcel_id, status, note)
    )


def create_parcel(client_phone: str, client_telegram_id: Optional[int],
                  partner_id: int, weight: float, length: float, width: float,
                  height: float, photo_file_id: Optional[str],
                  destination_country: str = 'KG') -> sqlite3.Row:
    vol, chargeable, price = calculate_price(weight, length, width, height, destination_country)
    route = route_type_for_country(destination_country)
    tracking = generate_tracking()
    conn = get_conn()
    while conn.execute('SELECT id FROM parcels WHERE tracking=?', (tracking,)).fetchone():
        tracking = generate_tracking()
    conn.execute(
        '''INSERT INTO parcels
           (tracking, client_phone, client_telegram_id, partner_id,
            destination_country, route_type,
            weight, length, width, height, volumetric_weight, chargeable_weight, price, photo_file_id)
           VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
        (tracking, client_phone, client_telegram_id, partner_id,
         destination_country, route,
         weight, length, width, height, vol, chargeable, price, photo_file_id)
    )
    parcel_id = conn.execute('SELECT id FROM parcels WHERE tracking=?', (tracking,)).fetchone()['id']
    _log_event(conn, parcel_id, 'accepted')
    conn.commit()
    row = conn.execute('SELECT * FROM parcels WHERE tracking=?', (tracking,)).fetchone()
    conn.close()
    return row


def get_parcel_by_tracking(tracking: str) -> Optional[sqlite3.Row]:
    conn = get_conn()
    row = conn.execute('SELECT * FROM parcels WHERE tracking=?', (tracking.upper(),)).fetchone()
    conn.close()
    return row


def get_parcel_timeline(parcel_id: int) -> list:
    conn = get_conn()
    rows = conn.execute(
        'SELECT * FROM parcel_events WHERE parcel_id=? ORDER BY created_at ASC',
        (parcel_id,)
    ).fetchall()
    conn.close()
    return rows


def update_parcel_status(tracking: str, new_status: str, note: str = None) -> Optional[sqlite3.Row]:
    """Update parcel status and log the event. Returns updated parcel row or None if not found."""
    conn = get_conn()
    parcel = conn.execute('SELECT * FROM parcels WHERE tracking=?', (tracking.upper(),)).fetchone()
    if not parcel:
        conn.close()
        return None
    conn.execute('UPDATE parcels SET status=? WHERE id=?', (new_status, parcel['id']))
    _log_event(conn, parcel['id'], new_status, note)
    conn.commit()
    row = conn.execute('SELECT * FROM parcels WHERE id=?', (parcel['id'],)).fetchone()
    conn.close()
    return row


def get_client_parcels(client_telegram_id: int):
    conn = get_conn()
    rows = conn.execute(
        'SELECT * FROM parcels WHERE client_telegram_id=? ORDER BY created_at DESC',
        (client_telegram_id,)
    ).fetchall()
    conn.close()
    return rows


def get_partner_parcels(partner_id: int, status: Optional[str] = None):
    conn = get_conn()
    if status:
        rows = conn.execute(
            'SELECT * FROM parcels WHERE partner_id=? AND status=? ORDER BY created_at DESC',
            (partner_id, status)
        ).fetchall()
    else:
        rows = conn.execute(
            'SELECT * FROM parcels WHERE partner_id=? ORDER BY created_at DESC',
            (partner_id,)
        ).fetchall()
    conn.close()
    return rows


def handoff_parcels(partner_id: int) -> list:
    conn = get_conn()
    rows = conn.execute(
        'SELECT * FROM parcels WHERE partner_id=? AND status=?',
        (partner_id, 'accepted')
    ).fetchall()
    if rows:
        for p in rows:
            conn.execute('UPDATE parcels SET status=? WHERE id=?', ('with_driver', p['id']))
            _log_event(conn, p['id'], 'with_driver')
        conn.commit()
    conn.close()
    return rows


def get_partner_stats(partner_id: int) -> dict:
    since = (datetime.utcnow() - timedelta(days=7)).strftime('%Y-%m-%d %H:%M:%S')
    conn = get_conn()
    rows = conn.execute(
        'SELECT * FROM parcels WHERE partner_id=? AND created_at>=?',
        (partner_id, since)
    ).fetchall()
    conn.close()
    count = len(rows)
    total_weight = sum(r['chargeable_weight'] for r in rows)
    revenue = sum(r['price'] for r in rows)
    return {
        'count': count,
        'weight': round(total_weight, 2),
        'revenue': round(revenue, 2),
        'reward': round(revenue * 0.10, 2),
    }


def get_network_stats() -> dict:
    since = (datetime.utcnow() - timedelta(days=7)).strftime('%Y-%m-%d %H:%M:%S')
    conn = get_conn()
    rows = conn.execute(
        'SELECT * FROM parcels WHERE created_at>=?', (since,)
    ).fetchall()
    total = len(rows)
    in_transit_statuses = {'in_transit', 'arrived', 'customs', 'ready', 'transit_zone', 'arrived_moscow', 'with_driver'}
    in_transit = sum(1 for r in rows if r['status'] in in_transit_statuses)
    delivered = sum(1 for r in rows if r['status'] == 'delivered')
    weight = sum(r['chargeable_weight'] for r in rows)
    revenue = sum(r['price'] for r in rows)

    active_partners = conn.execute(
        'SELECT COUNT(DISTINCT partner_id) as cnt FROM parcels WHERE created_at>=?', (since,)
    ).fetchone()['cnt']
    conn.close()
    return {
        'total': total,
        'in_transit': in_transit,
        'delivered': delivered,
        'weight': round(weight, 2),
        'revenue': round(revenue, 2),
        'partners': active_partners,
    }


def get_partner_parcel_count(partner_id: int) -> int:
    conn = get_conn()
    row = conn.execute('SELECT COUNT(*) as cnt FROM parcels WHERE partner_id=?', (partner_id,)).fetchone()
    conn.close()
    return row['cnt']


def get_partner_by_id(partner_id: int) -> Optional[sqlite3.Row]:
    conn = get_conn()
    row = conn.execute('SELECT * FROM partners WHERE id=?', (partner_id,)).fetchone()
    conn.close()
    return row


# ──────────────────── DRIVERS ────────────────────

def get_driver_by_code(code: str) -> Optional[sqlite3.Row]:
    conn = get_conn()
    row = conn.execute('SELECT * FROM drivers WHERE code=?', (code.upper(),)).fetchone()
    conn.close()
    return row


def get_driver_by_telegram(telegram_id: int) -> Optional[sqlite3.Row]:
    conn = get_conn()
    row = conn.execute('SELECT * FROM drivers WHERE telegram_id=?', (telegram_id,)).fetchone()
    conn.close()
    return row


def link_driver_telegram(driver_id: int, telegram_id: int):
    conn = get_conn()
    conn.execute('UPDATE drivers SET telegram_id=? WHERE id=?', (telegram_id, driver_id))
    conn.commit()
    conn.close()


def get_parcels_for_driver() -> list:
    """All parcels currently with driver (ready to deliver)."""
    conn = get_conn()
    rows = conn.execute(
        "SELECT * FROM parcels WHERE status='with_driver' ORDER BY created_at ASC"
    ).fetchall()
    conn.close()
    return rows


def mark_parcel_delivered(tracking: str) -> Optional[sqlite3.Row]:
    return update_parcel_status(tracking, 'delivered')
