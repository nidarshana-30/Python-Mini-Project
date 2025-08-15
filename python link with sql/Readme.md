# Python MySQL CRUD Application

A simple Python application to perform CRUD operations (Create, Read, Update, Delete) on a MySQL database using the mysql-connector-python library. The data is displayed neatly in a tabular format using the tabulate library.

## Features

?* Insert Records into the database.

* View Records in a formatted table.

* Update Records (Name, Age, Address, Contact, Mail) using user input.

* Delete Records by ID.

* Interactive Menu to perform operations repeatedly.

## Technologies Used

Python 3.x

MySQL

## Libraries:

mysql-connector-python

## Database Setup

Connect to MySQL:

        SHOW DATABASES;
        USE mysql;


Create the data table:

        CREATE TABLE data(
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(30),
            age INT,
            address VARCHAR(30),
            contact VARCHAR(10),
            mail VARCHAR(50)
        );


Optional: Modify the contact column length if needed:

        ALTER TABLE data MODIFY contact VARCHAR(10);
        
        
        Delete table (if needed for reset):
        
        DROP TABLE data;

## Python Setup

1)Install required packages:

        pip install mysql-connector-python
        pip install tabulate


2)Database connection:

        import mysql.connector
        
        con = mysql.connector.connect(
            host="127.0.0.1", 
            user="root", 
            password="your_password", 
            database="your_database_name"
        )

3)How to Run

Run the Python script:

        python your_script_name.py


4)You will see a menu:

1. Insert Record
2. Select Record
3. Update Record
4. Delete Record
5. Exit


Enter your choice and follow the prompts.

## Example Output

Select Records Table Format:

        +----+--------+-----+---------+-----------+------------------+
        | ID | NAME   | AGE | ADDRESS | CONTACT   | MAIL             |
        +----+--------+-----+---------+-----------+------------------+
        | 1  | John   | 25  | NY      | 1234567890| john@mail.com    |
        | 2  | Alice  | 30  | LA      | 9876543210| alice@mail.com   |
        +----+--------+-----+---------+-----------+------------------+

## Notes

Make sure MySQL service is running on your system.

Update your host, user, password, and database name in the Python script.

The tabulate library allows multiple table formats, like grid, github, presto.
