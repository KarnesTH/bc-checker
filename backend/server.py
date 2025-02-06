import os

from flask import Flask, jsonify
from flask_cors import CORS
from models.models import Product, db
from services import crawler_service
from utils.seed_db import seed_database

app = Flask(__name__)
CORS(app)
db_path = os.path.join(app.instance_path, 'products.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True
db.init_app(app)

with app.app_context():
    if not Product.query.first():
        seed_database(app)

@app.route('/api/health')
def health_check():
    return jsonify({'status': 'ok', "message": "Service is running"})

@app.route('/api/test-crawler')
def test_crawler():
    result = crawler_service.fetch_page('https://www.google.com')
    if result:
        return jsonify({
            "status": "success",
            "title": result.title.string if result.title else "No title found"
        })
    return jsonify({"status": "error", "message": "Failed to fetch page"})

@app.route('/api/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'sku': p.sku,
        'category': p.category,
        'prices': [{
            'id': price.id,
            'price': price.price,
            'unit': price.unit,
            'vendor': price.vendor,
            'timestamp': price.timestamp.isoformat()
        } for price in p.prices]
    } for p in products])

if __name__ == '__main__':
    app.run(debug=True)
