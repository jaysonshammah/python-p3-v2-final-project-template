from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey

Base = declarative_base()

class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    email = Column(String(), unique=True)
    account_type = Column(String())
    accounts = relationship('Account', back_populates='client')

class Account(Base):
    __tablename__ = 'profile'

    id = Column(Integer(), primary_key=True)
    account_number = Column(String())
    account_balance = Column(Float())
    client_id = Column(Integer(), ForeignKey('clients.id'))
    client = relationship('Client', back_populates='accounts')
    holdings = relationship('Holdings', back_populates='account')
    
class Asset(Base):
    __tablename__ = 'assets'

    id = Column(Integer(), primary_key=True)
    type = Column(String())
    issuer_name = Column(String())
    current_price = Column(Float())
    maturity_date = Column(Date())
    holdings = relationship('Holdings', back_populates='asset')
    clients = relationship('Client', secondary='holdings', overlaps="holdings")
    
class Holdings(Base):
    __tablename__ = 'holdings'

    id = Column(Integer(), primary_key=True)
    account_id = Column(Integer(), ForeignKey('profile.id')) 
    asset_id = Column(Integer(), ForeignKey('assets.id'))
    number_of_shares = Column(Float())
    purchase_price = Column(Float())
    purchase_date = Column(Date())
    account = relationship('Account', back_populates='holdings')
    asset = relationship('Asset', back_populates='holdings', overlaps="clients")
    client_id = Column(Integer(), ForeignKey('clients.id'))
