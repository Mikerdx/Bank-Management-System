#creation of fake entities
from faker import Faker
from lib.models import Session, engine, Base
from lib.models.account import Account
from lib.models.user_profile import UserProfile
from lib.models.bank_branch import BankBranch
from lib.models.product import Product
from lib.models.transaction import Transaction
from datetime import datetime
import random

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

session = Session()
fake = Faker()

branches = []
for _ in range(3):
    branch = BankBranch(name=fake.company(), location=fake.city())
    branches.append(branch)
    session.add(branch)
    
products = []
for _ in range(5):
    product = Product(name=fake.bs().capitalize(), description=fake.catch_phrase())
    products.append(product)
    session.add(product)
    
for _ in range(10):
    profile = UserProfile(
        full_name=fake.name(),
        email=fake.email(),
        phone=fake.phone_number(),
        address=fake.address()
    )
    branch = random.choice(branches)
    account = Account(
        user_name=fake.user_name(),
        user_pw="pass1234",
        balance=random.randint(100, 5000),
        profile=profile,
        branch=branch
    )
    for _ in range(3):
        tx_type = random.choice(['deposit', 'withdrawal'])
        amount = random.randint(10, 1000)
        tx = Transaction(type=tx_type, amount=amount, timestamp=datetime.utcnow(), account=account)
        session.add(tx)

    account.products.append(random.choice(products))

    session.add(account)

session.commit()
print("Fake data seeded successfully.")
