import sqlite3 as sql

con = sql.connect('kundesag.db')
cur = con.cursor()

sql ='''CREATE TABLE "sager"(
    "User" INTEGER PRIMARY KEY AUTOINCREMENT,
    "Involveret" TEXT,
    "Ulykke" TEXT,
    "Location" TEXT
)'''
cur.execute(sql)

con.commit()

con.close()