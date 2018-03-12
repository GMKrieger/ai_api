import json


def test_openapi_spec_json_validity(test_client):
    raw_openapi_spec = test_client.get('api/specification.json').data
    json.loads(raw_openapi_spec.decode('utf-8'))
