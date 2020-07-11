from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound, BadRequest

from python_challenge.dao.customer_dao import CustomerDAO
from python_challenge.model.customer import Customer


class CustomerService:
    def __init__(self):
        self.dao = CustomerDAO()

    def find_by_id(self, customer_id: int) -> Customer:
        model = self.dao.get(customer_id)
        if model is None or not model.active:
            raise NotFound('Customer with identifier \'{}\' not found.'.format(customer_id))
        return model

    def update(self, customer: Customer, customer_id: int) -> Customer:
        self.find_by_id(customer_id)

        customer.id = customer_id
        customer.active = True
        return self.dao.update(customer)

    def delete(self, customer_id) -> None:
        customer = self.find_by_id(customer_id)
        customer.active = False
        self.dao.update(customer)

    def register_customer(self, customer: Customer) -> Customer:
        customer.active = True
        return self.dao.add(customer)
