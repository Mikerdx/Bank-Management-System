# lib/cli.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.helpers import (
    create_account, deposit, withdraw, view_accounts, view_transactions,
    add_bank_branch, add_product, assign_product_to_account
)

from lib.models import Base, engine

Base.metadata.create_all(engine)

def menu():
    print("\nBank CLI")
    print("1. Open Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View All Accounts")
    print("5. View Transactions")
    print("6. Add Bank Branch")
    print("7. Add Product")
    print("8. Assign Product to Account")
    print("0. Exit")

def main():
    while True:
        menu()
        choice = input("Choose an option: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            view_accounts()
        elif choice == "5":
            view_transactions()
        elif choice == "6":
            add_bank_branch()
        elif choice == "7":
            add_product()
        elif choice == "8":
            assign_product_to_account()
        elif choice == "0":
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
