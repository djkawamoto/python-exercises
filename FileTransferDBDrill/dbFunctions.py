import sqlite3
import time
import datetime

conn = sqlite3.connect('DailyFileTransfer.db')
c = conn.cursor()

def createTable():
    c.execute("CREATE TABLE if not exists \
    FileCheckTimes( \
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    unix REAL, \
    datestamp TEXT \
    );")

def viewAll():
    sql_str = "SELECT * FROM FileCheckTimes"
    c.execute(sql_str)
    rows = c.fetchall()
    return rows

def addEntry():
    current_time = int(time.time())
    date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%m-%d-%Y %H:%M:%S'))
    c.execute("INSERT INTO FileCheckTimes (unix, datestamp) VALUES (?,?)", (current_time, date))
    conn.commit()

def mostRecentEntry():
    sql = "SELECT datestamp FROM FileCheckTimes WHERE ID = (SELECT MAX(ID) FROM FileCheckTimes);" #"SELECT * FROM FileCheckTimes;" #WHERE unix =?"
    c.execute(sql)
    x = str(c.fetchall())
    y = x[4:-4]
    return y

def mostRecentUnix():
    sql = "SELECT unix FROM FileCheckTimes WHERE ID = (SELECT MAX(ID) FROM FileCheckTimes);"
    c.execute(sql)
    x = str(c.fetchall())
    try:
        y = float(x[2:-3])
        z = int(y)
        return z
    except ValueError:
        return 0

createTable()
