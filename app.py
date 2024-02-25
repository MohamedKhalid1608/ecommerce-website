from flask import Flask
from flask_restful import Api
from models import db
from resources import ProductListResource, ProductResource, CartResource, CartListResource

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return 'Welcome to the e-commerce platform!'


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:tiger@localhost/karkhana'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

api.add_resource(ProductListResource, '/products')
api.add_resource(ProductResource, '/products/<int:id>')
api.add_resource(CartResource, '/cart')
api.add_resource(CartListResource, '/cart/<int:item_id>')

if __name__ == '__main__':
    app.run(debug=True)

