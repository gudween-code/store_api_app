import os
import re

from flask import Flask, render_template
import requests
from flask_restful import Api
from flask_jwt import JWT
from flask_cors import CORS, cross_origin
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, Items
from resources.store import Store, StoreList

uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
else:
    uri = 'sqlite:///data.db'
# rest of connection code using the connection string `uri`

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')

@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')

@app.route('/items')
def hello():
    r = requests.get('https://store-api-app.herokuapp.com/items')
    return r.text

if __name__ == '__main__':
    app.run(port=5000, debug=True)