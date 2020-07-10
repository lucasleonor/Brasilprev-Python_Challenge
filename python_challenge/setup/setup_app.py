from flask import Flask


def setup_app():
    app = Flask(__name__)

    from python_challenge.setup.setup_api import setup_api
    setup_api(app)

    from python_challenge.setup.setup_cors import setup_cors
    setup_cors(app)

    from python_challenge.setup.setup_db import setup_db
    setup_db(app)

    return app
