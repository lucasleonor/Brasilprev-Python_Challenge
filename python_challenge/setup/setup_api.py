from flask import Blueprint
from flask_restplus import Api

from python_challenge.config.config_loader import app_prefix
from python_challenge.controller import customer_controller


def setup_api(app):
    blueprint = Blueprint('api', __name__, url_prefix=app_prefix)
    api = Api(blueprint)
    app.register_blueprint(blueprint)

    api.add_namespace(customer_controller.namespace)
    return api
