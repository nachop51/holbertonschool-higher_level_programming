#!/usr/bin/python3
"""
    This module lists one state object
    from the databse hbtn_0e_6_usa
"""
if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import Session
    from sqlalchemy import select

    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    mysql_db = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_user, mysql_pass, mysql_db), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        query = select(State).order_by(State.id)
        result = session.execute(query).first()
        if result is not None:
            print(f"{result[0].id}: {result[0].name}")
        else:
            print("Nothing")
