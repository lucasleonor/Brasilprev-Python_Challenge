from flask import request
from flask_restplus import Namespace, Resource, fields

from python_challenge.controller import remove_id
from python_challenge.model.customer import CustomerSchema
from python_challenge.service.customer_service import CustomerService

namespace = Namespace('customers')
customer_flask_model = namespace.model('Customer', {
    'id': fields.Integer,
    'name': fields.String,
    'document': fields.String
})


@namespace.route('/<int:customer_id>')
class ModelCrudId(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = CustomerSchema()
        self.service = CustomerService()

    @namespace.marshal_with(customer_flask_model)
    def get(self, customer_id):
        return self.service.find_by_id(customer_id)

    @namespace.expect(customer_flask_model)
    @namespace.marshal_with(customer_flask_model)
    def put(self, customer_id):
        json = request.json
        remove_id(json)
        customer = self.schema.load(json)
        return self.service.update(customer, customer_id)

    def delete(self, customer_id):
        self.service.delete(customer_id)
        return None, 204


@namespace.route('')
class ModelCrudRoot(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = CustomerSchema()
        self.dao = CustomerService()

    @namespace.expect(customer_flask_model)
    @namespace.marshal_with(customer_flask_model, code=201, description='CREATED')
    def post(self):
        json = request.json
        remove_id(json)
        project = self.schema.load(json)
        return self.dao.register_customer(project), 201
