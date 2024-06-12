#!/usr/bin/env python3
"""
Create module basic Flask app
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello() -> str:
    """say welcome to the root path"""
    return jsonify({'message': 'Bienvenue'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
