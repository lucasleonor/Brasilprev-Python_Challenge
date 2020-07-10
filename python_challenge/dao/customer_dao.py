from python_challenge.model.customer import Customer
from python_challenge.setup.setup_db import db


class CustomerDAO:
    def get(self, customer_id: int) -> Customer:
        model = db.session.query(Customer).get(customer_id)
        return model

    def add(self, customer: Customer) -> Customer:
        db.session.add(customer)
        db.session.commit()
        return customer

    def update(self, customer: Customer) -> Customer:
        model: Customer = db.session.query(Customer).get(customer.id)
        model.name = customer.name
        model.document = customer.document
        model.active = customer.active
        db.session.commit()
        return model
