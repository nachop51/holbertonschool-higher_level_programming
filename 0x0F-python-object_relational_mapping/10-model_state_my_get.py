#!/usr/bin/python3
"""
    This module prints the State
    object with the name passed as argument
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
    mysql_state = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_user, mysql_pass, mysql_db), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        query = select(State).filter(
            State.name == mysql_state).order_by(State.id)
        result = session.execute(query).all()
    s = ""
    for row in result:
        s += f"{row[0].id}\n"
    print(s if s else "Not found\n", end="")
