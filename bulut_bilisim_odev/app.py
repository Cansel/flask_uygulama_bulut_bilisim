from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


carts = {}

@app.route('/index_page/<user_id>', methods=['GET'])
def get_index(user_id):
    return jsonify({"index": carts.get(user_id, [])})

@app.route('/index_page/<user_id>', methods=['POST'])
def add_to_index_page(user_id):
    data = request.get_json()
    product_id = data.get("product_id")
    if product_id is None:
        return jsonify({"message": "Eksik bilgi"}), 400

    product = {"product_id": product_id, "quantity": data.get("quantity", 1)}
    if user_id not in carts:
        carts[user_id] = []

    carts[user_id].append(product)
    return jsonify({"index": carts[user_id]})

@app.route('/index_page/<user_id>', methods=['GET'])
def index_page(user_id):
    cart_content = carts.get(user_id, [])
    return render_template('index.html', user_id=user_id, cart=cart_content)

# Ürün eklemek için yeni bir rota ekleyelim
@app.route('/add_to_index_page/<user_id>', methods=['POST'])
def add_product_to_index_page(user_id):
    data = request.get_json()
    product_id = data.get("product_id")
    quantity = data.get("quantity", 1)

    if product_id is None:
        return jsonify({"message": "Eksik bilgi"}), 400

    product = {"product_id": product_id, "quantity": quantity}

    if user_id not in carts:
        carts[user_id] = []

    carts[user_id].append(product)
    return jsonify({"message": "Ürün başarıyla sepete eklendi", "index": carts[user_id]})

if __name__ == '__main__ ':
    app.run(debug=True, port=5002)
