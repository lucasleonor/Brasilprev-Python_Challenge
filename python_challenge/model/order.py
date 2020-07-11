from marshmallow_sqlalchemy import ModelSchema

from python_challenge.setup.setup_db import db
from python_challenge.model.order_item import OrderItem


class Order(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    delivery_address = db.Column(db.String(200), unique=False, nullable=False)
    status = db.Column(db.String(20), unique=False, nullable=False)
    customer_id = db.Column(db.Integer(), nullable=False)
    db.ForeignKeyConstraint(['customer_id'], ['customer.id'])
    items = db.relationship("OrderItem")


class OrderSchema(ModelSchema):
    class Meta:
        model = Order
        sqla_session = db.session
