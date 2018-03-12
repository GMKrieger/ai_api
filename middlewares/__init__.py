"""
A package defining middleware decorators that can be used to wrap the request processing
of the resources that uses it.


This module contains the following sub-modules:
    db_mid:  opens a connection with the project database before starting processing each api request.
             additionally in the end of each request it closes the opened connection.
             the connection with the no4j database is passed to the kwargs endpoints argument.


Created by: Gustavo Krieger, 2018
"""
from .db_mid import db_mid
