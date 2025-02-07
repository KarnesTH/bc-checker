import sys
from pathlib import Path

import pytest
from flask import Flask
from models.models import Material, Price, db
from server import get_material, get_materials, index, search_materials

backend_path = Path(__file__).parent.parent
sys.path.append(str(backend_path))

@pytest.fixture
def app():
    """Create application for the tests"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TESTING'] = True

    db.init_app(app)

    app.add_url_rule('/', view_func=index)
    app.add_url_rule('/api/materials', view_func=get_materials)
    app.add_url_rule('/api/materials/<int:material_id>', view_func=get_material)
    app.add_url_rule('/api/materials/search/<string:query>', view_func=search_materials)

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """Create test client"""
    return app.test_client()

@pytest.fixture
def sample_material(app):
    """Create a sample material with price"""
    with app.app_context():
        material = Material()
        material.name = 'Test Material'
        material.unit = 'kg'

        db.session.add(material)
        db.session.commit()

        price = Price()
        price.amount = 9.99
        price.vendor = 'Test Vendor'
        price.material_id = material.id

        db.session.add(price)
        db.session.commit()

        material = db.session.get(Material, material.id)

        return material
