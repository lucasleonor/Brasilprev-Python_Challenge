from flask import request
from flask_restplus import Namespace, Resource, fields

from python_challenge.controller import remove_id, remove_key
from python_challenge.helpers import response_manager
from python_challenge.helpers.decorators.auth import auth
from python_challenge.helpers.status_code import code
from python_challenge.model.order import OrderSchema
from python_challenge.service.order_service import OrderService

namespace = Namespace('Orders', path='customers/<int:customer_id>/orders')
order_item_flask_model = namespace.model('OrderItem', {
    'amount': fields.Integer(),
    'product_id': fields.Integer()
})
order_flask_model = namespace.model('Order', {
    'id': fields.Integer(),
    'delivery_address': fields.String(),
    'status': fields.String(),
    'items': fields.Nested(order_item_flask_model, as_list=True)
})
pagination_model = namespace.model('OrderPagination', {
    'page': fields.Integer(),
    'per_page': fields.Integer(),
    'total': fields.Integer(),
    'pages': fields.Integer(),
    'items': fields.Nested(order_flask_model, as_list=True)
})

pagination_params = {'page': 'Current Page', 'per_page': 'Number of items per page', 'order_by': 'order by',
                     'id': 'Order id', 'delivery_address': 'Order delivery address', 'status': 'Order status'}


@namespace.route('/<int:order_id>')
@namespace.doc(responses=response_manager.common_errors)
@auth
class OrderControllerId(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = OrderSchema()
        self.service = OrderService()

    @namespace.marshal_with(order_flask_model)
    @namespace.doc(responses=response_manager.get_by)
    def get(self, customer_id, order_id):
        return self.service.find_by_id(customer_id, order_id)

    @namespace.doc(responses=response_manager.delete)
    def delete(self, customer_id, order_id):
        self.service.cancel(customer_id, order_id)
        return None, 204


@namespace.route('')
@namespace.doc(responses=response_manager.common_errors)
@auth
class OrderController(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = OrderSchema()
        self.service = OrderService()

    @namespace.marshal_with(pagination_model)
    @namespace.doc(params=pagination_params)
    def get(self, customer_id):
        params = request.args.to_dict()
        page = remove_key(params, 'page', int)
        per_page = remove_key(params, 'per_page', int)
        order_by = remove_key(params, 'order_by')
        order = self.schema.load(params, partial=True)
        return self.service.find_all(page, per_page, customer_id, order, order_by)

    @namespace.expect(order_flask_model)
    @namespace.marshal_with(order_flask_model, code=201, description=code[201])
    @namespace.doc(responses=response_manager.create)
    def post(self, customer_id):
        json = request.json
        remove_id(json)
        order = self.schema.load(json, partial=True)
        return self.service.place_order(customer_id, order), 201
