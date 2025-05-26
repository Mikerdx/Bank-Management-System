# main.py
import tkinter as tk
from tkinter import messagebox
import bankdb

class BankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Management")
        self.root.geometry("800x600")

        bankdb.create_tables()

        tk.Label(root, text="Bank Account Management System", font=("Arial", 24, "bold"), bg="lightgreen").pack(fill="x")

        btn_frame = tk.Frame(root, bg="lightgrey")
        btn_frame.pack(pady=40)

        tk.Button(btn_frame, text="Open Account", font=("Arial", 16), command=self.open_account).grid(row=0, column=0, padx=20, pady=10)
        tk.Button(btn_frame, text="Deposit", font=("Arial", 16), command=self.deposit).grid(row=1, column=0, padx=20, pady=10)
        tk.Button(btn_frame, text="Withdraw", font=("Arial", 16), command=self.withdraw).grid(row=2, column=0, padx=20, pady=10)

    def open_account(self):
        win = tk.Toplevel(self.root)
        win.title("Open Account")
        win.geometry("400x300")

        tk.Label(win, text="Username").grid(row=0, column=0, padx=10, pady=10)
        u_name = tk.Entry(win)
        u_name.grid(row=0, column=1)

        tk.Label(win, text="Password").grid(row=1, column=0, padx=10, pady=10)
        pw = tk.Entry(win, show="*")
        pw.grid(row=1, column=1)

        tk.Label(win, text="Confirm Password").grid(row=2, column=0, padx=10, pady=10)
        confirm = tk.Entry(win, show="*")
        confirm.grid(row=2, column=1)

        def create():
            if pw.get() != confirm.get():
                messagebox.showerror("Error", "Passwords do not match!")
                return
            try:
                bankdb.insert_user(u_name.get(), pw.get())
                messagebox.showinfo("Success", "Account created successfully!")
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Could not create account: {e}")

        tk.Button(win, text="Create", command=create).grid(row=3, column=0, columnspan=2, pady=20)

    def deposit(self):
        win = tk.Toplevel(self.root)
        win.title("Deposit")
        win.geometry("400x200")

        tk.Label(win, text="Username").grid(row=0, column=0, padx=10, pady=10)
        u_name = tk.Entry(win)
        u_name.grid(row=0, column=1)

        tk.Label(win, text="Amount").grid(row=1, column=0, padx=10, pady=10)
        amount = tk.Entry(win)
        amount.grid(row=1, column=1)

        def deposit_action():
            try:
                amt = int(amount.get())
                balance = bankdb.get_balance(u_name.get())
                if balance is None:
                    raise Exception("User not found")
                bankdb.update_balance(u_name.get(), balance + amt)
                messagebox.showinfo("Success", "Deposit successful!")
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(win, text="Deposit", command=deposit_action).grid(row=2, column=0, columnspan=2, pady=20)

    def withdraw(self):
        win = tk.Toplevel(self.root)
        win.title("Withdraw")
        win.geometry("400x250")

        tk.Label(win, text="Username").grid(row=0, column=0, padx=10, pady=10)
        u_name = tk.Entry(win)
        u_name.grid(row=0, column=1)

        tk.Label(win, text="Password").grid(row=1, column=0, padx=10, pady=10)
        pw = tk.Entry(win, show="*")
        pw.grid(row=1, column=1)

        tk.Label(win, text="Amount").grid(row=2, column=0, padx=10, pady=10)
        amount = tk.Entry(win)
        amount.grid(row=2, column=1)

        def withdraw_action():
            try:
                amt = int(amount.get())
                creds = bankdb.get_user_credentials(u_name.get())
                if not creds:
                    raise Exception("User not found")
                if creds[0] != pw.get():
                    raise Exception("Incorrect password")
                if creds[1] < amt:
                    raise Exception("Insufficient balance")
                bankdb.update_balance(u_name.get(), creds[1] - amt)
                messagebox.showinfo("Success", "Withdrawal successful!")
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(win, text="Withdraw", command=withdraw_action).grid(row=3, column=0, columnspan=2, pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()
