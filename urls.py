"""
urls.py - An entry point to the url rules.
"""
from flask import Flask
from flask import json, request
from werkzeug.exceptions import HTTPException

from aws_utils import aws_logger
import settings


def register_urls(app: Flask):
    """
    An entry point to register the project url rules.
    :param app: An Flask Application instance.
    """
    register_api_resource(app)

    # application url rules should come here
    @app.route('/')
    def root():
        """
        root api route.
        :return: rendered swagger index.html
        """
        return app.send_static_file('index.html')

    # app error handler definition
    @app.errorhandler(Exception)
    def handle_error(error):
        """
        Filters any request exception raised by the api and then handles these exception correctly.

        Logs any exception raised by the api and returns an http response object
        containing the correct status code and a json error message.
        :param error: the raised exception object.
        :return: http response object.
        """
        aws_logger.logger.exception(str(error))

        response = json.jsonify(dict(error=str(error)))
        response.status_code = 500
        if hasattr(error, "code") and isinstance(error.code, int):
            response.status_code = error.code

        return response

    # for any http status code force json response
    for cls in HTTPException.__subclasses__():
        app.register_error_handler(cls, handle_error)

    # Setting CORS due to swagger-ui
    from flask_cors import CORS
    CORS(app)


def register_api_resource(app: Flask):
    """
    An entry point to register the rest api resources.

    This function is called by the "api.on_app_initialization" function
    on the app initialization.

    :param api: An "flask_restful_swagger_2.API" object instance.
    """
    # API initialization
    from flask_restful_swagger_2 import Api
    api = Api(
        app,
        title=app.config["API_TITLE"],
        api_spec_url=app.config["API_SPEC_URL"],
        api_version=settings.__version__,
        base_path='/' + app.config["API_TITLE"],
        prefix='/api'
    )

    from resources import ai
    ai.register_api_resources(api)
