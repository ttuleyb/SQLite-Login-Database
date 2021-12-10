import sqlite3

DATABASE = "userdb.db"
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

sql = """
CREATE TABLE USER (
ID INTEGER PRIMARY KEY,
email TEXT,
password TEXT);
"""

cursor.execute(sql)
connection.commit() #save changes
connection.close()