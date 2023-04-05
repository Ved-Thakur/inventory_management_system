import sqlite3


def create_db():
    con = sqlite3.connect(database=r'ims.db')
    cur = con.cursor()
    cur.execute("Create table if not exists employee(eid integer primary key autoincrement,name text,email text,gender text,contact text,dob text,doj text,pass text,utype text,address text,salary text)")
    con.commit()
    cur.execute("Create table if not exists Supplier(invoice integer primary key autoincrement,name text,contact text,desc text)")
    con.commit()
    cur.execute("Create table if not exists category(cid integer primary key autoincrement,name text)")
    con.commit()
    cur.execute("CREATE TABLE if not exists product(pid integer primary key autoincrement,Supplier text,Category text,name text,price text,qty text,status text)")
    con.commit()

create_db()
