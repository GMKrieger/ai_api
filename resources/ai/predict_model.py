"""
Python module defining save/return endpoint and auxiliary functions.

Created by: Gustavo Krieger, 2018
"""
from flask import request
from flask_restful_swagger_2 import swagger, Resource

from middlewares import db_mid
from resources.ai.swagger import paths as search_paths
from utils import validation, api_utils
from db.tables import Model
from theano.misc import pkl_utils as pkl


class PredictModel(Resource):
    """
    /save/return Endpoint. Has a GET method that returns requested list of queries.
    """
    validation_args = validation.create_args(search_paths.POST_PREDICT)
    decorators = [db_mid]

    @swagger.doc(search_paths.POST_PREDICT)
    def post(self, *args, **kwargs):
        """
        Returns a JSON with requested template based on IDs sent
        """

        dbresponse = ""
        model_id = ""

        # db connection variable
        session = kwargs["db_connection"]

        dataset = request.files['dataset']
        model_id = request.form['info']

        # check if ids list is populated
        try:
            fetch = session.query(Model).filter(Model.MODEL == model_id).one()
        finally:
            # releases the database cursor
            session.close()

        with open("models/" + fetch.MODEL + ".zip", "rb") as f:
            model = pkl.load(f)

        response = list()

        data, _, _ = api_utils.file_treatment(dataset)

        for line in data:
            response.append(int(model.pred(line)))

        return response
