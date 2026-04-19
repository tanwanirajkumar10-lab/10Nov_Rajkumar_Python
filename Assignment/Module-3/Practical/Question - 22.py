#Write a Python program to insert data into an SQLite3 database and fetch it.

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

#Insert Data

insert_data="insert into student(name,city)values('Rajkumar','Rajkot'),('Ashish','Ahmedabad'),('Jay','surat')"

try:
    db.execute(insert_data)
    db.commit()
    print("Data inserted successfully.")
except Exception as e:
    print(e)

#Select data

select_data="select * from student"
try:
    cr=db.cursor()
    cr.execute(select_data)
    data=cr.fetchall()
    for i in data:
        print(i)
except Exception as e:
    print(e)