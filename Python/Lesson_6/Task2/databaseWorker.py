import sqlite3
from sqlite3 import Error

def init_conn(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        #print ("Connection established!")
    except Error as e:
        print (e)
        print ("Connection failed!")
    return conn    

def init_tables(connection):
    sql = "CREATE TABLE IF NOT EXISTS PCInfo( id integer PRIMARY KEY, component text NOT NULL, information text NOT NULL);"
    connection.execute(sql)

def prepareDb(name):
    conn = init_conn(name)
    init_tables(conn)
    conn.close()

def getComponentAndInformation(name):
    connection = init_conn(name)
    sql = "SELECT component, information FROM PCInfo;"
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    connection.close()

    return rows

def generatePCInfoHTMLTable(rows):
    usersTable = "<table>"
    for row in rows:
        usersTable += "<tr>"
        for cell in row:
            usersTable += "<td>" + str(cell) + "</td>"
        usersTable += "</tr>"
    usersTable += "</table>"
    return usersTable

def registerComponentAndInformation(db, component, information):
    connection = init_conn(db)
    sql = "INSERT INTO PCInfo(`component`, `information`) VALUES('{}', '{}')".format(component + ":", information)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()