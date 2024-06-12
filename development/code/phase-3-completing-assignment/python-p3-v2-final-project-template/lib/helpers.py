import sqlite3

# Create a database connection and cursor
conn = sqlite3.connect('FIMEA.db')
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS Client (
                    id INTEGER PRIMARY KEY,
                    first_name TEXT,
                    last_name TEXT,
                    email TEXT UNIQUE,
                    account_type TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Account (
                    id INTEGER PRIMARY KEY,
                    account_number TEXT,
                    account_balance REAL,
                    client_id INTEGER,
                    FOREIGN KEY (client_id) REFERENCES Client(id))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Asset (
                    id INTEGER PRIMARY KEY,
                    type TEXT,
                    issuer_name TEXT,
                    current_price REAL,
                    maturity_date DATE)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Holdings (
                    id INTEGER PRIMARY KEY,
                    account_id INTEGER,
                    asset_id INTEGER,
                    number_of_shares REAL,
                    purchase_price REAL,
                    purchase_date DATE,
                    FOREIGN KEY (account_id) REFERENCES Account(id),
                    FOREIGN KEY (asset_id) REFERENCES Asset(id))''')

# Commit changes after table creation
conn.commit()

# Other functions
# ...

# Close the connection
conn.close()




import sqlite3

# Create a database connection and cursor
conn = sqlite3.connect('FIMEA.db')
cursor = conn.cursor()

def add_client():
    print("\nEnter client details:")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    account_type = input("Account Type (Savings/Checking/Investment): ")

    cursor.execute("INSERT INTO Client (first_name, last_name, email, account_type) VALUES (?, ?, ?, ?)",
                   (first_name, last_name, email, account_type))
    conn.commit()
    print("Client added successfully.")

def view_clients():
    cursor.execute("SELECT * FROM Client")
    clients = cursor.fetchall()
    if clients:
        print("\nClients:")
        for client in clients:
            print(f"{client[0]}: {client[1]} {client[2]} - {client[3]} ({client[4]} Account)")
    else:
        print("No clients found.")

def update_client():
    client_id = input("\nEnter Client ID to update: ")
    cursor.execute("SELECT * FROM Client WHERE id = ?", (client_id,))
    client = cursor.fetchone()
    if client:
        print("\nEnter new client details (leave blank to keep current value):")
        first_name = input(f"First Name ({client[1]}): ") or client[1]
        last_name = input(f"Last Name ({client[2]}): ") or client[2]
        email = input(f"Email ({client[3]}): ") or client[3]
        account_type = input(f"Account Type ({client[4]}): ") or client[4]

        cursor.execute("UPDATE Client SET first_name = ?, last_name = ?, email = ?, account_type = ? WHERE id = ?",
                       (first_name, last_name, email, account_type, client_id))
        conn.commit()
        print("Client updated successfully.")
    else:
        print("Client not found.")

def delete_client():
    client_id = input("\nEnter Client ID to delete: ")
    cursor.execute("SELECT * FROM Client WHERE id = ?", (client_id,))
    client = cursor.fetchone()
    if client:
        cursor.execute("DELETE FROM Client WHERE id = ?", (client_id,))
        conn.commit()
        print("Client deleted successfully.")
    else:
        print("Client not found.")

def add_account():
    print("\nEnter account details:")
    account_number = input("Account Number: ")
    account_balance = float(input("Account Balance: "))
    client_id = input("Client ID: ")

    cursor.execute("INSERT INTO Account (account_number, account_balance, client_id) VALUES (?, ?, ?)",
                   (account_number, account_balance, client_id))
    conn.commit()
    print("Account added successfully.")

def view_accounts():
    cursor.execute("SELECT * FROM Account")
    accounts = cursor.fetchall()
    if accounts:
        print("\nAccounts:")
        for account in accounts:
            print(f"{account[0]}: Account Number - {account[1]}, Balance - {account[2]}")
    else:
        print("No accounts found.")

def update_account():
    account_id = input("\nEnter Account ID to update: ")
    cursor.execute("SELECT * FROM Account WHERE id = ?", (account_id,))
    account = cursor.fetchone()
    if account:
        print("\nEnter new account details (leave blank to keep current value):")
        account_number = input(f"Account Number ({account[1]}): ") or account[1]
        account_balance = float(input(f"Account Balance ({account[2]}): ") or account[2])

        cursor.execute("UPDATE Account SET account_number = ?, account_balance = ? WHERE id = ?",
                       (account_number, account_balance, account_id))
        conn.commit()
        print("Account updated successfully.")
    else:
        print("Account not found.")

def delete_account():
    account_id = input("\nEnter Account ID to delete: ")
    cursor.execute("SELECT * FROM Account WHERE id = ?", (account_id,))
    account = cursor.fetchone()
    if account:
        cursor.execute("DELETE FROM Account WHERE id = ?", (account_id,))
        conn.commit()
        print("Account deleted successfully.")
    else:
        print("Account not found.")

def add_asset():
    print("\nEnter asset details:")
    type = input("Asset Type: ")
    issuer_name = input("Issuer Name: ")
    current_price = float(input("Current Price: "))
    maturity_date = input("Maturity Date (YYYY-MM-DD): ")

    cursor.execute("INSERT INTO Asset (type, issuer_name, current_price, maturity_date) VALUES (?, ?, ?, ?)",
                   (type, issuer_name, current_price, maturity_date))
    conn.commit()
    print("Asset added successfully.")

def view_assets():
    cursor.execute("SELECT * FROM Asset")
    assets = cursor.fetchall()
    if assets:
        print("\nAssets:")
        for asset in assets:
            print(f"{asset[0]}: {asset[1]} - {asset[2]}, Current Price: {asset[3]}, Maturity Date: {asset[4]}")
    else:
        print("No assets found.")

def update_asset():
    asset_id = input("\nEnter Asset ID to update: ")
    cursor.execute("SELECT * FROM Asset WHERE id = ?", (asset_id,))
    asset = cursor.fetchone()
    if asset:
        print("\nEnter new asset details (leave blank to keep current value):")
        type = input(f"Asset Type ({asset[1]}): ") or asset[1]
        issuer_name = input(f"Issuer Name ({asset[2]}): ") or asset[2]
        current_price = float(input(f"Current Price ({asset[3]}): ") or asset[3])
        maturity_date = input(f"Maturity Date ({asset[4]}): ") or asset[4]

        cursor.execute("UPDATE Asset SET type = ?, issuer_name = ?, current_price = ?, maturity_date = ? WHERE id = ?",
                       (type, issuer_name, current_price, maturity_date, asset_id))
        conn.commit()
        print("Asset updated successfully.")
    else:
        print("Asset not found.")

def delete_asset():
    asset_id = input("\nEnter Asset ID to delete: ")
    cursor.execute("SELECT * FROM Asset WHERE id = ?", (asset_id,))
    asset = cursor.fetchone()
    if asset:
        cursor.execute("DELETE FROM Asset WHERE id = ?", (asset_id,))
        conn.commit()
        print("Asset deleted successfully.")
    else:
        print("Asset not found.")

def add_holding():
    print("\nEnter holding details:")
    account_id = input("Account ID: ")
    asset_id = input("Asset ID: ")
    number_of_shares = float(input("Number of Shares: "))
    purchase_price = float(input("Purchase Price: "))
    purchase_date = input("Purchase Date (YYYY-MM-DD): ")

    cursor.execute("INSERT INTO Holdings (account_id, asset_id, number_of_shares, purchase_price, purchase_date) VALUES (?, ?, ?, ?, ?)",
                   (account_id, asset_id, number_of_shares, purchase_price, purchase_date))
    conn.commit()
    print("Holding added successfully.")

def view_holdings():
    cursor.execute("SELECT * FROM Holdings")
    holdings = cursor.fetchall()
    if holdings:
        print("\nHoldings:")
        for holding in holdings:
            print(f"{holding[0]}: Account - {holding[1]}, Asset - {holding[2]}, Shares: {holding[3]}, Purchase Price: {holding[4]}, Purchase Date: {holding[5]}")
    else:
        print("No holdings found.")

def update_holding():
    holding_id = input("\nEnter Holding ID to update: ")
    cursor.execute("SELECT * FROM Holdings WHERE id = ?", (holding_id,))
    holding = cursor.fetchone()
    if holding:
        print("\nEnter new holding details (leave blank to keep current value):")
        account_id = input(f"Account ID ({holding[1]}): ") or holding[1]
        asset_id = input(f"Asset ID ({holding[2]}): ") or holding[2]
        number_of_shares = float(input(f"Number of Shares ({holding[3]}): ") or holding[3])
        purchase_price = float(input(f"Purchase Price ({holding[4]}): ") or holding[4])
        purchase_date = input(f"Purchase Date ({holding[5]}): ") or holding[5]

        cursor.execute("UPDATE Holdings SET account_id = ?, asset_id = ?, number_of_shares = ?, purchase_price = ?, purchase_date = ? WHERE id = ?",
                       (account_id, asset_id, number_of_shares, purchase_price, purchase_date, holding_id))
        conn.commit()
        print("Holding updated successfully.")
    else:
        print("Holding not found.")

def delete_holding():
    holding_id = input("\nEnter Holding ID to delete: ")
    cursor.execute("SELECT * FROM Holdings WHERE id = ?", (holding_id,))
    holding = cursor.fetchone()
    if holding:
        cursor.execute("DELETE FROM Holdings WHERE id = ?", (holding_id,))
        conn.commit()
        print("Holding deleted successfully.")
    else:
        print("Holding not found.")

def exit_program():
    print("Powered by Virtual")
    conn.close()
    exit()
