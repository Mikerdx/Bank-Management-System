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
        
        openAcBtn = tk.Button(mainFrame, width=20,text="open account",bg="light blue", bd=3, relief="raised", font=("Arial",20,"bold"))
        openAcBtn.grid(row=0, column=0, padx=40, pady=70)
        
        depBtn = tk.Button(mainFrame, width=20,text="Deposit",bg="light blue", bd=3, relief="raised", font=("Arial",20,"bold"))
        depBtn.grid(row=1, column=0, padx=40, pady=70)
 
 
        
root=tk.Tk()
obj = bank(root)
root.mainloop()