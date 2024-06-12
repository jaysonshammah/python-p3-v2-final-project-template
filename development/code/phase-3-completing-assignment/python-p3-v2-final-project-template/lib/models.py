import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('FIMEA.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT UNIQUE,
    account_type TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS profile (
    id INTEGER PRIMARY KEY,
    account_number TEXT,
    account_balance REAL,
    client_id INTEGER,
    FOREIGN KEY(client_id) REFERENCES clients(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS assets (
    id INTEGER PRIMARY KEY,
    type TEXT,
    issuer_name TEXT,
    current_price REAL,
    maturity_date DATE
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS holdings (
    id INTEGER PRIMARY KEY,
    account_id INTEGER,
    asset_id INTEGER,
    number_of_shares REAL,
    purchase_price REAL,
    purchase_date DATE,
    client_id INTEGER,
    FOREIGN KEY(account_id) REFERENCES profile(id),
    FOREIGN KEY(asset_id) REFERENCES assets(id),
    FOREIGN KEY(client_id) REFERENCES clients(id)
)
''')

# Commit changes and close connection
conn.commit()
conn.close()
