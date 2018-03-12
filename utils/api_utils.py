"""
Python module defining common auxiliary functions used by the '/search' endpoint.
"""
from flask import request as Request
import datetime, decimal
import redis
import json
import os
from werkzeug.utils import secure_filename
import numpy as np


def check_json(request: Request, data, attribute):
    """
    Checks if requested attribute is in the body. If not, add empty list to that key.
    :param data: Dictionary
    :param attribute: Name of the attribute
    :param request: a 'flask.request' object
    :return: Filled dictionary with appropriate value
    """
    if attribute in request.json:
        data[attribute] = request.json[attribute]
    else:
        data[attribute] = []

    return data[attribute]


def check_op(op):
    """
    :param op: op to be checked
    :return: op if acceptable, raise error if not
    """
    acceptable_op = ["=", ">=", "<=", "CONTAINS", "!!=", ">", "<", "<>", "IS NULL", "IS NOT NULL"]

    if op not in acceptable_op:
        raise KeyError("'op' sent ('%s') not acceptable. Please check your request." % op)

    return op


def parse_type(s):
    """
    Checks the type of 's' and adds plics to it except for NULL and NOT NULL.
    :param s: value to be checked.
    :return: Parsed value
    """
    string = "'%s'" % s
    return string.upper()


def get_redis_cli():
    """
    Creates a the redis client and returns it.
    """
    # Opens Redis
    host = os.getenv('CLIENT_SYSTEM_REDIS_URL', "localhost")
    port = os.getenv('CLIENT_SYSTEM_REDIS_PORT', "6379")
    db = os.getenv('CLIENT_SYSTEM_REDIS_DB', "0")

    r = redis.Redis(host=host, port=int(port), db=int(db))

    return r


def alchemy_encoder(obj):
    """
    JSON encoder function for SQLAlchemy special classes.
    :param obj: Special type object
    :return: Formatted object
    """
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    elif isinstance(obj, decimal.Decimal):
        return float(obj)


def alchemy_to_json(obj):
    """
    Returns JSON serialized SQLAlchemy row.
    :param obj: SQLAlchemy row
    :return: JSON object
    """
    # use special handler for dates and decimals
    return json.dumps([dict(r) for r in obj], default=alchemy_encoder)


def file_treatment(dataset, results=None):
    datasetext = os.path.splitext(dataset.filename)[1]
    path = os.getcwd()

    datasetpath = ""
    if datasetext == ".csv":
        filename = secure_filename(dataset.filename)
        datasetpath = os.path.join(path, "files/", filename)
        dataset.save(datasetpath)

    data = np.genfromtxt(datasetpath, delimiter=',')

    if results:
        resultsext = os.path.splitext(results.filename)[1]
        resultspath = ""
        if resultsext == ".csv":
            filename = secure_filename(results.filename)
            resultspath = os.path.join(path, "files/", filename)
            results.save(resultspath)

        results = np.genfromtxt(resultspath, delimiter=',')

    classes = len(np.unique(results))

    return data, results, classes
