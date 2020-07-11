from flask import request
from flask_restplus import Namespace, Resource, fields

from python_challenge.controller import remove_id, remove_key
from python_challenge.helpers import response_manager
from python_challenge.helpers.decorators.auth import auth
from python_challenge.helpers.status_code import code
from python_challenge.model.product import ProductSchema
from python_challenge.service.product_service import ProductService

namespace = Namespace('Products', path='products')
product_flask_model = namespace.model('Product', {
    'id': fields.Integer(),
    'name': fields.String(),
    'price': fields.Float()
})
pagination_model = namespace.model('ProductPagination', {
    'page': fields.Integer(),
    'per_page': fields.Integer(),
    'total': fields.Integer(),
    'pages': fields.Integer(),
    'items': fields.Nested(product_flask_model, as_list=True)
})

pagination_params = {'page': 'Current Page', 'per_page': 'Number of items per page', 'order_by': 'order by',
                     'id': 'Product id', 'name': 'Product name', 'price': 'Product price'}


@namespace.route('/<int:product_id>')
@namespace.doc(responses=response_manager.common_errors)
class ProductControllerId(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = ProductSchema()
        self.service = ProductService()

    @namespace.marshal_with(product_flask_model)
    @namespace.doc(responses=response_manager.get_by)
    def get(self, product_id):
        return self.service.find_by_id(product_id)

    @namespace.expect(product_flask_model)
    @namespace.marshal_with(product_flask_model)
    @namespace.doc(responses=response_manager.update)
    @auth
    def put(self, product_id):
        json = request.json
        remove_id(json)
        product = self.schema.load(json, partial=True)
        return self.service.update(product, product_id)


@namespace.route('')
@namespace.doc(responses=response_manager.common_errors)
class ProductController(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = ProductSchema()
        self.service = ProductService()

    @namespace.marshal_with(pagination_model)
    @namespace.doc(params=pagination_params)
    def get(self):
        params = request.args.to_dict()
        page = remove_key(params, 'page', int)
        per_page = remove_key(params, 'per_page', int)
        order_by = remove_key(params, 'order_by')
        product = self.schema.load(params, partial=True)
        return self.service.find_all(page, per_page, product, order_by)

    @namespace.expect(product_flask_model)
    @namespace.marshal_with(product_flask_model, code=201, description=code[201])
    @namespace.doc(responses=response_manager.create)
    @auth
    def post(self):
        json = request.json
        remove_id(json)
        project = self.schema.load(json, partial=True)
        return self.service.register_product(project), 201
