"""
Python module defining swagger endpoint for easy of use and demonstration applications

Created by: Gustavo Krieger, 2018
"""

from resources.ai.swagger import schemas

POST_TRAINORD = {
    'tags': ['Load'],
    'description': 'Returns a JSON object',
    'parameters': [
        {
            'name': 'dataset',
            'description': 'Dataset to upload',
            'in': 'formData',
            'required': True,
            'type': 'file'
        },
        {
            'name': 'results',
            'description': 'Results to upload',
            'in': 'formData',
            'required': True,
            'type': 'file'
        }
    ],
    'responses': {
        '200': {
            'description': 'OK',
            'schema': schemas.TrainResponse
        },
        '400': {
            'description': 'Validation error'
        },
        '404': {
            'description': 'Entity not found'
        },
        '405': {
            'description': 'Method not allowed'
        }
    }
}

POST_TRAINPRANK = {
    'tags': ['Load'],
    'description': 'Returns a JSON object',
    'parameters': [
        {
            'name': 'dataset',
            'description': 'Dataset to upload',
            'in': 'formData',
            'required': True,
            'type': 'file'
        },
        {
            'name': 'results',
            'description': 'Results to upload',
            'in': 'formData',
            'required': True,
            'type': 'file'
        }
    ],
    'responses': {
        '200': {
            'description': 'OK',
            'schema': schemas.TrainResponse
        },
        '400': {
            'description': 'Validation error'
        },
        '404': {
            'description': 'Entity not found'
        },
        '405': {
            'description': 'Method not allowed'
        }
    }
}


POST_PREDICT = {
    'tags': ['Predict'],
    'description': 'Returns a JSON object',
    'parameters': [
        {
            'name': 'dataset',
            'description': 'Dataset to upload',
            'in': 'formData',
            'required': True,
            'type': 'file'
        },
        {
            'name': 'info',
            'description': 'ID of model to predict for.',
            'in': 'formData',
            'required': True,
            'type': 'string'
        }
    ],
    'responses': {
        '200': {
            'description': 'OK',
            'schema': schemas.PredictResponse
        },
        '400': {
            'description': 'Validation error'
        },
        '404': {
            'description': 'Entity not found'
        },
        '405': {
            'description': 'Method not allowed'
        }
    }
}
