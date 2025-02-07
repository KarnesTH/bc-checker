from datetime import UTC, datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Material(db.Model):
    """
    Represents a building material.
    Ein Baustoff mit seinen Grundeigenschaften.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    unit = db.Column(db.String(20))
    created = db.Column(db.DateTime, default=datetime.now(UTC))
    prices = db.relationship('Price', backref='material', lazy=True)

    def __repr__(self):
        return f'<Material {self.name}>'

class Price(db.Model):
    """
    Represents a price entry for a material.
    Preiseintrag für einen Baustoff von einem bestimmten Händler.
    """
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    vendor = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime, default=datetime.now(UTC))
    material_id = db.Column(db.Integer, db.ForeignKey('material.id'), nullable=False)

    def __repr__(self):
        return f'<Price {self.amount} for material {self.material_id}>'
