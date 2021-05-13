from tkinter import *


class BillApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x800+0+0")
        self.root.title("Billing Software")
        title = Label(self.root, text="Billing Software", bg = "black",fg = "white",font=("Times", 15, "bold"), bd=3, relief=GROOVE)
        title.place(x=650, y=0, height=30, width=200)
        f1 = Label(self.root, text="Customer Details", bg="Black", fg="pink", font=("times new roman", 25, "bold"))
        f1.place(x=5, y=50)

        cname_lbl = Label(self.root, text="Customer Name", bg="sandy brown", font=("times", 15, "bold")).place(x=25, y = 92)
        cname_txt = Entry(self.root, width=20, font="arial 15", bd=4, relief="sunken").place(x=145, y=90)

        cphn_lbl = Label(self.root, text="Customer Phone no.", bg="sandy brown", font=("times", 15, "bold")).place(x=470, y = 92)
        cphn_txt = Entry(self.root, width=20, font="arial 15", bd=4, relief="sunken").place(x=620, y=90)

        c_bill_lbl = Label(self.root, text="Bill no.", bg="sandy brown", font=("times", 15, "bold")).place(x=940, y = 92)
        c_bill_txt = Entry(self.root, width=20, font="arial 15", bd=4, relief="sunken").place(x=1000 , y=90)

        bill_btn = Button(self.root , text = "Search" , width = 10 , bd = 7 , font = "arial 12 bold")
        bill_btn.place(x = 1250, y = 95  , height = 25,width= 90)

        f2 = Label(self.root, text="Morning Beverages: ", bg="sandy brown", fg="black", font=("times new roman", 15, "bold"))
        f2.place(x=10, y=130 , width = 140)

        americano = Label(self.root, text = "Americano" ,bg = "sandy brown" , font =("Times",15,"bold")).place(x = 30, y = 170)
        amr_text = Entry(self.root, width = 10 ,bd = 3, font =("times" , 15 ),relief = "sunken").place(x = 120, y =168)

        cappuccino = Label(self.root, text = "Cappuccino" ,bg = "sandy brown" , font =("Times",15,"bold")).place(x = 30, y = 220)
        cpc_text = Entry(self.root, width = 10 ,bd = 3, font =("times" , 15 ),relief = "sunken").place(x = 120, y =218)

        milk_tea = Label(self.root, text = "Milk Tea" ,bg = "sandy brown" , font =("Times",15,"bold")).place(x = 30, y = 270)
        mlk_text = Entry(self.root, width = 10 ,bd = 3, font =("times" , 15 ),relief = "sunken").place(x = 120, y =268)

        black_tea = Label(self.root, text = "Black Tea" ,bg = "sandy brown" , font =("Times",15,"bold")).place(x = 30, y = 320)
        blk_text = Entry(self.root, width = 10 ,bd = 3, font =("times" , 15 ),relief = "sunken").place(x = 120, y =319)

root = Tk()
root.configure(bg="sandy brown")
obj = BillApp(root)
root.mainloop()
