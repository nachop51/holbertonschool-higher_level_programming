#!/usr/bin/python3
"""
    This module deletes all objects that
    contains the letter a from a database
"""
if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine, select
    from sqlalchemy.orm import Session

    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    mysql_db = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_user, mysql_pass, mysql_db), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        query = select(City, State).filter(
            City.state_id == State.id).order_by(City.id)
        result = session.execute(query).all()
        for row in result:
            # This way of doing it, returns a tuple
            # with the first element being the city
            # and the second element being the state
            # print(row)
            print(f"{row[1].name}: {row[0].id} {row[0].name}]")
