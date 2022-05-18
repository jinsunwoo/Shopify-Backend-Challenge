from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
from bson.objectid import ObjectId

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.shopify

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/add_inventory")
def add_inventory():
    return render_template("add_inventory.html")

@app.route('/api/add_warehouse', methods=['POST'])
def add_warehouse():
    warehouse_receive = request.form['warehouse_give']
    db_warehouse_list = list(db.warehouse.find({}))
    warehouse_list = []
    for warehouse in db_warehouse_list:
        location = warehouse['location']
        location = location.replace(" ", "")
        location = location.lower()
        warehouse_list.append(location)
    modified_location = warehouse_receive.replace(" ", "")
    modified_location = modified_location.lower()
    if modified_location in warehouse_list:
         return jsonify({'result': 'taken','msg':'The warehouse location you entered already exist in DB'})
    else:
        db.warehouse.insert_one({'location': warehouse_receive})
        return jsonify({'result': 'success'})

@app.route('/api/get_warehouse', methods=['GET'])
def get_warehouse():
    db_warehouse_list = list(db.warehouse.find({}))
    warehouse_list = []
    for warehouse in db_warehouse_list:
        location = warehouse['location']
        warehouse_list.append(location)
    return jsonify({'result': 'success', 'warehouse_list': warehouse_list})

@app.route('/api/save_inventory', methods=['POST'])
def save_inventory():
    # Get data from cleint side
    name_receive = request.form['name_give']
    description_receive = request.form['description_give']
    manufacturer_receive = request.form['manufacturer_give']
    model_receive = request.form['model_give']
    barcode_receive = request.form['barcode_give']
    serial_number_receive = request.form['serial_number_give']
    category_receive = request.form['category_give']
    warehouse_location_receive = request.form['warehouse_location_give']
    quantity_receive = request.form['quantity_give']
    purchase_price_receive = request.form['purchase_price_give']
    purchase_date_receive = request.form['purchase_date_give']
    notes_receive = request.form['notes_give']
    inventory = {'name': name_receive,
                 'description': description_receive,
                 'manufacturer': manufacturer_receive,
                 'model': model_receive,
                 'barcode': barcode_receive,
                 'serial_number': serial_number_receive,
                 'category': category_receive,
                 'warehouse_location': warehouse_location_receive,
                 'quantity': quantity_receive,
                 'purchase_price': purchase_price_receive,
                 'purchase_date': purchase_date_receive,
                 'notes': notes_receive}
    # Save inventory info in DB
    db.inventory.insert_one(inventory)
    return jsonify({'result': 'success'})

@app.route('/api/put_inventory', methods=['PUT'])
def put_inventory():
    id_receive = request.form['id_give']
    name_receive = request.form['name_give']
    description_receive = request.form['description_give']
    manufacturer_receive = request.form['manufacturer_give']
    model_receive = request.form['model_give']
    barcode_receive = request.form['barcode_give']
    serial_number_receive = request.form['serial_number_give']
    category_receive = request.form['category_give']
    warehouse_location_receive = request.form['warehouse_location_give']
    quantity_receive = request.form['quantity_give']
    purchase_price_receive = request.form['purchase_price_give']
    purchase_date_receive = request.form['purchase_date_give']
    notes_receive = request.form['notes_give']
    inventory = {'name': name_receive,
                 'description': description_receive,
                 'manufacturer': manufacturer_receive,
                 'model': model_receive,
                 'barcode': barcode_receive,
                 'serial_number': serial_number_receive,
                 'category': category_receive,
                 'warehouse_location': warehouse_location_receive,
                 'quantity': quantity_receive,
                 'purchase_price': purchase_price_receive,
                 'purchase_date': purchase_date_receive,
                 'notes': notes_receive}
    db.inventory.update_one({'_id': ObjectId(id_receive)}, {"$set": inventory})
    return jsonify({'result': 'success'})

@app.route('/api/get_inventory_list', methods=['GET'])
def get_inventory_list():
    db_inventory_list = list(db.inventory.find({}))
    for inventory in db_inventory_list:
        id = str(inventory['_id'])
        inventory['_id'] = id
    return jsonify({'result': 'success', 'inventory_list': db_inventory_list})

@app.route('/api/delete_inventory', methods=['DELETE'])
def delete_inventory():
    id_receive = request.form['id_give']
    db.inventory.delete_one({'_id': ObjectId(id_receive)})
    return jsonify({'result': 'success'})

@app.route('/api/edit_inventory')
def edit_inventory():
    try:
        _id = request.args["id"]
    except KeyError:
        return "Id not present", 400 
    inventory = db.inventory.find_one({"_id": ObjectId(_id)})
    if inventory is None:
        raise Exception('No such id exist in DB')
    else:
        name = inventory['name']
        description = inventory['description']
        manufacturer = inventory['manufacturer']
        model = inventory['model']
        barcode = inventory['barcode']
        serial_number = inventory['serial_number']
        category = inventory['category']
        warehouse_location = inventory['warehouse_location']
        quantity = inventory['quantity']
        purchase_price = inventory['purchase_price']
        purchase_date = inventory['purchase_date']
        notes = inventory['notes']
        return render_template('edit_inventory.html',
                                id = _id, 
                                name = name,
                                description = description,
                                manufacturer = manufacturer,
                                model = model,
                                barcode = barcode,
                                serial_number = serial_number,
                                category = category, 
                                warehouse_location = warehouse_location, 
                                quantity = quantity, 
                                purchase_price = purchase_price, 
                                purchase_date = purchase_date,
                                notes = notes)

if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)
    