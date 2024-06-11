from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Client, Account, Asset, Holdings

# Create engine and session
engine = create_engine('sqlite:///FIMEA.db')
Session = sessionmaker(bind=engine)
session = Session()

def add_client():
    print("\nEnter client details:")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    account_type = input("Account Type (Savings/Checking/Investment): ")
    
    client = Client(first_name=first_name, last_name=last_name, email=email, account_type=account_type)
    session.add(client)
    session.commit()
    print("Client added successfully.")

def view_clients():
    clients = session.query(Client).all()
    if clients:
        print("\nClients:")
        for client in clients:
            print(f"{client.id}: {client.first_name} {client.last_name} - {client.email} ({client.account_type} Account)")
    else:
        print("No clients found.")

def update_client():
    client_id = input("\nEnter Client ID to update: ")
    client = session.query(Client).filter_by(id=client_id).first()
    if client:
        print("\nEnter new client details (leave blank to keep current value):")
        first_name = input(f"First Name ({client.first_name}): ") or client.first_name
        last_name = input(f"Last Name ({client.last_name}): ") or client.last_name
        email = input(f"Email ({client.email}): ") or client.email
        account_type = input(f"Account Type ({client.account_type}): ") or client.account_type
        
        client.first_name = first_name
        client.last_name = last_name
        client.email = email
        client.account_type = account_type
        
        session.commit()
        print("Client updated successfully.")
    else:
        print("Client not found.")

def delete_client():
    client_id = input("\nEnter Client ID to delete: ")
    client = session.query(Client).filter_by(id=client_id).first()
    if client:
        session.delete(client)
        session.commit()
        print("Client deleted successfully.")
    else:
        print("Client not found.")

def add_account():
    print("\nEnter account details:")
    account_number = input("Account Number: ")
    account_balance = float(input("Account Balance: "))
    client_id = input("Client ID: ")
    
    account = Account(account_number=account_number, account_balance=account_balance, client_id=client_id)
    session.add(account)
    session.commit()
    print("Account added successfully.")

def view_accounts():
    accounts = session.query(Account).all()
    if accounts:
        print("\nAccounts:")
        for account in accounts:
            print(f"{account.id}: Account Number - {account.account_number}, Balance - {account.account_balance}")
    else:
        print("No accounts found.")

def update_account():
    account_id = input("\nEnter Account ID to update: ")
    account = session.query(Account).filter_by(id=account_id).first()
    if account:
        print("\nEnter new account details (leave blank to keep current value):")
        account_number = input(f"Account Number ({account.account_number}): ") or account.account_number
        account_balance = float(input(f"Account Balance ({account.account_balance}): ") or account.account_balance)
        
        account.account_number = account_number
        account.account_balance = account_balance
        
        session.commit()
        print("Account updated successfully.")
    else:
        print("Account not found.")

def delete_account():
    account_id = input("\nEnter Account ID to delete: ")
    account = session.query(Account).filter_by(id=account_id).first()
    if account:
        session.delete(account)
        session.commit()
        print("Account deleted successfully.")
    else:
        print("Account not found.")

def add_asset():
    print("\nEnter asset details:")
    type = input("Asset Type: ")
    issuer_name = input("Issuer Name: ")
    current_price = float(input("Current Price: "))
    maturity_date = input("Maturity Date (YYYY-MM-DD): ")
    
    asset = Asset(type=type, issuer_name=issuer_name, current_price=current_price, maturity_date=maturity_date)
    session.add(asset)
    session.commit()
    print("Asset added successfully.")

def view_assets():
    assets = session.query(Asset).all()
    if assets:
        print("\nAssets:")
        for asset in assets:
            print(f"{asset.id}: {asset.type} - {asset.issuer_name}, Current Price: {asset.current_price}, Maturity Date: {asset.maturity_date}")
    else:
        print("No assets found.")

def update_asset():
    asset_id = input("\nEnter Asset ID to update: ")
    asset = session.query(Asset).filter_by(id=asset_id).first()
    if asset:
        print("\nEnter new asset details (leave blank to keep current value):")
        type = input(f"Asset Type ({asset.type}): ") or asset.type
        issuer_name = input(f"Issuer Name ({asset.issuer_name}): ") or asset.issuer_name
        current_price = float(input(f"Current Price ({asset.current_price}): ") or asset.current_price)
        maturity_date = input(f"Maturity Date ({asset.maturity_date}): ") or asset.maturity_date
        
        asset.type = type
        asset.issuer_name = issuer_name
        asset.current_price = current_price
        asset.maturity_date = maturity_date
        
        session.commit()
        print("Asset updated successfully.")
    else:
        print("Asset not found.")

def delete_asset():
    asset_id = input("\nEnter Asset ID to delete: ")
    asset = session.query(Asset).filter_by(id=asset_id).first()
    if asset:
        session.delete(asset)
        session.commit()
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
    
    holding = Holdings(account_id=account_id, asset_id=asset_id, number_of_shares=number_of_shares, purchase_price=purchase_price, purchase_date=purchase_date)
    session.add(holding)
    session.commit()
    print("Holding added successfully.")

def view_holdings():
    holdings = session.query(Holdings).all()
    if holdings:
        print("\nHoldings:")
        for holding in holdings:
            print(f"{holding.id}: Account - {holding.account_id}, Asset - {holding.asset_id}, Shares: {holding.number_of_shares}, Purchase Price: {holding.purchase_price}, Purchase Date: {holding.purchase_date}")
    else:
        print("No holdings found.")

def update_holding():
    holding_id = input("\nEnter Holding ID to update: ")
    holding = session.query(Holdings).filter_by(id=holding_id).first()
    if holding:
        print("\nEnter new holding details (leave blank to keep current value):")
        account_id = input(f"Account ID ({holding.account_id}): ") or holding.account_id
        asset_id = input(f"Asset ID ({holding.asset_id}): ") or holding.asset_id
        number_of_shares = float(input(f"Number of Shares ({holding.number_of_shares}): ") or holding.number_of_shares)
        purchase_price = float(input(f"Purchase Price ({holding.purchase_price}): ") or holding.purchase_price)
        purchase_date = input(f"Purchase Date ({holding.purchase_date}): ") or holding.purchase_date
        
        holding.account_id = account_id
        holding.asset_id = asset_id
        holding.number_of_shares = number_of_shares
        holding.purchase_price = purchase_price
        holding.purchase_date = purchase_date
        
        session.commit()
        print("Holding updated successfully.")
    else:
        print("Holding not found.")

def delete_holding():
    holding_id = input("\nEnter Holding ID to delete: ")
    holding = session.query(Holdings).filter_by(id=holding_id).first()
    if holding:
        session.delete(holding)
        session.commit()
        print("Holding deleted successfully.")
    else:
        print("Holding not found.")

def exit_program():
    print("Powered by Virtual")
    exit()