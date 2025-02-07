import os

from flask import Flask, jsonify
from flask_cors import CORS
from models.models import Product, db
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
        db.create_all()
        seed_database(app)

@app.route('/')
def index():
    return jsonify({'status': 'ok', "message": "Service is running"})

if __name__ == '__main__':
    app.run(debug=True)
