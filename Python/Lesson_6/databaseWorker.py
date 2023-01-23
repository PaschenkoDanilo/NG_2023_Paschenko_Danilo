import sqlite3
from sqlite3 import Error

def init_conn(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print ("Connection established!")
    except Error as e:
        print (e)
        print ("Connection failed!")
    return conn    

def init_tables(connection):
    sql = "CREATE TABLE IF NOT EXISTS userLoginMessage( id integer PRIMARY KEY, login text NOT NULL, message text NOT NULL);"
    connection.execute(sql)

def prepareDb(name):
    conn = init_conn(name)
    init_tables(conn)
    conn.close()

def getLoginsAndMessages(name):
    connection = init_conn(name)
    sql = "SELECT login, message FROM userLoginMessage;"
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    connection.close()

    return rows

def generateUsersHTMLTable(rows):
    usersTable = "<table>"
    for row in rows:
        usersTable += "<tr>"
        for cell in row:
            usersTable += "<td>" + str(cell) + "</td>"
        usersTable += "</tr>"
    usersTable += "</table>"
    return usersTable

def registerUserMessage(db, login, message):
    connection = init_conn(db)
    sql = "INSERT INTO userLoginMessage(`login`, `message`) VALUES('{}', '{}')".format(login + ":", message)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()