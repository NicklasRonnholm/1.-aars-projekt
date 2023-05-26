import sqlite3 as sql

con = sql.connect('kodeord_database.db')
cur = con.cursor()

sql ='''CREATE TABLE "bruger"(
    "UID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "username" TEXT,
    "password" TEXT,
    "admin" TEXT
)'''
cur.execute(sql)

con.commit()

con.close()