#Write a Python program to create a database and a table using SQLite3.

import sqlite3

#Create Database

try:
    db=sqlite3.connect("school.db")
    print("Database connection established successfully.")
except Exception as e:
   print(e)

#Create Table

tbl_create="create table student(id integer primary key autoincrement, name varchar(20), city varchar(20))"
try:
    db.execute(tbl_create)
    print("Table created successfully.")
except Exception as e:
    print(e)