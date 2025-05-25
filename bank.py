import tkinter as tk

class bank():
    def __init__(self,root):
        self.root = root
        self.root.title("Bank Management")
        
        scrn_width = self.root.winfo_screenwidth()
        scrn_height = self.root.winfo_screenheight()
        
        self.root.geometry(f"{scrn_width}x{scrn_height}+0+0")
 
        
root=tk.Tk()
obj = bank(root)
root.mainloop()