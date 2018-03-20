from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
stores = [
    {
        'name':'denys',
        'items': [
            {
                'name':'chair',
                'price': 2032.56
            }
        ]
    }
]

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/store' , methods=['POST'])
def create_store():
  request_data = request.get_json()
  new_store = {
    'name':request_data['name'],
    'items':[]
  }
  stores.append(new_store)
  return jsonify(new_store)

@app.route('/store/<string:name>')
def get_store(name):
    for i in stores:
        if  i['name'] == name:
            return jsonify(i)
    return jsonify({'error':'Store not found'})



@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})


@app.route('/store/<string:name>/item' , methods=['POST'])
def create_item_in_store(name):
  request_data = request.get_json()
  for store in stores:
    if store['name'] == name:
        new_item = {
            'name': request_data['name'],
            'price': request_data['price']
        }
        store['items'].append(new_item)
        return jsonify(new_item)
  return jsonify ({'message' :'store not found'})

@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for i in stores:
        if  i['name'] == name:
            return jsonify({'items':i['items']})
    return jsonify({'error':'Store not found'})

if __name__ == '__main__':
    app.run(port=5000)
