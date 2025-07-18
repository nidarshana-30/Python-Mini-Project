import mysql.connector
from tabulate import tabulate

con = mysql.connector.connect(host="127.0.0.1", user="root", 
                              password="use your password", database="use your database name")

def insert():
    name = input("Enter Name : ")
    age = input("Enter Age : ")
    address = input("Enter Address : ")
    contact = input("Enter Contact : ")
    mail = input("Enter Mail : ")

    res = con.cursor()
    sql = "insert into data (name,age,address,contact,mail) values (%s,%s,%s,%s,%s)"
    res.execute(sql,(name, age, address,contact,mail))
    con.commit()
    print("\n")
    print("Record Insert Successfully")


def select():
    res = con.cursor()
    sql = "SELECT * from data"
    res.execute(sql)
    result = res.fetchall()
    print("\n")
    #print(tabulate(result, headers=[ "ID","NAME", "AGE", "ADDRESS","CONTACT","MAIL"]))
    #print(tabulate(result, headers=["ID", "NAME", "AGE", "ADDRESS","CONTACT","MAIL"],tablefmt="github"))
    print(tabulate(result, headers=["ID", "NAME", "AGE", "ADDRESS","CONTACT","MAIL"],tablefmt="grid"))
    #print(tabulate(result, headers=["ID", "NAME", "AGE", "ADDRESS","CONTACT","MAIL"],tablefmt="presto"))
def update():
    print("1.Name")
    print("2.Age")
    print("3.Address")
    print("4.Contact")
    print("5.Mail")
    option = int(input("\nWhich field you want to update?:"))
    if option == 1:
        id = input("Enter Your ID:")
        name = input("Enter Your Name:")
        cur = con.cursor()
        sql = "UPDATE data set name=%s where id=%s"
        cur.execute(sql, (name, id))
        con.commit()
        select()
        print("\n")
        print("Update Successfully")
    elif option == 2:
        id = input("Enter Your ID:")
        age = input("Enter Your Age:")
        cur = con.cursor()
        sql = "UPDATE data set age=%s where id=%s"
        cur.execute(sql, (age, id))
        con.commit()
        select()
        print("\n")
        print("Update Successfully")
    elif option == 3:
        id = input("Enter Your ID:")
        address = input("Enter Your Address:")
        cur = con.cursor()
        sql = "UPDATE data set address=%s where id=%s"
        cur.execute(sql, (address, id))
        con.commit()
        select()
        print("\n")
        print("Update Successfully")
    elif option == 4:
        id = input("Enter Your ID:")
        contact = input("Enter Your Contact:")
        cur = con.cursor()
        sql = "UPDATE data set contact=%s where id=%s"
        cur.execute(sql, (contact, id))
        con.commit()
        select()
        print("\n")
        print("Update Successfully")
    elif option == 5:
        id = input("Enter Your ID:")
        mail = input("Enter Your Mail:")
        cur = con.cursor()
        sql = "UPDATE data set mail=%s where id=%s"
        cur.execute(sql, (mail, id))
        con.commit()
        select()
        print("\n")
        print("Update Successfully")
    else:
        print("Invalid")

def delete():
    id = input("Enter Your ID:")
    res = con.cursor()
    sql = "delete from data where id=%s"
    res.execute(sql,(id,))
    con.commit()
    print("\n")
    print("Record Deleted Successfully...!!!")


while True:
    print("\n")
    print("1.Insert Record")
    print("2.Select Record")
    print("3.Update Record")
    print("4.Delete Record")
    print("5.Exit")
    print("\n")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        insert()
    elif choice == 2:
        select()
    elif choice == 3:
        update()
    elif choice == 4:
        delete()
    elif choice == 5:
        quit()
    else:
        print("Invalid Option...!!!")
