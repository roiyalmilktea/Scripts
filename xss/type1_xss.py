import mysql.connector
from flask import Flask


# database_info
def conn_db():
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='hostuser',
        passwd='hostuser',
        port='3306',
        db='sample1'
    )
    return conn


conn = conn_db()  # connect database
cursor = conn.cursor()  # get cursor
sql = "INSERT INTO user (names,mail) values (%s,%s);"
cursor.execute(sql, ("names", "mail"))  # thorow select
conn.commit()

sql = "SELECT * FROM sample1;"

cursor.execute(sql)
rows = cursor.fetchall()

for row in rows:
    print(row["name"])
    print(row["mail"])
