from flask import request
from flask_restful_swagger_2 import swagger, Resource
import json


class BaseEndPoint(Resource):
    __method_models__ = dict()
    
    def dispatch_request(self, *args, **kwargs):
        if request.method == 'POST':
            if request.data is not None:
                if request.data.decode("utf-8").strip() != "":
                    args = list(args)
                    data = json.loads(request.data.decode("utf-8"))
                    model = self.__method_models__.get(request.method,None)
                    
                    if model is None:
                        raise AttributeError(
                            "__method_models__ does not defines a model class"
                            " for the {} method.".format(request.method)
                        )
                    
                    data = model.from_json(data)
                    args.insert(0,data)
                    
        return super().dispatch_request(*args, **kwargs)