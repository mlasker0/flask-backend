from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

authors = []

@app.route('/add_author', methods=['POST'])
def add_author():
    data = request.json
    authors.append(data['name'])
    return jsonify({"message": "Author added successfully"})

@app.route('/get_authors', methods=['GET'])
def get_authors():
    return jsonify(authors)

if __name__ == '__main__':
    # Ensure the app runs on the correct port in production
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
