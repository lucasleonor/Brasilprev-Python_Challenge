from flask import Flask, Blueprint
from flask_restplus import Api
from flask_cors import CORS

from python_challenge.config.config_loader import app_prefix, cors as cors_config


def setup_api(app):
    blueprint = Blueprint('api', __name__, url_prefix=app_prefix)
    api = Api(blueprint)
    app.register_blueprint(blueprint)

    # api.add_namespace()
    return api


def setup_cors(app):
    if cors_config:
        origins = []
        for origin in cors_config['allow']:
            origins.append(origin)
        cors = CORS(app, origins=origins)
    else:
        cors = CORS(app)
    return cors


def setup_app():
    app = Flask(__name__)
    setup_api(app)
    setup_cors(app)
    return app
