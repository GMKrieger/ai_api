"""
db_mid module : a middleware that managers database connections across requests.

    opens a connection with the project relational database before starting processing each api request.
    additionally it ensures that the is closed in the end of each request.
    the connection with the relational database is passed to the kwargs endpoints argument.
"""

import os


def db_mid(func):
    def wrapper(*args, **kwargs):
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker
        from mysql4py.tables import Base

        db_connection = None
        try:
            path = os.getcwd()
            path = os.path.join(path, "db/model.db")

            path = os.getenv('CLIENT_SYSTEM_SQL_PATH', path)

            connection_string = "sqlite:///{path}".format(path=path)

            engine = create_engine(connection_string)
            # Bind the engine to the metadata of the Base class so that the
            # declaratives can be accessed through a DBSession instance
            Base.metadata.bind = engine

            DBSession = sessionmaker(bind=engine)
            db_connection = DBSession()

            kwargs['db_connection'] = db_connection

            return func(*args, **kwargs)

        finally:
            if db_connection:
                db_connection.close()

    return wrapper
