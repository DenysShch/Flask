from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = "denys_shch"
api = Api(app)

jwt = JWT(app, authenticate, identity) #/auth

items =[]

class Item(Resource):
    @jwt_required()
    def get(self, name):
        return {'item': next(filter(lambda x: x['name'] == name, items), None)}

    def post(self, name):
        if next(filter(lambda x :x['name'] == name, items), None):
            return {'message': 'item exist {0}'.format(name)} ,400

        data = request.get_json() #force=True =>do not need Content-type json
        item ={'name':name, 'price': data['price']}
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return {'items' : items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)


