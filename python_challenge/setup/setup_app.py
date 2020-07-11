from flask import Flask

from python_challenge.helpers.exception_handler import handle_error


def setup_app():
    app = Flask(__name__)

    from python_challenge.setup.setup_api import setup_api
    setup_api(app)

    from python_challenge.setup.setup_cors import setup_cors
    setup_cors(app)

    from python_challenge.setup.setup_db import setup_db
    setup_db(app)

    app.register_error_handler(Exception, handle_error)
    return app
