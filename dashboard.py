import os
from tkinter import*
from PIL import Image,ImageTk
import sqlite3
from tkinter import messagebox
from employee import Emp
from sales import salesClass
from supplier import supp
from category import category
from product import prod
import os
import time
class Dash:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")

        self.icon=PhotoImage(file="images/logo1.png")
        title = Label(self.root,text="Inventory Management System",image=self.icon,compound=LEFT,font=("time new roman",40,"bold"),bg="blue",fg="white",anchor="w",padx=30).place(x=0,y=0,relwidth=1,height=70)

        #BUTTON
        logout= Button(self.root,text ="Logout",command=self.logout, font=("time new roman",15,"bold"),cursor="hand2",bg="yellow").place(x=1190,y=10,height=45)

        #clock
        self.clock = Label(self.root, text="Welcome to inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("time new roman",15),bg="grey",fg="white")
        self.clock.place(x=0,y=70,relwidth=1,height=30)

        #Menu
        self.menulogo=Image.open("images/menu_im.png")
        self.menulogo=self.menulogo.resize((200,200),Image.ANTIALIAS)
        self.menulogo=ImageTk.PhotoImage(self.menulogo)

        Menu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Menu.place(x=0,y=102,width=200,height=565)

        lbl_menulogo=Label(Menu,image=self.menulogo)
        lbl_menulogo.pack(side=TOP,fill=X)

        self.side=PhotoImage(file="images/side.png")
        menu=Label(Menu,text="Menu",font=("time new roman",20),bg="green").pack(side=TOP,fill=X)
        emp = Button(Menu, text="Employee",command=self.Empp,image=self.side,compound=LEFT,padx=5,anchor="w",font=("time new roman", 20,"bold"), bg="white",bd=3,cursor="hand2").pack(side=TOP, fill=X)
        supp= Button(Menu, text="Supplier",command=self.supp,image=self.side, compound=LEFT, padx=5, anchor="w",font=("time new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        cat = Button(Menu, text="Category",command=self.category, image=self.side, compound=LEFT, padx=5, anchor="w",font=("time new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        prod= Button(Menu, text="Products", command=self.product,image=self.side, compound=LEFT, padx=5, anchor="w",font=("time new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        sales= Button(Menu, text="Sales", command=self.sales, image=self.side, compound=LEFT, padx=5, anchor="w",font=("time new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        exit = Button(Menu, text="Exit", command= self.logout,image=self.side,compound=LEFT, padx=5, anchor="w",font=("time new roman", 20, "bold"),bg="white",bd=3, cursor="hand2").pack(side=TOP, fill=X)

        self.lbl_emp=Label(self.root,text= "Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="cyan",font=("goudy old style",20,"bold"))
        self.lbl_emp.place(x=300,y=150,height=150,width=300)

        self.lbl_supp = Label(self.root, text="Total Supplier\n[ 0 ]", bd=5, relief=RIDGE, bg="cyan", font=("goudy old style", 20, "bold"))
        self.lbl_supp.place(x=650, y=150, height=150, width=300)

        self.lbl_cat = Label(self.root, text="Total Category\n[ 0 ]", bd=5, relief=RIDGE, bg="cyan", font=("goudy old style", 20, "bold"))
        self.lbl_cat.place(x=1000, y=150, height=150, width=300)

        self.lbl_prod = Label(self.root, text="Total Product\n[ 0 ]", bd=5, relief=RIDGE, bg="cyan", font=("goudy old style", 20, "bold"))
        self.lbl_prod.place(x=450, y=350, height=150, width=300)

        self.lbl_sales = Label(self.root, text="Total Sales\n[ 0 ]", bd=5, relief=RIDGE, bg="cyan", font=("goudy old style", 20, "bold"))
        self.lbl_sales.place(x=800, y=350, height=150, width=300)

        self.update_content()

    def Empp(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Emp(self.new_win)

    def supp(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supp(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=category(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=prod(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)

    def logout(self):
        self.root.destroy()
        os.system("python login.py")

    def update_content(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_prod.config(text=f"Total Product\n[ {str(len(product))} ]")

            cur.execute("select * from supplier")
            supplier = cur.fetchall()
            self.lbl_supp.config(text=f"Total Suppliers\n[ {str(len(supplier))} ]")

            cur.execute("select * from Category")
            category = cur.fetchall()
            self.lbl_cat.config(text=f"Total Category\n[ {str(len(category))} ]")

            cur.execute("select * from employee")
            employee = cur.fetchall()
            self.lbl_emp.config(text=f"Total Employees\n[ {str(len(employee))} ]")

            self.lbl_sales.config(text=f"Total Sales [{str(len(os.listdir('bill')))}]")

            time_ = time.strftime("%I:%M:%S")
            date_ = time.strftime("%d-%m-%Y")
            self.clock.config(text=f"Welcome to Inventory Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
            self.clock.after(200,self.update_content)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

if __name__=="__main__":
    root = Tk()
    obj  = Dash(root)
    root.mainloop()