from flask_cors import CORS
from python_challenge.config.config_loader import cors as cors_config


def setup_cors(app):
    if cors_config:
        origins = []
        for origin in cors_config['allow']:
            origins.append(origin)
        cors = CORS(app, origins=origins)
    else:
        cors = CORS(app)
    return cors
