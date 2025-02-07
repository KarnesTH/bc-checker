import os

from flask import Flask, jsonify
from flask_cors import CORS
from models.models import Material, db
from sqlalchemy.exc import SQLAlchemyError
from utils.utils import material_to_dict

app = Flask(__name__)
CORS(app)

db_path = os.path.join(app.instance_path, 'materials.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Shows the status of the service"""
    return jsonify({'status': 'ok', "message": "Service is running"})

@app.route('/api/materials')
def get_materials():
    """Returns all materials with their latest prices"""
    try:
        materials = Material.query.all()

        if not materials:
            return jsonify({'message': 'No materials found'}), 404

        return jsonify([material_to_dict(m) for m in materials])
    except SQLAlchemyError as e:
        return jsonify({'message': f'Failed to fetch materials: {e}'}), 500

@app.route('/api/materials/<int:material_id>')
def get_material(material_id):
    """Returns details for a specific material"""
    try:
        material = db.session.get(Material, material_id)

        if not material:
            return jsonify({'message': 'Material not found'}), 404

        return jsonify(material_to_dict(material))
    except SQLAlchemyError as e:
        return jsonify({'message': f'Failed to fetch material: {e}'}), 500

@app.route('/api/materials/search/<string:query>')
def search_materials(query):
    """Searches for materials by name"""
    try:
        materials = Material.query.filter(Material.name.ilike(f'%{query}%')).all()

        if not materials:
            return jsonify({'message': 'No materials found'}), 404

        return jsonify([material_to_dict(m) for m in materials])
    except SQLAlchemyError as e:
        return jsonify({'message': f'Failed to fetch materials: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
