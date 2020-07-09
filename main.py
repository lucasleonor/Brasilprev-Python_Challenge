from flask import Flask, Blueprint
from flask_restplus import Api
from flask_cors import CORS


def setup_api(app):
    blueprint = Blueprint('api', __name__, url_prefix="api/V1")
    api = Api(blueprint)
    app.register_blueprint(blueprint)

    # api.add_namespace()
    return api


def setup_cors(app):
    cors = CORS(app)
    return cors


def setup_app():
    app = Flask(__name__)
    setup_api(app)
    setup_cors(app)
    return app
