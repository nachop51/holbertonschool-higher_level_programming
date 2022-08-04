#!/usr/bin/python3
import sys
import MySQLdb

mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
mysql_db = sys.argv[3]
mysql_state = sys.argv[4]


db = MySQLdb.connect(
    host="localhost",
    user=mysql_username,
    passwd=mysql_password,
    db=mysql_db
)

c = db.cursor()
c.execute(f"SELECT * FROM states WHERE name LIKE '{mysql_state}' ORDER BY id ASC")
rows = c.fetchall()
for row in rows:
    print(row)

db.close()
