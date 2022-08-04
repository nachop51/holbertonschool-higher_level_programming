#!/usr/bin/python3
"""
    This module select all the states from a given db
    Where the name starts with N
"""
import sys
import MySQLdb

mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
mysql_db = sys.argv[3]


db = MySQLdb.connect(
    host="localhost",
    user=mysql_username,
    passwd=mysql_password,
    db=mysql_db
)

c = db.cursor()
c.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
rows = c.fetchall()
for row in rows:
    print(row)

db.close()
