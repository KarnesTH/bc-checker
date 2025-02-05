from flask import Flask, jsonify
from services import crawler_service

app = Flask(__name__)

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
    app.run(debug=True)
