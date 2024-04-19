from flask import Flask, jsonify, request
from model import db, Cart
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

with app.app_context():
    db.init_app(app)
    db.create_all()

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    data = request.json
    cart_item = Cart(
        user_id=data['user_id'],
        product_id=data['product_id'],
        order_quantity=data['order_quantity']
    )
    db.session.add(cart_item)
    db.session.commit()
    print(cart_item)
    return jsonify({"message": "Item added to cart successfully"}), 201

@app.route('/cart_items/<int:user_id>', methods=['GET'])
def get_cart_items(user_id):
    cart_items = Cart.query.filter_by(user_id=user_id).all()
    cart_data = []
    for item in cart_items:
        cart_data.append({
            'cart_id': item.cart_id,
            'user_id': item.user_id,
            'product_id': item.product_id,
            'order_quantity': item.order_quantity
        })
    return jsonify(cart_data), 200

if __name__ == '__main__':
    app.run(debug=True)
