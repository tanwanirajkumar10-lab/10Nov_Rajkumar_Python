import sqlite3

try:
    db = sqlite3.connect("student.db")
    print("Database Connected")
except Exception as e:
    print(e)

#Table Create

table_create = "create table studinfo(id integer primary key autoincrement,name text, sub text)"
try:
    db.execute(table_create)
    print("Table Created")
except Exception as e:
    print(e)


#Insert Data

'''insert_data = "insert into studinfo(name,sub) values ('Raj','Pyhton')"
try:
    db.execute(insert_data)
    db.commit()
    print("Record Inserted")
except Exception as e:
    print(e)'''


    #Update Data

'''update_data = "update studinfo set sub='Java' where id='1'"
try:
    db.execute(update_data)
    db.commit()
    print("Record Updated")
except Exception as e:
    print(e)'''


#Delete Data

delete_data = "delete from studinfo where id='6'"
try:
    db.execute(delete_data)
    db.commit()
    print("Record Deleted")
except Exception as e:
    print(e)

    #View Data
'''
select_data = "select * from studinfo"
try:
    cr=db.cursor()
    cr.execute(select_data)
    data = cr.fetchall()
    print(data)
except Exception as e:
    print(e)

'''