from flask import Blueprint
from flask_restplus import Api

from python_challenge.config.config_loader import app_prefix
from python_challenge.controller import customer_controller, product_controller, order_controller


def setup_api(app):
    authorizations = {
        'Bearer Auth': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        },
    }
    blueprint = Blueprint('api', __name__, url_prefix=app_prefix)
    api = Api(blueprint, title='Online Store - Python Challenge',
              description='REST API for a virtual store that features Clients, Products and Orders.\n'
                          'To get passed the mock authentication just send anything in the Authorization.'
                          'The products list methods are not protected, so anyone can browse through them',
              security='Bearer Auth', authorizations=authorizations)
    app.register_blueprint(blueprint)

    api.add_namespace(customer_controller.namespace)
    api.add_namespace(product_controller.namespace)
    api.add_namespace(order_controller.namespace)
    return api
