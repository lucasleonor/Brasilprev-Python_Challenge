from marshmallow_sqlalchemy import ModelSchema

from python_challenge.setup.setup_db import db


class Product(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), unique=False, nullable=False)
    price = db.Column(db.Float(2), unique=False, nullable=False)


class ProductSchema(ModelSchema):
    class Meta:
        model = Product
        sqla_session = db.session
