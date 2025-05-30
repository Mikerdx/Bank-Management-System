# Bank Management System (CLI-Based)

This is a Python-based Bank Management System using SQLAlchemy ORM and a Command-Line Interface (CLI).
It allows users to manage bank accounts, handle transactions and assign financial products

## PROJECT STRUCTURE 
lib/
├── cli.py 
├── helpers.py
├── models/
│ ├── init.py 
│ ├── account.py 
│ ├── user_profile.py 
│ ├── bank_branch.py 
│ ├── transaction.py 
│ ├── product.py 
│ └── account_product.py 
└── seed.py 

## KEY FEATURES
-  Create and manage user accounts and profiles
-  Deposit and withdraw money
-  View transactions for specific users
-  Manage bank branches
-  Manage financial products 
-  Assign products to accounts 
-  Seed database with realistic fake data

## TECHNOLOGIES USED 
**Python**
**SQLAlchemy**
**SQLite**
**Faker**
**getpass**
**Alembic**

##  How to run 
`pipenv install`
`pipenv python3 lib.seed`-to create fake data
`pipenv python3 lib.cli`- to open menu options

### Relationships Overview
Account ↔ UserProfile (One-to-One)
Account ↔ BankBranch (Many-to-One)
Account ↔ Transaction (One-to-Many)
Account ↔ Product (Many-to-Many via account_product)

# LINKS
To demo -- **python -m lib.cli**
Dbdiagram.io -- **https://dbdiagram.io/d/68347bd26980ade2eb70f4b3**
<video controls src="video2106508728.mp4" title="Title"></video>

# Author
Name:Mike Bett
GitHub: Mikerdx
Email: mike.bett@student.moringaschool.com

# License
This project is licensed under the MIT License.