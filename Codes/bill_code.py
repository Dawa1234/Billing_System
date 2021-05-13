from tkinter import *


class BillApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        title = Label(self.root, text="Billing Software", bd=3, relief=GROOVE, pady=2).pack()
        f1 = Label(self.root, text="Customer Details", font=("times new roman", 15, "bold"))
        f1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(f1, text="Customer Name").grid(row=0, column=0)


root = Tk()
obj = BillApp(root)
root.mainloop()