from flask_sqlalchemy import Pagination
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound, BadRequest

from python_challenge.dao.order_dao import OrderDAO
from python_challenge.model.order import Order
from python_challenge.service.customer_service import CustomerService


class OrderService:
    def __init__(self):
        self.dao = OrderDAO()
        self.customer_service = CustomerService()

    def find_all(self, page: int, per_page: int, customer_id: int, order: Order, order_by: str) -> Pagination:
        return self.dao.get_all(customer_id, page, per_page, order, order_by)

    def find_by_id(self, customer_id: int, order_id: int) -> Order:
        model = self.dao.get(customer_id, order_id)
        if model is None:
            raise NotFound(
                'Order with identifier \'{}\' not found for Customer \'{}\'.'.format(customer_id, customer_id))
        return model

    def place_order(self, customer_id: int, order: Order) -> Order:
        self.customer_service.find_by_id(customer_id)
        order.customer_id = customer_id

        return self.dao.add(order)

    def cancel(self, customer_id: int, order_id) -> Order:
        order = self.find_by_id(customer_id, order_id)

        order.status = 'CANCELED'
        return self.dao.update(order)
