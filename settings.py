import os
import pkg_resources
from neomodel import config

VERSION_FILE = 'VERSION'

__version__ = pkg_resources.resource_stream(__name__, VERSION_FILE).read().decode('UTF-8')

# os system vars
flask_config = os.getenv('FLASK_CONFIG', False)
stream_logs_disable = os.getenv('STREAM_LOGS_DISABLE', False)

# Flask application instance configurations

# gunicorn variables configurations
GUNICORN_CONFIG = {
    'config_path': '.config/config.py',
    'env_vars_path': '.config/env.json'
}

# logger path configuration
LOG_MODULE = 'aws_utils.aws_logger'
LOG_GROUP = "/aml-api"

# Flask APP CONFIGS
# configuration mapper
CONFIG_NAME_MAPPER = {
    'test': 'settings.TestConfig',
    'production': 'settings.ProductionConfig',
    'local': 'settings.DevelopmentConfig'
}


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    PROPAGATE_EXCEPTIONS = True
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

    # api configurations
    API_SPEC_URL = '/specification'
    API_TITLE = 'api'

    BLUE_PRINTS = []


class TestConfig(BaseConfig):
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    pass


def on_app_initialization(app):
    print('Init app.')

    neo4j_host = os.getenv('CLIENT_SYSTEM_NEO4J_URL', "localhost")
    neo4j_user = os.getenv('CLIENT_SYSTEM_NEO4J_USER', "neo4j")
    neo4j_password = os.getenv('CLIENT_SYSTEM_NEO4J_ENCRYPTED_PASSWD', "admin")

    config.DATABASE_URL = 'bolt://{}:{}@{}:7687'.format(neo4j_user, neo4j_password, neo4j_host)

    if flask_config != 'production':
        os.environ['CLIENT_SYSTEM_REDIS_URL'] = "localhost"
        os.environ['CLIENT_SYSTEM_REDIS_PORT'] = "6379"
        os.environ['CLIENT_SYSTEM_REDIS_DB'] = "0"
        os.environ['CLIENT_SYSTEM_REDIS_THRESHOLD'] = "3600"

    connection_string = "mysql+mysqldb://{user}:{passwd}@{host}/{schema}".format(
        user=os.getenv('CLIENT_SYSTEM_MYSQL_USER', "root"),
        passwd=os.getenv('CLIENT_SYSTEM_MYSQL_ENCRYPTED_PASSWD', "password"),
        host=os.getenv('CLIENT_SYSTEM_MYSQL_URL', "localhost"),
        schema=os.getenv('CLIENT_SYSTEM_MYSQL_SCHEMA', "ingestion_db")
    )
    from neo4py.alchemy_properties import AlchemyConnectionManager
    AlchemyConnectionManager.connection_string = connection_string
