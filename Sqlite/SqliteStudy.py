#!/usr/bin/python

import sqlite3

conn=sqlite3.connect('test.db')
print("Opened database successfully")
c = conn.cursor()

##c.execute('''CREATE TABLE DATA
##       (ID INTEGER PRIMARY KEY AUTOINCREMENT,
##       TIME           TEXT    ,
##       T            TEXT     ,
##       H        TEXT);''')
     
print("Table created successfully")

c.execute("INSERT INTO DATA (TIME,T,H) \
      VALUES ('1', '21', '20')");


conn.commit()
conn.close()
