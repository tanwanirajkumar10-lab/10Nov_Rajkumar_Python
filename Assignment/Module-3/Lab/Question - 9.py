#Write a Python program to connect to an SQLite3 database, create a table, insert data and fetch data.

import sqlite3

#Create Database

try:
    db=sqlite3.connect("company.db")
    print("Database connection established successfully.")
except Exception as e:
   print(e)

#Create Table

tbl_create="create table employee(id integer primary key autoincrement, name varchar(20), city varchar(20))"
try:
    db.execute(tbl_create)
    print("Table created successfully.")
except Exception as e:
    print(e)

#Insert Data

insert_data="insert into employee(name,city)values('Rajkumar','Rajkot'),('Ashish','Ahmedabad'),('Jay','surat')"

try:
    db.execute(insert_data)
    db.commit()
    print("Data inserted successfully.")
except Exception as e:
    print(e)

#Select data

select_data="select * from employee"
try:
    cr=db.cursor()
    cr.execute(select_data)
    data=cr.fetchall()
    print(data)
    for i in data:
        print(i)
except Exception as e:
    print(e)