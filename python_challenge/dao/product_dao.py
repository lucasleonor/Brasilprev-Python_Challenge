from flask_sqlalchemy import Pagination
from sqlalchemy.orm import Query

from python_challenge.model.product import Product
from python_challenge.setup.setup_db import db


class ProductDAO:
    def get_all(self, page: int = None, per_page: int = None, product: Product = None, order_by=None) -> Pagination:
        query: Query = db.session.query(Product)
        if product.id:
            query = query.filter(Product.id == product.id)
        if product.name:
            query = query.filter(Product.name.like("%%%s%%" % product.name))
        if product.price:
            query = query.filter(Product.price == product.price)
        if order_by is None:
            order_by = Product.id
        return query.order_by(order_by).paginate(page, per_page, error_out=False)

    def get(self, product_id: int) -> Product:
        model = db.session.query(Product).get(product_id)
        return model

    def add(self, product: Product) -> Product:
        db.session.add(product)
        db.session.commit()
        return product

    def update(self, product: Product) -> Product:
        model: Product = db.session.query(Product).get(product.id)
        model.name = product.name
        model.price = product.price
        db.session.commit()
        return model
