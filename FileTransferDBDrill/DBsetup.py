import sqlite3
import time
import datetime

conn = sqlite3.connect('DailyFileTransfer.db')
c = conn.cursor()

def TableCreate():
    c.execute("CREATE TABLE FileCheckTimes(ID INT PRIMARY KEY, unix REAL, datestamp TEXT)")
    print currenttime


sql = "SELECT unix FROM FileCheckTimes WHERE ID = (SELECT MAX(ID) FROM FileCheckTimes);" #"SELECT * FROM FileCheckTimes;" #WHERE unix =?"
currenttime = time.time()

def TimeOfRecord():
    date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))
    c.execute("INSERT INTO FileCheckTimes (unix, datestamp) VALUES (?,?)", (currenttime, date))
    conn.commit()

def TestConn():
    c.execute(sql)
    print currenttime

def GetMostRecentEntry():
    c.execute(sql)
    x = c.fetchall()
    print x

GetMostRecentEntry()
