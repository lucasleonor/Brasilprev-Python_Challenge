from marshmallow_sqlalchemy import ModelSchema

from python_challenge.setup.setup_db import db


class Customer(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), unique=False, nullable=False)
    document = db.Column(db.String(200), unique=False, nullable=False)
    active = db.Column(db.Boolean(), unique=False, default=True, nullable=False)


class CustomerSchema(ModelSchema):
    class Meta:
        model = Customer
        sqla_session = db.session
