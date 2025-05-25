import tkinter as tk

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
        
        depBtn = tk.Button(mainFrame, width=20,text="Deposit",bg="light blue", bd=3, relief="raised", font=("Arial",20,"bold"))
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
        
        okBtn = tk.Button(self.openAcFrame,text="Ok", bg="light Blue",bd=3, relief="raised",font=("Arial",15,"bold"))
        okBtn.grid(row=3, column=0, padx=40 ,pady=120)
        
        closeBtn = tk.Button(self.openAcFrame,command=self.close_openAc,text="Close", bg="light Blue",bd=3, relief="raised",font=("Arial",15,"bold"))
        closeBtn.grid(row=3, column=1, padx=40 ,pady=120)
        
    def close_openAc(self):
        self.openAcFrame.destroy()
 
 
 
        
root=tk.Tk()
obj = bank(root)
root.mainloop()