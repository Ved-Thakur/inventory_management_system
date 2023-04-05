from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class supp:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        self.var_searchby=StringVar()
        self.var_searchtxt = StringVar()

        self.var_sup_iv = StringVar()
        self.var_sup_name = StringVar()
        self.var_contact = StringVar()

       # search = LabelFrame(self.root, text="Search Employee", font=("goudy old style", 12, "bold"), bg="white")
       # search.place(x=250, y=20, width=600, height=70)
       #
       #  lbl_search=Label(search,text="Search By Invoice No.",font=("goudy old style",15),bg="white")
       #  lbl_search.place(x=10,y=10,width=180)
       #
       #  txt_search= Entry(search, textvariable=self.var_searchtxt, font=("goudy old style", 15), bg="lightyellow")
       #  txt_search.place(x=210, y=10)
       # enter_btn = Button(search, text="Search", font=("goudy old style", 15), bg="green", relief=RIDGE, cursor="hand2")
       #  enter_btn.place(x=430, y=10, width=150, height=29)

        title=Label(self.root,text="Supplier Details",font=("goudy old style",15),bg="Blue",fg="white")
        title.place(x=50, y=10, width=1000, height=30)

        #---------empid, contact , gender---------------
        lbl_suppiv = Label(self.root, text="Invoice No.", font=("goudy old style", 15), bg="white").place(x=50, y=70)
        txt_suppiv = Entry(self.root, textvariable=self.var_sup_iv, font=("goudy old style", 15), bg="lightyellow").place(x=180, y=70,width=200)

        #----------name ,dob,doj-------------
        lbl_Name = Label(self.root, text="Supplier Name", font=("goudy old style", 15), bg="white").place(x=50, y=110)
        txt_Name = Entry(self.root, textvariable=self.var_sup_name, font=("goudy old style", 15),bg="lightyellow").place(x=180, y=110, width=200)

        lbl_cont = Label(self.root, text="Contact", font=("goudy old style", 15), bg="white").place(x=50, y=150)
        txt_cont = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15),bg="lightyellow").place(x=180, y=150, width=200)


        lbl_search_iv = Label(self.root, text="Invoice No.", font=("goudy old style", 15,"bold"), bg="white").place(x=620, y=70)
        txt_Search_iv= Entry(self.root, textvariable=self.var_searchtxt, font=("goudy old style", 15),bg="white").place(x=730, y=70, width=180)
        btn_search = Button(self.root, text="Search",command=self.search, font=("goudy old style", 15), bg="green", fg="white",cursor="hand2", relief=RIDGE).place(x=930, y=70, width=130, height=30)

       #----------add,salary----------
        lbl_desc = Label(self.root, text="Description", font=("goudy old style", 15), bg="white").place(x=50, y=190)
        self.txt_desc = Text(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.txt_desc.place(x=180, y=190, width=300,height=75)

        #-----------buttons------------
        btn_save=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#00A1AF",fg="white",cursor="hand2",relief=RIDGE).place(x=50,y=310,width=120,height=30)
        btn_update = Button(self.root, text="Update",command=self.update, font=("goudy old style", 15), bg="green", fg="white",cursor="hand2", relief=RIDGE).place(x=180, y=310, width=120, height=30)
        btn_del = Button(self.root, text="Delete",command=self.delete, font=("goudy old style", 15), bg="red", fg="white",cursor="hand2", relief=RIDGE).place(x=310, y=310, width=120, height=30)
        btn_clear = Button(self.root, text="Clear",command=self.clear, font=("goudy old style", 15), bg="grey", fg="white",cursor="hand2", relief=RIDGE).place(x=450, y=310, width=120, height=30)

        supp_frame=Frame(self.root,bd=3,relief=RIDGE)
        supp_frame.place(x=650, y=130, height=350)

        scrolly=Scrollbar(supp_frame,orient=VERTICAL)
        scrollx=Scrollbar(supp_frame,orient=HORIZONTAL)

        self.SupplierTable=ttk.Treeview(supp_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)

        self.SupplierTable.heading("invoice",text="Invoice No.")
        self.SupplierTable.heading("name", text="Name")
        self.SupplierTable.heading("contact", text="Contact")
        self.SupplierTable.heading("desc", text="Desc")

        self.SupplierTable["show"]="headings"

        self.SupplierTable.column("invoice",width=90)
        self.SupplierTable.column("name",width=100)
        self.SupplierTable.column("contact",width=100)
        self.SupplierTable.column("desc",width=100)

        self.SupplierTable.pack(fill=BOTH,expand=1)

        self.SupplierTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

        # =================================================================================================

    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_iv.get() == "":
                messagebox.showerror("Error", "Invoice Must be required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?", (self.var_sup_iv.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Invoice no. already assigned, try different", parent=self.root)
                else:
                    cur.execute(
                        "Insert into Supplier (invoice,name,contact,desc) values (?,?,?,?)",
                        (
                            self.var_sup_iv.get(),
                            self.var_sup_name.get(),
                            self.var_contact.get(),
                            self.txt_desc.get('1.0',END),
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Added Successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from supplier")
            rows = cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.SupplierTable.focus()
        content = (self.SupplierTable.item(f))
        row = content['values']
        self.var_sup_iv.set(row[0])
        self.var_sup_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_desc.delete('1.0', END)
        self.txt_desc.insert(END, row[3])

    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_iv.get() == "":
                messagebox.showerror("Error", "invoice no Must be required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?", (self.var_sup_iv.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Invoice no", parent=self.root)
                else:
                    cur.execute(
                        "Update Supplier set name=?,contact=?,desc=? where invoice=?",
                        (
                            self.var_sup_name.get(),
                            self.var_contact.get(),
                            self.txt_desc.get('1.0', END),  # nonetype error
                            self.var_sup_iv.get(),
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Updated Successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_iv.get() == "":
                messagebox.showerror("Error", "Invoice no Must be required", parent=self.root)
            else:
                cur.execute("Select * from Supplier where invoice=?", (self.var_sup_iv.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Invoice no", parent=self.root)
                else:
                    op = messagebox.askyesno("confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from supplier where invoice no=?", (self.var_sup_iv.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Supplier Deleted Successfully", parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self):
        self.var_sup_id.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0', END)
        self.var_searchtxt.set("")
        self.show()

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Invoice no. should be required", parent=self.root)
            else:
                cur.execute("select * from Supplier where invoice=?", (self.var_searchtxt.get(),))
                row = cur.fetchone()
                if row != None:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    self.SupplierTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "no record found!!!", parent=self.root)


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__=="__main__":
    root = Tk()
    obj  = supp(root)
    root.mainloop()