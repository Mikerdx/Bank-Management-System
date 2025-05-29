# lib/helpers.py
from getpass import getpass
from datetime import datetime
from lib.models import Session
from lib.models.account import Account
from lib.models.transaction import Transaction
from lib.models.user_profile import UserProfile
from lib.models.bank_branch import BankBranch
from lib.models.product import Product

#Create a new user account along with a user profile and links it to a bank branch.
def create_account():
    session = Session()
    username = input("Enter username: ")
    pw = getpass("Enter password: ")
    confirm = getpass("Confirm password: ")

    if pw != confirm:
        print("Passwords do not match.")
        return

    if session.query(Account).filter_by(user_name=username).first():
        print("Account already exists.")
        return

    full_name = input("Full name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    address = input("Address: ")

    profile = UserProfile(full_name=full_name, email=email, phone=phone, address=address)
    session.add(profile)
    session.flush()  

    # List branches and linking 
    branches = session.query(BankBranch).all()
    if not branches:
        print("No bank branches available. Please add one first.")
        session.rollback()
        return
    print("Available bank branches:")
    for b in branches:
        print(f"{b.id}: {b.name} - {b.location}")
    branch_id = int(input("Choose branch by ID: "))
    branch = session.query(BankBranch).get(branch_id)
    if not branch:
        print("Invalid branch.")
        session.rollback()
        return

    account = Account(user_name=username, user_pw=pw, profile=profile, branch=branch)
    session.add(account)
    session.commit()
    print("Account created successfully.")

def deposit():
    session = Session()
    username = input("Username: ")
    acc = session.query(Account).filter_by(user_name=username).first()
    if not acc:
        print("Account not found.")
        return
    amount = int(input("Amount to deposit: "))
    acc.balance += amount
    tx = Transaction(account=acc, type='deposit', amount=amount, timestamp=datetime.utcnow())
    session.add(tx)
    session.commit()
    print("Deposit successful.")

def withdraw():
    session = Session()
    username = input("Username: ")
    pw = getpass("Password: ")
    acc = session.query(Account).filter_by(user_name=username, user_pw=pw).first()
    if not acc:
        print("Invalid credentials.")
        return
    amount = int(input("Amount to withdraw: "))
    if acc.balance < amount:
        print("Insufficient funds.")
        return
    acc.balance -= amount
    tx = Transaction(account=acc, type='withdrawal', amount=amount, timestamp=datetime.utcnow())
    session.add(tx)
    session.commit()
    print("Withdrawal successful.")

def view_accounts():
    session = Session()
    accounts = session.query(Account).all()
    for acc in accounts:
        profile = acc.profile
        branch = acc.branch
        print(f"User: {acc.user_name}, Balance: {acc.balance}, Branch: {branch.name if branch else 'N/A'}, Profile: {profile.full_name if profile else 'N/A'}")

def view_transactions():
    session = Session()
    username = input("Enter username to view transactions: ")
    acc = session.query(Account).filter_by(user_name=username).first()
    if not acc:
        print("Account not found.")
        return
    txs = session.query(Transaction).filter_by(account_id=acc.id).order_by(Transaction.timestamp.desc()).all()
    for tx in txs:
        print(f"{tx.timestamp}: {tx.type.capitalize()} of {tx.amount}")

def add_bank_branch():
    session = Session()
    name = input("Branch name: ")
    location = input("Location: ")
    branch = BankBranch(name=name, location=location)
    session.add(branch)
    session.commit()
    print("Branch added.")

def add_product():
    session = Session()
    name = input("Product name: ")
    description = input("Description: ")
    product = Product(name=name, description=description)
    session.add(product)
    session.commit()
    print("Product added.")

def assign_product_to_account():
    session = Session()
    username = input("Username: ")
    acc = session.query(Account).filter_by(user_name=username).first()
    if not acc:
        print("Account not found.")
        return

    products = session.query(Product).all()
    if not products:
        print("No products available.")
        return

    print("Available products:")
    for p in products:
        print(f"{p.id}: {p.name}")
    product_id = int(input("Choose product by ID: "))
    product = session.query(Product).get(product_id)
    if not product:
        print("Invalid product.")
        return

    from datetime import datetime
    start_date = datetime.utcnow()
    # For simplicity, no end_date specified here
    acc.products.append(product)
    session.commit()
    print("Product assigned to account.")

def exit_program():
    print("Goodbye!")
    exit()

