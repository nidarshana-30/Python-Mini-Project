#pip install mysql-connector-python
#pip install tabulate

import mysql.connector
mydb=mysql.connector.connect(host="127.0.0.1",user="root",password="neethu3026")
mycursor=mydb.cursor()
mycursor.execute("SHOW DATABASES")
for i in mycursor:
    print(i)