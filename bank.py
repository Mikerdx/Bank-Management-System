import tkinter as tk
from tkinter import messagebox
import pymysql
class bank():
    def __init__(self,root):
        self.root = root
        self.root.title("Bank Management")
        
        scrn_width = self.root.winfo_screenwidth()
        scrn_height = self.root.winfo_screenheight()
        
        self.root.geometry(f"{scrn_width}x{scrn_height}+0+0")
        
        mainLabel = tk.Label(self.root, text = "Bank Account Management System", font=("Arial",40,"bold"),bg="light green", bd=5, relief="groove")
        mainLabel.pack(side="top", fill="x")
        
        mainFrame = tk.Frame(self.root, bg="light grey", bd=5, relief="ridge")
        mainFrame.place(x=400, y=90, width=450, height=550)
        
        openAcBtn = tk.Button(mainFrame,command=self.openAc, width=20,text="open account",bg="light blue", bd=3, relief="raised", font=("Arial",20,"bold"))
        openAcBtn.grid(row=0, column=0, padx=40, pady=65)
        
        depBtn = tk.Button(mainFrame, width=20,text="Deposit",command=self.deposit_fun,bg="light blue", bd=3, relief="raised", font=("Arial",20,"bold"))
        depBtn.grid(row=1, column=0, padx=40, pady=65)
        
        wdBtn = tk.Button(mainFrame, width=20,text="Withdraw",bg="light blue", bd=3, relief="raised", font=("Arial",20,"bold"))
        wdBtn.grid(row=2, column=0, padx=40, pady=65)
 
    def openAc(self):
        self.openAcFrame = tk.Frame(self.root, bg="light grey", bd=5, relief="ridge")
        self.openAcFrame.place(x=400, y=90, width=450, height=550)
        
        uNameLabel = tk.Label(self.openAcFrame, text="User Name:", bg="light grey", font=("Arial",15,"bold"))
        uNameLabel.grid(row=0, column=0, padx=20, pady=30)
        self.uNameInput = tk.Entry(self.openAcFrame, width=15, font=("Arial",15))
        self.uNameInput.grid(row=0, column=1, padx=5, pady=30)
        
        uPWLabel = tk.Label(self.openAcFrame, text="User Password:", bg="light grey", font=("Arial",15,"bold"))
        uPWLabel.grid(row=0, column=0, padx=20, pady=30)
        self.uPWInput = tk.Entry(self.openAcFrame, width=15, font=("Arial",15))
        self.uPWInput.grid(row=0, column=1, padx=5, pady=30)
        
        confirmLabel = tk.Label(self.openAcFrame, text="Confirm Password:", bg="light grey", font=("Arial",15,"bold"))
        confirmLabel.grid(row=0, column=0, padx=20, pady=30)
        self.confirmInput = tk.Entry(self.openAcFrame, width=15, font=("Arial",15))
        self.confirmInput.grid(row=2, column=1, padx=5, pady=30)
        
        okBtn = tk.Button(self.openAcFrame,self.insert,text="Ok", bg="light Blue",bd=3, relief="raised",font=("Arial",15,"bold"))
        okBtn.grid(row=3, column=0, padx=40 ,pady=120)
        
        closeBtn = tk.Button(self.openAcFrame,command=self.close_openAc,text="Close", bg="light Blue",bd=3, relief="raised",font=("Arial",15,"bold"))
        closeBtn.grid(row=3, column=1, padx=40 ,pady=120)
        
    def close_openAc(self):
        self.openAcFrame.destroy()
    
    def insert(self):
        uName = self.uNameInput.get()
        uPW = self.uPWInput.get()
        confirm = self.confirmInput.get()
        
        if uPW == confirm:
            con = pymsql.connect(host="localhost", user="root",password="admin",database="bankdb")
            cur = con.cursor()
            cur.execute("Insert into account (userName, userPW) values(%s, %s)",(uName,uPW))
            con.commit()
            con.close()
            tk.messagebox.showinfo("success","Account opened successfully!")
            self.clear()
        else:
            tk.messagebox.showerror("Error","Both Passwords Should be Same!")
            self.clear
            
    def clear(self):
        self.uNameInput.delete(0,tk.END)
        self.uPWInput.delete(0,tk.END)
        self.confirmInput.delete(0,tk.END)
 
    def deposit(self):
        self.depositFrame = tk.Frame(self.root, bg="light grey", bd=5, relief="ridge")
        self.depositFrame.place(x=400, y=90, width=450, height=550)
        
        NameLabel = tk.Label(self.depositFrame, text="User Name:", bg="light grey", font=("Arial",15,"bold"))
        NameLabel.grid(row=0, column=0, padx=20, pady=30)
        self.NameInput = tk.Entry(self.depositFrame, width=15, font=("Arial",15))
        self.NameInput.grid(row=0, column=1, padx=5, pady=30)
        
        amountLabel = tk.Label(self.depositFrame, text="Enter Amount:", bg="light grey", font=("Arial",15,"bold"))
        amountLabel.grid(row=1, column=0, padx=20, pady=30)
        self.amountInput = tk.Entry(self.depositFrame, width=15, font=("Arial",15))
        self.amountInput.grid(row=1, column=1, padx=5, pady=30)
        
        okBtn = tk.Button(self.depositFrame,command=self.deposit_fun,text="Deposit", bg="light Blue",bd=3, relief="raised",font=("Arial",15,"bold"))
        okBtn.grid(row=2, column=0, padx=40 ,pady=150)
        
        closeBtn = tk.Button(self.depositFrame,command=self.close_deposit,text="Close", bg="light Blue",bd=3, relief="raised",font=("Arial",15,"bold"))
        closeBtn.grid(row=2, column=1, padx=40 ,pady=150)
        
    def deposit_fun(self):
        name = self.NameInput.get()
        amount = int(self.amountInput.get())
        
        con = pymsql.connect(host="localhost", user="root",password="admin",database="bankdb")
        cur = con.cursor()
        cur.execute("select balance from account where userName=%s", name)
        data= cur.fetchone()
        if data:
            balance=data[0]
            if data[0] is None:
                balance=0
            update = balance +amount
            cur.execute("update account set balance=%s where userName=%s", (update,name))
            con.commit()
            con.close()
            tk.messagebox.showinfo("success","Operation was successful!")
        else:
            tk.messagebox.showerror("Error","Invalid Customer Name!")
        
    def close_deposit(self):
        self.depositFrame.destroy()
    
    def  wd(self):
        self.wdFrame = tk.Frame(self.root, bg="light grey", bd=5, relief="ridge")
        self.wdFrame.place(x=400, y=90, width=450, height=550)
        
        cNameLabel = tk.Label(self.wdFrame, text="User Name:", bg="light grey", font=("Arial",15,"bold"))
        cNameLabel.grid(row=0, column=0, padx=20, pady=30)
        self.cNameInput = tk.Entry(self.wdFrame, width=15, font=("Arial",15))
        self.cNameInput.grid(row=0, column=1, padx=5, pady=30)
        
        cPWLabel = tk.Label(self.wdFrame, text="User Password:", bg="light grey", font=("Arial",15,"bold"))
        cPWLabel.grid(row=0, column=0, padx=20, pady=30)
        self.cPWInput = tk.Entry(self.wdFrame, width=15, font=("Arial",15))
        self.cPWInput.grid(row=0, column=1, padx=5, pady=30)
        
        wdLabel = tk.Label(self.wdFrame, text="Enter Amount:", bg="light grey", font=("Arial",15,"bold"))
        wdLabel.grid(row=0, column=0, padx=20, pady=30)
        self.wdInput = tk.Entry(self.wdFrame, width=15, font=("Arial",15))
        self.wdInput.grid(row=2, column=1, padx=5, pady=30)
        
        okBtn = tk.Button(self.wdFrame,self.,text="Withdraw", bg="light Blue",bd=3, relief="raised",font=("Arial",15,"bold"))
        okBtn.grid(row=3, column=0, padx=40 ,pady=120)
        
        closeBtn = tk.Button(self.wdFrame,command=self.close_wd,text="Close", bg="light Blue",bd=3, relief="raised",font=("Arial",15,"bold"))
        closeBtn.grid(row=3, column=1, padx=40 ,pady=120)
        
    def wd_fun(self):
        name = self.cNameInput.get()
        pw = self.cPWInput.get()
        amount= int(self.wdInput.get())
        
        con = pymsql.connect(host="localhost", user="root",password="admin",database="bankdb")
        cur = con.cursor()
        cur.execute("select userPW, balance from account where userName=%s",name)
        data = cur.fetchone()
        if data:
            if data[0]==pw:
                if data[1] >= amount:
                    update = data[1] -amount
                    cur.execute("Update account set balance=%s ")
                else:
                    tk.messagebox.showerror("Error","Insufficient balance!")
                
            else:
                tk.messagebox.showerror("Error","Invalid Customer Password!")
        else:
            tk.messagebox.showerror("Error","Invalid Customer Name!")
            
        
        
        
        

    def close_wd(self):
        self.wdFrame.destroy()
    
        
        
root=tk.Tk()
obj = bank(root)
root.mainloop()