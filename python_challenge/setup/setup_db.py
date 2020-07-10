from flask_sqlalchemy import SQLAlchemy

from python_challenge.config.config_loader import db_url

db = SQLAlchemy()


def setup_db(app):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url

    db.init_app(app)

    with app.app_context():
        db.create_all()
