from tkinter import *


# Creating a Class
class BillApp:
    # Creating Function.
    def __init__(self, root):
        self.root = root

        # Setting Resolution of the window.
        self.root.geometry("1500x800+0+0")

        # For the title of the Window.
        self.root.title("Billing Software")
        title = Label(self.root, text="Billing Software", bg="black", fg="white", font=("Times", 15, "bold"), bd=3,
                      relief=GROOVE)
        title.place(x=650, y=0, height=30, width=200)

        # For Morning Beverage.
        self.americano = IntVar()
        self.cappuccino = IntVar()
        self.milk_tea = IntVar()
        self.black_tea = IntVar()

        # For Main Dishes
        self.fried_rice = IntVar()
        self.pizza = IntVar()
        self.burger = IntVar()
        self.dumpling = IntVar()

        # For Alcoholic Drinks
        self.signature = IntVar()
        self.red_label = IntVar()
        self.jack_daniel = IntVar()
        self.vodka = IntVar()

        # For Total Price and Total Tax Varible.

        self.beverage_price = StringVar()
        self.dishes_price = StringVar()
        self.drinks_price = StringVar()

        self.beverage_price_tax = StringVar()
        self.dishes_tax = StringVar()
        self.drinks_tax = StringVar()

        # For Customer Details.

        self.c_name = StringVar()
        self.c_phon = StringVar()
        self.bill_no = StringVar()
        self.search = StringVar()

        f1 = Label(self.root, text="Customer Details", bg="Black", fg="pink", font=("times new roman", 25, "bold"))
        f1.place(x=5, y=50)

        # Adding specific name for their specific function.
        cname_lbl = Label(self.root, text="Customer Name", bg="sandy brown", font=("times", 15, "bold"))
        cname_lbl.place(x=25, y=92)

        cname_txt = Entry(self.root, width=20, textvariable=self.c_name, font="arial 15", bd=4, relief="sunken")
        cname_txt.place(x=145, y=90)

        cphn_lbl = Label(self.root, text="Customer Phone no.", bg="sandy brown", font=("times", 15, "bold"))
        cphn_lbl.place(x=470, y=92)

        cphn_txt = Entry(self.root, textvariable=self.c_phon, width=20, font="arial 15", bd=4, relief="sunken")
        cphn_txt.place(x=620, y=90)

        c_bill_lbl = Label(self.root, text="Bill no.", bg="sandy brown", font=("times", 15, "bold"))
        c_bill_lbl.place(x=940, y=92)

        c_bill_txt = Entry(self.root, width=20, textvariable=self.bill_no, font="arial 15", bd=4, relief="sunken")
        c_bill_txt.place(x=1000, y=90)

        # Adding Buttons.
        bill_btn = Button(self.root, text="Search", width=10, bd=7, font="arial 12 bold")
        bill_btn.place(x=1250, y=95, height=25, width=90)

        # Title.
        f2 = Label(self.root, text="Morning Beverages: ", bg="sandy brown", fg="black",
                   font=("times new roman", 20, "bold"))
        f2.place(x=10, y=160, width=200)

        # Adding Drinks.
        americano = Label(self.root, text="Americano", bg="sandy brown", font=("Times", 15, "bold"))
        americano.place(x=30, y=200)

        amr_text = Entry(self.root, width=10, textvariable=self.americano, bd=3, font=("times", 15), relief="sunken")
        amr_text.place(x=120, y=198)

        cappuccino = Label(self.root, text="Cappuccino", bg="sandy brown", font=("Times", 15, "bold"))
        cappuccino.place(x=30, y=250)

        cpc_text = Entry(self.root, width=10, textvariable=self.cappuccino, bd=3, font=("times", 15), relief="sunken")
        cpc_text.place(x=120, y=248)

        milk_tea = Label(self.root, text="Milk Tea", bg="sandy brown", font=("Times", 15, "bold"))
        milk_tea.place(x=30, y=300)

        mlk_text = Entry(self.root, width=10, textvariable=self.milk_tea, bd=3, font=("times", 15), relief="sunken")
        mlk_text.place(x=120, y=298)

        black_tea = Label(self.root, text="Black Tea", bg="sandy brown", font=("Times", 15, "bold"))
        black_tea.place(x=30, y=350)

        blk_text = Entry(self.root, width=10, textvariable=self.black_tea, bd=3, font=("times", 15), relief="sunken")
        blk_text.place(x=120, y=349)

        # Providing numbers.
        one = Label(self.root, text="1)", bg="sandy brown", font=("Times", 15, "bold"))
        one.place(x=10, y=200)
        two = Label(self.root, text="2)", bg="sandy brown", font=("Times", 15, "bold"))
        two.place(x=10, y=250)
        three = Label(self.root, text="3)", bg="sandy brown", font=("Times", 15, "bold"))
        three.place(x=10, y=300)
        four = Label(self.root, text="4)", bg="sandy brown", font=("Times", 15, "bold"))
        four.place(x=10, y=350)

        # Title.
        f3 = Label(self.root, text="Main Dishes: ", bg="sandy brown", fg="black", font=("times new roman", 20, "bold"))
        f3.place(x=300, y=160, width=200)

        # Adding Dishes.
        fried_rice = Label(self.root, text="Fried Rice", bg="sandy brown", font=("Times", 15, "bold"))
        fried_rice.place(x=350,y=200)

        frc_text = Entry(self.root, width=10, textvariable=self.fried_rice, bd=3, font=("times", 15), relief="sunken")
        frc_text.place(x=440, y=198)

        pizza = Label(self.root, text="Pizza", bg="sandy brown", font=("Times", 15, "bold"))
        pizza.place(x=350, y=250)

        piz_text = Entry(self.root, width=10, textvariable=self.pizza, bd=3, font=("times", 15), relief="sunken")
        piz_text.place(x=440, y=248)

        burger = Label(self.root, text="Burger", bg="sandy brown", font=("Times", 15, "bold"))
        burger.place(x=350, y=300)

        brg_text = Entry(self.root, width=10, textvariable=self.burger, bd=3, font=("times", 15), relief="sunken")
        brg_text.place(x=440, y=298)

        dumpling = Label(self.root, text="Dumpling", bg="sandy brown", font=("Times", 15, "bold"))
        dumpling.place(x=350, y=350)

        dmp_txt = Entry(self.root, width=10, textvariable=self.dumpling, bd=3, font=("times", 15), relief="sunken")
        dmp_txt.place(x=440, y=349)

        # Providing numbers.
        one_ = Label(self.root, text="1)", bg="sandy brown", font=("Times", 15, "bold"))
        one_.place(x=330, y=200)
        two_ = Label(self.root, text="2)", bg="sandy brown", font=("Times", 15, "bold"))
        two_.place(x=330, y=250)
        three_ = Label(self.root, text="3)", bg="sandy brown", font=("Times", 15, "bold"))
        three_.place(x=330, y=300)
        four_ = Label(self.root, text="4)", bg="sandy brown", font=("Times", 15, "bold"))
        four_.place(x=330, y=350)

        f3 = Label(self.root, text="Alcoholic Drinks:", bg="sandy brown", fg="black",font=("times", 20, "bold"))
        f3.place(x=500, y=160, width=400)

        # Adding Hard Drinks.
        signature = Label(self.root, text="Signature", bg="sandy brown", font=("Times", 15, "bold"))
        signature.place(x=660,y=200)

        sgn_txt = Entry(self.root, width=10, textvariable=self.signature, bd=3, font=("times", 15), relief="sunken")
        sgn_txt.place(x=750, y=198)

        red_label = Label(self.root, text="Red Label", bg="sandy brown", font=("Times", 15, "bold"))
        red_label.place(x=660, y=250)

        rdb_txt = Entry(self.root, width=10, textvariable=self.red_label, bd=3, font=("times", 15), relief="sunken")
        rdb_txt.place(x=750, y=248)

        jd = Label(self.root, text="Jack Daniel", bg="sandy brown", font=("Times", 15, "bold"))
        jd.place(x=660, y=300)

        jd_text = Entry(self.root, width=10, textvariable=self.jack_daniel, bd=3, font=("times", 15), relief="sunken")
        jd_text.place(x=750, y=298)

        vodka = Label(self.root, text="Vodka", bg="sandy brown", font=("Times", 15, "bold"))
        vodka.place(x=660, y=350)

        vdk_text = Entry(self.root, width=10, textvariable=self.vodka, bd=3, font=("times", 15), relief="sunken")
        vdk_text.place(x=750, y=349)

        # Providing numbers.
        one__ = Label(self.root, text="1)", bg="sandy brown", font=("Times", 15, "bold"))
        one__.place(x=640, y=200)
        two__ = Label(self.root, text="2)", bg="sandy brown", font=("Times", 15, "bold"))
        two__.place(x=640, y=250)
        three__ = Label(self.root, text="3)", bg="sandy brown", font=("Times", 15, "bold"))
        three__.place(x=640, y=300)
        four__ = Label(self.root, text="4)", bg="sandy brown", font=("Times", 15, "bold"))
        four__.place(x=640, y=350)

        # For billing.
        f5 = Frame(self.root, bd=10, relief="groove")
        f5.place(x=910, y=150, width=450, height=480)
        bill_title = Label(f5, text="Bill Area", font=("arial", 15, "bold"), bd=7, relief="groove").pack(fill=X)
        scrol_y = Scrollbar(f5, orient=VERTICAL)
        self.txtarea = Text(f5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # Bill Menu Frame.
        f6 = LabelFrame(self.root, bd=10, relief="groove", bg="sandy brown", text="Bill Menu", font="times 20 bold")
        f6.place(x=0, y=630, relwidth=1, height=140)

        m1 = Label(f6, text="Total Beverage Price", bg="sandy brown", font=("Times", 15, "bold"))
        m1.grid(row=0, column=0, padx=20, pady=1, sticky="W")

        m1_e = Entry(f6, width=18, textvariable=self.beverage_price, font="arial 15", bd=3, relief="sunken")
        m1_e.grid(row=0, column=1, padx=10, pady=1)

        m2 = Label(f6, text="Total Dishes Price", bg="sandy brown", font=("Times", 15, "bold"))
        m2.grid(row=1, column=0, padx=20, pady=1, sticky="W")

        m2_e = Entry(f6, width=18, textvariable=self.dishes_price, font="arial 15", bd=3, relief="sunken")
        m2_e.grid(row=1, column=1, padx=10, pady=1)

        m3 = Label(f6, text="Total Alcohol  Price", bg="sandy brown", font=("Times", 15, "bold"))
        m3.grid(row=2, column=0, padx=20, pady=1, sticky="W")

        m3_e = Entry(f6, width=18, textvariable=self.drinks_price, font="arial 1", bd=3, relief="sunken")
        m3_e.place(x=198, y=67, width=176, height=30)

        m4 = Label(f6, text="Total Beverage Tax", bg="sandy brown", font=("Times", 15, "bold"))
        m4.grid(row=0, column=3, padx=20, pady=1, sticky="W")

        m4_e = Entry(f6, width=18, textvariable=self.beverage_price_tax, font="arial 15", bd=3, relief="sunken")
        m4_e.grid(row=0, column=4, padx=10, pady=1)

        m5 = Label(f6, text="Total Dishes Tax", bg="sandy brown", font=("Times", 15, "bold"))
        m5.grid(row=1, column=3, padx=20, pady=1, sticky="W")

        m5_e = Entry(f6, width=18, textvariable=self.dishes_tax, font="arial 15", bd=3, relief="sunken")
        m5_e.grid(row=1, column=4, padx=10, pady=1)

        m6 = Label(f6, text="Total Alcohol Tax", bg="sandy brown", font=("Times", 15, "bold"))
        m6.grid(row=2, column=3, padx=20, pady=1, sticky="W")

        m6_e = Entry(f6, width=18, textvariable=self.drinks_tax, font="arial 1", bd=3, relief="sunken")
        m6_e.place(x=572, y=67, width=176, height=30)

        btn_f = Frame(f6, bd=7, relief="groove")
        btn_f.place(x=755, y=-3, width=660, height=105)

        total_btn = Button(btn_f, text="Total", pady=20, width=15, font=("arial", 15, "bold") , command = self.total)
        total_btn.grid(row=0, column=0, padx=5, pady=10)

        gbill_btn = Button(btn_f, text="Generate Bill", pady=20, width=20, font=("arial", 15, "bold"))
        gbill_btn.grid(row=0, column=1, padx=5, pady=10)

        clear_btn = Button(btn_f, text="Clear", pady=20, width=15, font=("arial", 15, "bold"))
        clear_btn.grid(row=0, column=2, padx=5, pady=10)

        exit_btn = Button(btn_f, text="Exit", pady=20, width=15, font=("arial", 15, "bold"), command=root.destroy)
        exit_btn.grid(row=0, column=3, padx=5, pady=10)

    def total(self):
        self.total_beverage_price = float(
            (self.americano.get()*40)+
            (self.cappuccino.get()*140)+
            (self.milk_tea.get()*90)+
            (self.black_tea.get()*70)
                                    )

        self.beverage_price.set(str(self.total_beverage_price))

        self.total_dishes_price = float(
            (self.fried_rice.get() * 40) +
            (self.pizza.get() * 140) +
            (self.burger.get() * 90) +
            (self.dumpling.get() * 70)
        )

        self.dishes_price.set(str(self.total_dishes_price))

        self.total_drinks_price = float(
            (self.signature.get() * 40) +
            (self.red_label.get() * 140) +
            (self.jack_daniel.get() * 90) +
            (self.vodka.get() * 70)
        )

        self.drinks_price.set(str(self.total_drinks_price))







# Creating Window.
root = Tk()
root.configure(bg="sandy brown")
obj = BillApp(root)

# Running window in the mainloop.
root.mainloop()
