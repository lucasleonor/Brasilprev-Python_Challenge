from marshmallow_sqlalchemy import ModelSchema

from python_challenge.setup.setup_db import db


class OrderItem(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    amount = db.Column(db.Integer(), unique=False, nullable=False)
    order_id = db.Column(db.Integer(),  db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer(), db.ForeignKey('product.id'), nullable=False)
    product = db.relationship('Product')
    db.ForeignKeyConstraint(['order_id'], ['order.id'])
    db.ForeignKeyConstraint(['product_id'], ['product.id'])


class OrderItemSchema(ModelSchema):
    class Meta:
        model = OrderItem
        sqla_session = db.session
