#!/usr/bin/python3
"""
    Filter cities by state
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

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
    sql = """SELECT cities.name FROM cities
    LEFT JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC"""
    params = (mysql_state,)
    c.execute(sql, params)

    rows = c.fetchall()
    for row in rows:
        print(row[0], end=", " if row != rows[-1] else "\n")

    db.close()
