from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    sku = db.Column(db.String(50), unique=True)
    category = db.Column(db.String(100))
    prices = db.relationship('Price', backref='product', lazy=True)

class Price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(20))
    vendor = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
