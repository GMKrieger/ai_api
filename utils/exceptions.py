"""
exception module - defines a set of custom exception to be used by the application api.
"""


class CustomException(Exception):
    def __init__(self, text):
        super().__init__(self.__class__.__name__ + " - " + text)


class IncorrectValueException(CustomException):
    code = 400


class IncorrectTypeException(CustomException):
    code = 405


class EntityNotFoundException(CustomException):
    code = 404
