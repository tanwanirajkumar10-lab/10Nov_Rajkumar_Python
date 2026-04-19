import tkinter
from tkinter import ttk,messagebox
import sqlite3

window=tkinter.Tk()
window.title("MyApp")
window.geometry("400x500")
window.config(bg="lightblue")

#Create Database if not
try:
    db = sqlite3.connect("student.db")
    print("Database Connected")
except Exception as e:
    print(e)

#Table Create

def create_table():
    try:
        table_create = "create table studinfo(id integer primary key autoincrement,name text, sub text)"
        db.execute(table_create)
        print("Table Created")
    except Exception as e:
        print(e)

#insert Record

def insert_record():

    try:   
        insert_data = f"insert into studinfo(name,sub) values ('{name.get()}','{subject.get()}')"
        db.execute(insert_data)
        db.commit()
        print("Record Inserted")
    except Exception as e:
        print(e)

#Update Data
'''
def update_record():

    try: 
        update_data = f"update studinfo set name='{name}',sub='{subject}' where id={'id.get()'}"
        db.execute(update_data)
        db.commit()
        print("Record Updated")
    except Exception as e:
        print(e)


select_data = "select * from studinfo "
try:
    cr=db.cursor()
    cr.execute(select_data)
    data = cr.fetchall()
    print(data)
except Exception as e:
    print(e)
    '''
lbl1=tkinter.Label(text="Name",bg="lightblue",fg='red',font='Constantia 15 bold')
lbl1.grid(row=0,column=0)

lbl2=tkinter.Label(text="Subject",bg="lightblue",fg='red',font='Constantia 15 bold')
lbl2.grid(row=1,column=0)

name=tkinter.Entry()
name.grid(row=0,column=1)

subject=tkinter.Entry()
subject.grid(row=1,column=1)


def btnInsert():
   
    insert_record()
    name.delete(0, tkinter.END)
    subject.delete(0, tkinter.END)
'''
def btnUpdate():
   
    update_record()
    name.delete(0, tkinter.END)
    subject.delete(0, tkinter.END)

def btnDelete():
   
    insert_record()
    name.delete(0, tkinter.END)
    subject.delete(0, tkinter.END)

def btnView():
   
    insert_record()
    name.delete(0, tkinter.END)
    subject.delete(0, tkinter.END)    

'''
btninsert=tkinter.Button(text="Insert",bg="black",fg='red',font='Constantia 15 bold',command=btnInsert)
btninsert.place(x=10,y=100)


btnupdate=tkinter.Button(text="Update",bg="black",fg='red',font='Constantia 15 bold')
btnupdate.place(x=100,y=100)

btndelete=tkinter.Button(text="Delete",bg="black",fg='red',font='Constantia 15 bold')
btndelete.place(x=200,y=100)

btnview=tkinter.Button(text="View",bg="black",fg='red',font='Constantia 15 bold')
btnview.place(x=300,y=100)

window.mainloop()
