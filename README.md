# Python CRUD Applications

This repository contains Python applications to perform CRUD (Create, Read, Update, Delete) operations using two different databases: **MySQL and SQLite**. Both applications provide interactive menus and display data in a tabular format using the tabulate library.

**Table of Contents**

 * Features

* Technologies Used

* MySQL CRUD Application

      Database Setup
      
      Python Setup
      
      How to Run

* SQLite CRUD Application

      Database Setup
      
      Python Setup
      
      How to Run

* Example Output

* Notes


## Features

* Insert records into the database.

* View records in a formatted table.

* Update records (Name, Age, Address, Contact, Mail).

* Delete records by ID.

* Interactive menu-driven interface for easy operations.

* Works with both MySQL and SQLite.

## Technologies Used

* Python 3.x

* Databases: MySQL, SQLite

* Libraries:
      
      mysql-connector-python (for MySQL)
      
      sqlite3 (built-in for SQLite)
      
      tabulate (for table formatting)

  ## MySQL CRUD Application
### Database Setup

1) Connect to MySQL:

            SHOW DATABASES;
            USE your_database_name;

2)Create the data table:

             CREATE TABLE data(
                id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(30),
                age INT,
                address VARCHAR(30),
                contact VARCHAR(10),
                mail VARCHAR(50)
            );
3) Optional: Modify column length:

            ALTER TABLE data MODIFY contact VARCHAR(10);

### Python Setup

1)Install required packages:

            pip install mysql-connector-python
            pip install tabulate


2) Connect to your MySQL database in Python:

            import mysql.connector
            
            con = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="your_password",
                database="your_database_name"
            )

### How to Run

* Run the MySQL Python script:

            python mysql_crud.py


* Follow the menu:

1. Insert Record
2. Select Record
3. Update Record
4. Delete Record
5. Exit
   
## SQLite CRUD Application
### Database Setup

SQLite is file-based, so no server setup is required. A database file will be created automatically (e.g., database.db) when the script is run.

Create the data table (if not exists):

            import sqlite3
            
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute("""
            CREATE TABLE IF NOT EXISTS data(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                address TEXT NOT NULL,
                contact TEXT NOT NULL,
                mail TEXT NOT NULL
            )
            """)
            con.commit()
            con.close()

###  Python Setup

No extra packages needed for SQLite (built-in).

Install tabulate for table formatting:

            pip install tabulate

### How to Run

* Run the SQLite Python script:

            python sqlite_crud.py


Use the interactive menu to manage records.

## Example Output

Tabular Display of Records:

            +----+--------+-----+---------+-----------+------------------+
            | ID | NAME   | AGE | ADDRESS | CONTACT   | MAIL             |
            +----+--------+-----+---------+-----------+------------------+
            | 1  | John   | 25  | NY      | 1234567890| john@mail.com    |
            | 2  | Alice  | 30  | LA      | 9876543210| alice@mail.com   |
            +----+--------+-----+---------+-----------+------------------+

## Notes

* Ensure MySQL service is running for MySQL operations.

* Update your host, user, password, and database name in the Python script.

* SQLite database file is created automatically.

* tabulate supports multiple formats: grid, github, fancy_grid, etc.
sqlite3 (built-in for SQLite)

tabulate (for table formatting)
