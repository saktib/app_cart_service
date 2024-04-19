from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cart(db.Model):
    __tablename__ = 'cart'

    cart_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    order_quantity = db.Column(db.Integer, nullable=False)
