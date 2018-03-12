"""
Python module defining swagger schemas for easy of use and demonstration applications

Created by: Gustavo Krieger
"""

from flask_restful_swagger_2 import Schema


class TrainResponse(Schema):
    type = "object"
    properties = {
        "model_id": {
            "type": "string",
            "required": "true"
        }
    }

    example = {
        "query_id": "acfe7d3f-7b1a-41f6-b510-2d96788b60ef",
    }


class PredictResponse(Schema):
    type = "object"
    properties = {
        "prediction": [],
    }

    example = {
        "prediction": [
            1,
            0,
            1,
            2,
            2,
            0,
            1,
            2,
            4,
            0,
            2,
            1
        ]
    }
