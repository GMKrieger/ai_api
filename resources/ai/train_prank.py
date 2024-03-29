"""
Python module defining train/prank endpoint and auxiliary functions

Created by: Gustavo Krieger, 2018
"""
from flask import request
from flask_restful_swagger_2 import swagger, Resource

import uuid
import datetime
from AI.p_rank import PRank
from db.tables import Model
from middlewares import db_mid
from resources.ai.swagger import paths
from utils import api_utils, validation
from theano.misc import pkl_utils as pkl
from werkzeug import exceptions


def creation_and_training(dataset, results):
    """
    Creation and training function.
    :param dataset: dataset received from request
    :param results: results received from request
    :return: model_id for response
    """
    # Treats the received file to be used on the model
    data, results, classes = api_utils.file_treatment(dataset, results)

    # Create model based on data
    prank = PRank(n_classes=classes, n_features=data.shape[1])

    # Train the model with 10 epochs
    for i in range(10):
        for line, sentiment in zip(data, results):
            L, err = prank.train(line, sentiment)

    return prank


class TrainPrank(Resource):
    """
    /train/prank/ Endpoint. Has a POST method that returns a ID of a model trained
    based on the data sent in the body of the request.
    """
    validation_args = validation.create_args(paths.POST_TRAINPRANK)
    decorators = [db_mid]

    @swagger.doc(paths.POST_TRAINPRANK)
    def post(self, *args, **kwargs):
        """
        Trains and saves a Prank model
        :params:
        dataset: Dataset to be trained
        results: Results for supervised training
        :return: Dict with model_id to be later used for prediction
        """

        # Receives request files
        try:
            dataset = request.files['dataset']
            results = request.files['results']
        except:
            raise exceptions.NotAcceptable("You need to send a dataset and a result set.")

        # Connects to db
        session = kwargs["db_connection"]

        prank = creation_and_training(dataset, results)

        # Create variables for database entry
        model_id = str(uuid.uuid4())
        timestamp = datetime.datetime.now()

        # Save model for future use
        with open("models/" + model_id + ".zip", "wb") as f:
            pkl.dump(prank, f)

        # Create new row and add it to db
        try:
            new_model = Model(MODEL=model_id, AI="p_rank", TIMESTAMP=timestamp)

            session.add(new_model)

        finally:
            session.commit()

        # Create response
        response = dict()

        response['model_id'] = model_id

        return response
