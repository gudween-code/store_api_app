import os

from flask import Flask
import requests
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, Items
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql//ybdakdhqfsfmht:8178dbeae542b7ada38146407ccb36c8636b6b5100a7381f62c911d059b9c946@ec2-54-74-60-70.eu-'#os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')

app.route('/hello')
def hello_world():
    return "Hello World"

@app.route('/items')
def hello():
    r = requests.get('http://127.0.0.1:5000/items')
    return r.text

if __name__ == '__main__':
    app.run(port=5000, debug=True)