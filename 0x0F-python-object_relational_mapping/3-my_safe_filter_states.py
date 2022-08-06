#!/usr/bin/python3
"""
    This module select all the states from a given db
    Where the name starts with whatever u typed in the command line
    but this time safe
"""

if __name__ == "__main__":
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
        db=mysql_db,
        port=3306
    )

    c = db.cursor()

    sql = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    params = (mysql_state,)
    c.execute(sql, params)
    rows = c.fetchall()
    for row in rows:
        print(row)

    db.close()
