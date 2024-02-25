from flask_restful import Resource, reqparse
from models import db, Product, CartItem

class ProductListResource(Resource):
    def get(self):
        products = Product.query.all()
        return [product.serialize() for product in products]

class ProductResource(Resource):
    def get(self, id):
        product = Product.query.get_or_404(id)
        return product.serialize()

class CartResource(Resource):
    def get(self):
        cart_items = CartItem.query.all()
        return [cart_item.serialize() for cart_item in cart_items]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('product_id', type=int, required=True)
        parser.add_argument('quantity', type=int, required=True)
        args = parser.parse_args()

        new_cart_item = CartItem(product_id=args['product_id'], quantity=args['quantity'])
        db.session.add(new_cart_item)
        db.session.commit()
        return '', 201

    def delete(self, id):
        cart_item = CartItem.query.get_or_404(id)
        db.session.delete(cart_item)
        db.session.commit()
        return '', 204

class CartListResource(Resource):
    def get(self):
        cart_items = CartItem.query.all()
        return [cart_item.serialize() for cart_item in cart_items]