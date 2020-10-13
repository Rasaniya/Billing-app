from tkinter import*
import math,random,os
from tkinter import messagebox

class Bill_App():
    def __init__(self,root):
        self.root=root #initialize the root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #=====================variable cosmetic

        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.hair_sh=IntVar()
        self.hair_gel=IntVar()
        self.body_loshan=IntVar()

        #=====variable grosary

        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.weate=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()

        # =====variable cold drink

        self.cock=IntVar()
        self.funta=IntVar()
        self.maza=IntVar()
        self.thumbs_up=IntVar()
        self.sprite=IntVar()
        self.fruity=IntVar()

        #===== prise and tax

        self.cosmetic_price=StringVar()
        self.grosary_price=StringVar()
        self.colddrink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grosary_tax=StringVar()
        self.colddrink_tax=StringVar()

        #======customer

        self.cname=StringVar()
        self.cphone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()



        #==============Customer detail frame
        F1=LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=70,relwidth=1)

        cst_name = Label(F1,text="Customer Name",font=("times new roman",15,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=20,pady=5)
        cst_txt = Entry(F1,width=15,font=("arial 15"),textvariable=self.cname,bd=7,relief=SUNKEN).grid(row=0,column=1,pady=10)

        cst_phone = Label(F1, text="Phone Number", font=("times new roman", 15, "bold"), bg=bg_color, fg="white").grid(row=0, column=2, padx=20, pady=5)
        cst_phone = Entry(F1, width=15, font=("arial 15"),textvariable=self.cphone,bd=7, relief=SUNKEN).grid(row=0, column=3, pady=10)

        cst_bill = Label(F1, text="Bill Number", font=("times new roman", 15, "bold"), bg=bg_color, fg="white").grid(row=0, column=4, padx=20, pady=5)
        cst_bill = Entry(F1, width=15, font=("arial 15"),textvariable=self.bill_no,bd=7, relief=SUNKEN).grid(row=0, column=5, pady=10)

        bill_btn = Button(F1,text="Search",command=self.find_bill,font=("arial 12 bold"),width=10,bd=7).grid(row=0,column=6,padx=10,pady=10)

    #===================== Cosmetic Frame

        F2 = LabelFrame(self.root,text="Cosmetic",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=0, y=170, width=325, height=380)

        bth_lbl = Label(F2,text="Bath Soup",font=("times new roman", 16, "bold"),bg=bg_color,fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        bth_txt = Entry(F2,width=10,font=("times new roman", 16, "bold"),textvariable=self.soap,bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        face_cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        face_cream_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"),textvariable=self.face_cream,bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        face_wash_lbl = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        face_wash_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"),textvariable=self.face_wash,bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10, pady=10)

        hair_s_lbl = Label(F2, text="Hair Shampoo", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        hair_s_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), textvariable=self.hair_sh,bd=5, relief=SUNKEN).grid(row=3, column=1,padx=10, pady=10)

        hair_gel_lbl = Label(F2, text="Hair Gel", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        hair_gel_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), textvariable=self.hair_gel,bd=5, relief=SUNKEN).grid(row=4, column=1,padx=10, pady=10)

        body_l_lbl = Label(F2, text="Body Loshan", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        body_l_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), textvariable=self.body_loshan,bd=5, relief=SUNKEN).grid(row=5, column=1,padx=10, pady=10)

    #===================== Grosary

        F3 = LabelFrame(self.root,text="Grosary",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=325, y=170, width=325, height=380)

        rice_lbl = Label(F3,text="Rice",font=("times new roman", 16, "bold"),bg=bg_color,fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        rice_txt = Entry(F3,width=10,font=("times new roman", 16, "bold"),textvariable=self.rice,bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        food_oil_lbl = Label(F3, text="Food Oil", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        food_oil_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"), textvariable=self.food_oil,bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        daal_lbl = Label(F3, text="Daal", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        daal_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"), textvariable=self.daal,bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10, pady=10)

        weate_lbl = Label(F3, text="Weate", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        weate_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"), textvariable=self.weate,bd=5, relief=SUNKEN).grid(row=3, column=1,padx=10, pady=10)

        sugar_lbl = Label(F3, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        sugar_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"), textvariable=self.sugar,bd=5, relief=SUNKEN).grid(row=4, column=1,padx=10, pady=10)

        tea_lbl = Label(F3, text="Tea", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        tea_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"), textvariable=self.tea,bd=5, relief=SUNKEN).grid(row=5, column=1,padx=10, pady=10)

    #===================== Cold drinks Frame

        F4 = LabelFrame(self.root,text="Cold Drinks",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=650, y=170, width=325, height=380)

        cock_lbl = Label(F4,text="Cock",font=("times new roman", 16, "bold"),bg=bg_color,fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        cock_txt = Entry(F4,width=10,font=("times new roman", 16, "bold"),textvariable=self.cock,bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        funta_lbl = Label(F4, text="Funta", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        funta_txt = Entry(F4, width=10, font=("times new roman", 16, "bold"), textvariable=self.funta,bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        maza_lbl = Label(F4, text="Maza", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        maza_txt = Entry(F4, width=10, font=("times new roman", 16, "bold"), textvariable=self.maza,bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10, pady=10)

        thumbs_up_lbl = Label(F4, text="Thumbs Up", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        thumbs_up_txt = Entry(F4, width=10, font=("times new roman", 16, "bold"), textvariable=self.thumbs_up,bd=5, relief=SUNKEN).grid(row=3, column=1,padx=10, pady=10)

        sprite_lbl = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        sprite_txt = Entry(F4, width=10, font=("times new roman", 16, "bold"), textvariable=self.sprite,bd=5, relief=SUNKEN).grid(row=4, column=1,padx=10, pady=10)

        fruity_lbl = Label(F4, text="Fruity", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        fruity_txt = Entry(F4, width=10, font=("times new roman", 16, "bold"), textvariable=self.fruity,bd=5, relief=SUNKEN).grid(row=5, column=1,padx=10, pady=10)


        #======== Bill area =========
        F5 = Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=980,y=170,width=370,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #===========Button frame===
        F6=LabelFrame(self.root,text="Cosmetic",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0 , y=550, relwidth=1, height=140)
        m1_lbl=Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,font="arial 10 bold",textvariable=self.cosmetic_price,bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl = Label(F6, text="Total Grosary Price", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18, font="arial 10 bold", textvariable=self.grosary_price,bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(F6, text="Total Cold Drinks Price", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt = Entry(F6, width=18, font="arial 10 bold", textvariable=self.colddrink_price,bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        c1_lbl=Label(F6,text="Cosmetic Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,font="arial 10 bold",textvariable=self.cosmetic_tax,bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl = Label(F6, text="grosary Tax", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        c2_txt = Entry(F6, width=18, font="arial 10 bold", textvariable=self.grosary_tax,bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        c3_lbl = Label(F6, text="Cold Drink Tax", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        c3_txt = Entry(F6, width=18, font="arial 10 bold", textvariable=self.colddrink_tax,bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        btn_f = Frame(F6,bd=7,relief=GROOVE)
        btn_f.place(x=730,width=600,height=105)

        total_btn=Button(btn_f,command=self.total,text="Total",bg="cadetblue",fg="white",bd=5,pady=15,width=10,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        gbill_btn=Button(btn_f,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",bd=5,pady=15,width=10,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_f,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",bd=5,pady=15,width=10,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_f,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",bd=5,pady=15,width=10,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*100
        self.c_fw_p = self.face_wash.get()*120
        self.c_hs_p = self.hair_sh.get()*20
        self.c_hg_p = self.hair_gel.get()*60
        self.c_bl_p = self.body_loshan.get()*180


        self.total_cosmetic_price=float(
            (self.c_s_p)+
            (self.c_fc_p)+
            (self.c_fw_p)+
            (self.c_hs_p)+
            (self.c_hg_p)+
            (self.c_bl_p)
            )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round(self.total_cosmetic_price*0.05,2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))

        self.g_r_p = self.rice.get()*40.50
        self.g_fi_p = self.food_oil.get()*1550
        self.g_d_p = self.daal.get()*140
        self.g_w_p = self.weate.get()*27
        self.g_s_p = self.sugar.get()*40
        self.g_t_p = self.tea.get()*100

        self.total_grosary_price=float(
            (self.g_r_p)+
            (self.g_fi_p)+
            (self.g_d_p)+
            (self.g_w_p)+
            (self.g_s_p)+
            (self.g_t_p)
            )
        self.grosary_price.set("Rs. "+str(self.total_grosary_price))
        self.g_tax=round(self.total_grosary_price * 0.05,2 )
        self.grosary_tax.set("Rs. " + str(self.g_tax))

        self.c_c_p= self.cock.get()*50
        self.c_m_p= self.maza.get()*50
        self.c_ft_p= self.funta.get()*45
        self.c_tu_p= self.thumbs_up.get()*45
        self.c_sp_p= self.sprite.get()*50
        self.c_fr_p= self.fruity.get()*40

        self.total_coldDrink_price=float(
            (self.c_c_p)+
            (self.c_m_p)+
            (self.c_ft_p)+
            (self.c_tu_p)+
            (self.c_sp_p)+
            (self.c_fr_p)
            )
        self.colddrink_price.set("Rs. "+str(self.total_coldDrink_price))
        self.cd_tax=round(self.total_coldDrink_price * 0.05, 2)
        self.colddrink_tax.set("Rs. " + str(self.cd_tax))

        self.Total_bill = float(self.total_cosmetic_price + self.c_tax + self.total_grosary_price + self.g_tax + self.total_coldDrink_price + self.cd_tax)

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome Webcode Retail\n")
        self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.cname.get()}")
        self.txtarea.insert(END,f"\n Phone Number : {self.cphone.get()}")
        self.txtarea.insert(END,f"\n=========================================")
        self.txtarea.insert(END,f"\n Product\t\tQYT\t\tPrice")
        self.txtarea.insert(END,f"\n=========================================")

    def bill_area(self):
        if self.cname.get()=="" or self.cphone.get()=="":
            messagebox.showerror("Error","Customer Detial are must.")
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grosary_price.get()=="Rs. 0.0" and self.colddrink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No Product Purches.")
        else:
            self.welcome_bill()
            #=======cosmetic
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.hair_sh.get()!=0:
                self.txtarea.insert(END,f"\n Hair shampoo\t\t{self.hair_sh.get()}\t\t{self.c_hs_p}")
            if self.hair_gel.get()!=0:
                self.txtarea.insert(END,f"\n Hair Gel\t\t{self.hair_gel.get()}\t\t{self.c_hg_p}")
            if self.body_loshan.get()!=0:
                self.txtarea.insert(END,f"\n Body Loshan\t\t{self.body_loshan.get()}\t\t{self.c_bl_p}")

            #===========grosary

            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.food_oil.get()!=0:
                self.txtarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_fi_p}")
            if self.daal.get()!=0:
                self.txtarea.insert(END,f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")
            if self.weate.get()!=0:
                self.txtarea.insert(END,f"\n Weate\t\t{self.weate.get()}\t\t{self.g_w_p}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Hair Gel\t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")

            #========cold Drink============

            if self.cock.get()!=0:
                self.txtarea.insert(END,f"\n Cock\t\t{self.cock.get()}\t\t{self.c_c_p}")
            if self.maza.get()!=0:
                self.txtarea.insert(END,f"\n Maza\t\t{self.maza.get()}\t\t{self.c_m_p}")
            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.c_sp_p}")
            if self.thumbs_up.get()!=0:
                self.txtarea.insert(END,f"\n Thumbs up\t\t{self.thumbs_up.get()}\t\t{self.c_tu_p}")
            if self.funta.get()!=0:
                self.txtarea.insert(END,f"\n Funta\t\t{self.funta.get()}\t\t{self.c_ft_p}")
            if self.fruity.get()!=0:
                self.txtarea.insert(END,f"\n Fruiti\t\t{self.fruity.get()}\t\t{self.c_fr_p}")

            #=======Tax=======

            self.txtarea.insert(END,f"\n-----------------------------------------")
            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Cosmetic Product Tax  \t\t\t {self.cosmetic_tax.get()}")
            if self.grosary_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Grosary Product Tax   \t\t\t {self.grosary_tax.get()}")
            if self.colddrink_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Cold-Drink Product Tax\t\t\t {self.colddrink_tax.get()}")

            self.txtarea.insert(END,f"\n-----------------------------------------")

            self.txtarea.insert(END, f"\n Total Bill : \t\t\t Rs. {self.Total_bill}")
            self.save_bill()

    def save_bill(self):
            op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
            if op>0:
                self.bill_data=self.txtarea.get("1.0",END)
                f1=open("bills/"+str(self.bill_no.get())+".txt","w")
                f1.write(self.bill_data)
                f1.close()
                messagebox.showinfo("Saved",f"Bill NO : {self.bill_no.get()} saved succesfully")
            else:
                return

    def find_bill(self):
            present="no"
            for i in os.listdir("bills/"):
                if i.split('.')[0]==self.search_bill.get():
                    f1=open(f"bills/{i}","r")
                    self.txtarea.delete('1.0',END)
                    for d in f1:
                        self.txtarea.insert(END,d)
                    f1.close()
                    present="yes"
            if present=="no":
                messagebox.showerror("Error","Invalid Bill Number.")
    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really want to Clear?")
        if op>0:
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.hair_sh.set(0)
            self.hair_gel.set(0)
            self.body_loshan.set(0)

            #=====variable grosary

            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.weate.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            # =====variable cold drink

            self.cock.set(0)
            self.funta.set(0)
            self.maza.set(0)
            self.thumbs_up.set(0)
            self.sprite.set(0)
            self.fruity.set(0)

            #===== prise and tax

            self.cosmetic_price.set("")
            self.grosary_price.set("")
            self.colddrink_price.set("")

            self.cosmetic_tax.set("")
            self.grosary_tax.set("")
            self.colddrink_tax.set("")

            #======customer

            self.cname.set("")
            self.cphone.set("")
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")

            self.welcome_bill()


    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()







root=Tk()
obj = Bill_App(root)
root.mainloop()