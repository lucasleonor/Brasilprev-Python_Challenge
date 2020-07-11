from sqlalchemy.exc import IntegrityError, CompileError
from werkzeug.exceptions import NotFound, BadRequest

from python_challenge.dao.product_dao import ProductDAO
from python_challenge.model.product import Product


class ProductService:
    def __init__(self):
        self.dao = ProductDAO()

    def find_all(self, page, per_page, product, order_by):
        return self.dao.get_all(page, per_page, product, order_by)

    def find_by_id(self, product_id: int) -> Product:
        model = self.dao.get(product_id)
        if model is None:
            raise NotFound('Product with identifier \'{}\' not found.'.format(product_id))
        return model

    def update(self, product: Product, product_id: int) -> Product:
        self.find_by_id(product_id)

        product.id = product_id
        return self.dao.update(product)

    def register_product(self, product: Product) -> Product:
        return self.dao.add(product)
