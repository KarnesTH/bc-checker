from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from services import crawler_service
from models.models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

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

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
