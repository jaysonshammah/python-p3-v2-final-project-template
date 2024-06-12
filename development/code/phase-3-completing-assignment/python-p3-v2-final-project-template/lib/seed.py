import sqlite3
from random import choice, randint
from faker import Faker

# Initialize Faker
fake = Faker()

# Connect to the SQLite database
conn = sqlite3.connect('FIMEA.db')
cursor = conn.cursor()

# Seed clients
print("Seeding clients...")
clients = []
for _ in range(10):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    account_type = choice(['Savings', 'Checking', 'Investment'])
    cursor.execute('''
        INSERT INTO client (first_name, last_name, email, account_type)
        VALUES (?, ?, ?, ?)
    ''', (first_name, last_name, email, account_type))
    client_id = cursor.lastrowid
    clients.append(client_id)
print("All clients seeded.")

# Seed accounts
print("Seeding accounts...")
for client_id in clients:
    for _ in range(randint(1, 3)):
        account_number = fake.random_int(min=10000000, max=99999999)
        account_balance = randint(1000, 100000)
        cursor.execute('''
            INSERT INTO account (account_number, account_balance, client_id)
            VALUES (?, ?, ?)
        ''', (account_number, account_balance, client_id))
print("All accounts seeded.")

# Seed assets
print("Seeding assets...")
asset_types = ['Stock', 'Bond', 'ETF']
assets = []
for _ in range(10):
    type = choice(asset_types)
    issuer_name = fake.company()
    current_price = randint(10, 1000)
    maturity_date = fake.date_between(start_date='-1y', end_date='+1y').isoformat()
    cursor.execute('''
        INSERT INTO asset (type, issuer_name, current_price, maturity_date)
        VALUES (?, ?, ?, ?)
    ''', (type, issuer_name, current_price, maturity_date))
    asset_id = cursor.lastrowid
    assets.append(asset_id)
print("All assets seeded.")

# Associate assets with random clients
print("Associating assets with clients...")
for asset_id in assets:
    client_id = choice(clients)
    cursor.execute('''
        INSERT INTO client_asset (client_id, asset_id)
        VALUES (?, ?)
    ''', (client_id, asset_id))

# Seed holdings
print("Seeding holdings...")
for asset_id in assets:
    cursor.execute('SELECT client_id FROM client_asset WHERE asset_id=?', (asset_id,))
    client_ids = [row[0] for row in cursor.fetchall()]
    if client_ids:
        client_id = choice(client_ids)
        cursor.execute('SELECT id FROM account WHERE client_id=?', (client_id,))
        account_ids = [row[0] for row in cursor.fetchall()]
        if account_ids:
            account_id = choice(account_ids)
            number_of_shares = randint(1, 100)
            purchase_price = randint(10, 1000)
            purchase_date = fake.date_between(start_date='-1y', end_date='today').isoformat()
            cursor.execute('''
                INSERT INTO holdings (account_id, asset_id, number_of_shares, purchase_price, purchase_date)
                VALUES (?, ?, ?, ?, ?)
            ''', (account_id, asset_id, number_of_shares, purchase_price, purchase_date))
print("All holdings seeded.")

# Commit and close
conn.commit()
conn.close()
print("All data seeded.")
