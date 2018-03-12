from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import os

Base = declarative_base()


class Model(Base):
    __tablename__ = 'model'
    # Here we define columns for the table risk_score
    ID = Column(Integer, primary_key=True)
    MODEL = Column(String(50), nullable=False)
    AI = Column(String(20), nullable=False)
    TIMESTAMP = Column(DateTime, nullable=False)

path = os.getcwd()
path = os.path.join(path, "db/model.db")

connection_string = "sqlite:///{path}".format(path=path)
# Create an engine that stores data in the local directory's
engine = create_engine(connection_string)

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
