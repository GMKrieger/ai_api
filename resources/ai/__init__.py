"""
api module
    
    A package that defines the api resources.
    This resources define the endpoints of the system.
    This init file loads all resources on the api and declares their respective
    URL. Removing any of them will remove the associated functionality from the api.
    More info on each endpoint, their working and purpose can be found on their
    respective modules.
"""
from . import train_prank, train_ord, predict_model


# register api resources here
def register_api_resources(api):
    """
    An entry point to register the rest api resources.
    
    This function is called by the "api.urls.register_api_resource" function
    on the app initialization.
    :param api: An "flask_restful_swagger_2.API" object instance.
    """
    api.add_resource(train_prank.TrainPrank, '/train/prank/')
    api.add_resource(train_ord.TrainOrd, '/train/ord/')
    api.add_resource(predict_model.PredictModel, '/predict/')
