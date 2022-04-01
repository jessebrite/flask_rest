from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [{"name": "New Store", "items": [{"name": "my item", "price": 14.49}]}]


@app.route("/")
def home():
    return render_template("index.html")


# GET store/
@app.route("/stores")
def get_stores():
    return jsonify({"stores": stores})


# GET store/<string:name>
@app.route("/stores/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
    # raise ValueError('No such name exists')
    return jsonify({"message": "item not found"})


# POST store/ data {name:}
@app.route("/stores", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "item": request_data["item"]}
    stores.append(new_store)
    return jsonify(new_store)


# POST store/<string:name/item>
@app.route("/stores/<string:name>/items", methods=["POST"])
def create_item_in_store(name):
    request_data = request.get_json()

    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return jsonify(new_item)

    return jsonify({"message": "store no found"})


# GET store/<string:name/item>
@app.route("/stores/<string:name>/items")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify({"items": store["items"]})
    return jsonify({"message": "item not found"})


app.run(port=5000, debug=True)
