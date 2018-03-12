import pytest
from aws_utils import aws_logger
from flask_manager.loaders import load_settings_file, build_flask_app


@pytest.fixture(scope="session", autouse=True)
def aml_app():
    aws_logger.init("test")
    return build_flask_app('', load_settings_file('settings'))


@pytest.fixture
def test_client(aml_app):
    return aml_app.test_client()
