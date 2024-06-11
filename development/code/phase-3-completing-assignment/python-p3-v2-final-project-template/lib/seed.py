from models import create_engine, sessionmaker, Base, Client, Account, Holdings, Asset
from random import choice, randint
from faker import Faker

# Create session
engine = create_engine('sqlite:///FIMEA.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Initialize faker for the fake data
fake = Faker()

# Add data to the Client and Account tables
print("Seeding clients")
for i in range(10):
    client = Client(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        account_type=choice(['Savings', 'Checking', 'Investment'])
    )
    session.add(client)
    print("All clients seeded")

    print("Seeding Account data")
    for client in session.query(Client).all():
        for i in range(randint(1, 3)):
            account = Account(
                account_number=fake.random_int(min=10000000, max=99999999),
                account_balance=randint(1000, 100000),
                client=client
            )
            session.add(account)
    print("All Accounts seeded")

# Add data to the Assets and Holdings tables
print("Seeding Asset data")
asset_types = ['Stock', 'Bond', 'ETF']
clients = session.query(Client).all()
for i in range(10):
    asset = Asset(
        type=choice(asset_types),
        issuer_name=fake.company(),
        current_price=randint(10, 1000),
        maturity_date=fake.date_between(start_date='-1y', end_date='+1y')
    )
    # Associate a random client with the asset
    if clients:
        asset.clients.append(choice(clients))
    session.add(asset)
    print("All Assets seeded")

    print("Seeding Holdings data")
    for asset in session.query(Asset).all():
        accounts = session.query(Account).filter(Account.client_id.in_([c.id for c in asset.clients])).all()
        if accounts:
            account = choice(accounts)
            holding = Holdings(
                account=account,
                asset=asset,
                number_of_shares=randint(1, 100),
                purchase_price=randint(10, 1000),
                purchase_date=fake.date_between(start_date='-1y', end_date='today')
            )
            session.add(holding)
    print("All Holdings data seeded")

print("All data seeded")

# Commit changes and close session
session.commit()
session.close()
