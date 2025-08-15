# SQLite CRUD Operations with Python

This project demonstrates basic CRUD (Create, Read, Update, Delete) operations using Python and SQLite3. It allows users to manage records with fields like name, age, gender, address, contact, and email via a simple command-line interface.

## 📌 Project Overview

? Language: Python

* Database: SQLite3

* Functionality:

Insert new records

Fetch all records

Update existing records

Delete records

## 🛠 Technologies Used

Python 3.x

SQLite3 (Python built-in module)

## ✨ Features

* Database Creation: Automatically creates a SQLite database (Sqlitedatabase.db) and table if not exists.

* Insert Records: Add new entries with all necessary fields.

* Fetch Records: Display all saved records in a structured format.

* Update Records: Update any specific field (name, age, gender, address, contact, or mail) of a record using the record ID.

* Delete Records: Remove a record using its ID.

* User-Friendly Interface: Simple command-line menu for performing CRUD operations.

## 🚀 How to Use

Clone or download this repository.

Ensure Python 3.x is installed on your system.

Run the Python script:

python your_script_name.py


** Follow the on-screen menu:

1 → Insert Record

2 → Fetch Record

3 → Update Record

4 → Delete Record

Enter the required details when prompted.

## 📂 Database

The project uses a SQLite database (Sqlitedatabase.db).

Table datas schema:
| Column | Type | Notes |
|----------|--------|-------------------------------|
| id | INTEGER | Primary Key, Auto Increment |
| name | TEXT | Not Null |
| age | INTEGER | Not Null |
| gender | TEXT | Not Null |
| address | TEXT | Not Null |
| contact | TEXT | Not Null |
| mail | TEXT | Not Null |

## 💡 Example Usage
Please Enter Your Operation: 1
Enter Your Name: John Doe
Enter Your Age: 30
Enter Your Gender: Male
Enter Your Address: 123 Main St
Enter Your Contact: 1234567890
Enter Your Mail: john@example.com
Record Added Successfully

## 📈 Future Improvements

Add input validation for fields like email and contact number.

Integrate a graphical user interface (GUI) using Tkinter or PyQt.

Add search functionality to quickly find records.
