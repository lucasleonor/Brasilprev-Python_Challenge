from flask_sqlalchemy import Pagination
from sqlalchemy.orm import Query

from python_challenge.model.order import Order
from python_challenge.setup.setup_db import db


class OrderDAO:
    def get_all(self, customer_id: int, page: int = None, per_page: int = None, order: Order = None,
                order_by: str = None) -> Pagination:
        query: Query = db.session.query(Order) \
            .filter(Order.customer_id == customer_id)
        if order.id:
            query = query.filter(Order.id == order.id)
        if order.delivery_address:
            query = query.filter(Order.delivery_address.like("%%%s%%" % order.delivery_address))
        if order.status:
            query = query.filter(Order.status == order.status)
        if order_by is None:
            order_by = Order.id
        return query.order_by(order_by).paginate(page, per_page, error_out=False)

    def get(self, customer_id: int, order_id: int) -> Order:
        model = db.session.query(Order) \
            .filter(Order.customer_id == customer_id) \
            .filter(Order.id == order_id) \
            .first()
        return model

    def add(self, order: Order) -> Order:
        db.session.add(order)
        db.session.commit()
        return order

    def update(self, order: Order) -> Order:
        model = self.get(order.customer_id, order.id)
        model.status = order.status
        db.session.commit()
        return model
