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