# TODO
"""
validation module - Provides an utility function that validate types in the request parameters. 
"""
import webargs
from webargs import flaskparser

# TODO: comment.
FIELD_CONSTRUCTOR = dict(integer=webargs.fields.Int,
                         double=webargs.fields.Float,
                         number=webargs.fields.Number,
                         string=webargs.fields.String,
                         boolean=webargs.fields.Boolean)


def create_args(swagger_dict):
    # TODO:
    """
    
    :param swagger_dict: TODO:
    :return: ??????
    """
    parameters = swagger_dict["parameters"]
    return_dict = dict()
    # TODO: comments.
    for parameter in parameters:
        # TODO: comments.
        if parameter["in"] == "query":
            constructor = FIELD_CONSTRUCTOR[parameter["type"]]
            args = dict(validate=[])
            keys = parameter.keys()
            # TODO: comments.
            if "required" in keys and parameter["required"]:
                args["required"] = True
            # TODO: comments.
            if "minimum" in keys:
                minimum = parameter["minimum"]
                args["validate"].append(lambda x: x >= minimum)
            # TODO: comments.
            if "maximum" in keys:
                maximum = parameter["maximum"]
                args["validate"].append(lambda x: x <= maximum)
            # TODO: comments.
            if "enum" in keys:
                enum = parameter["enum"]
                args["validate"].append(lambda x: x in enum)
            # TODO: comments.
            return_dict[parameter["name"]] = constructor(**args)
    return return_dict


@flaskparser.parser.error_handler
def handle_request_parsing_error(err):
    """
    TODO:
    :param err: TODO: 
    :return: TODO:
    """
    flaskparser.abort(400, errors=err.messages)
