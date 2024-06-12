#!/usr/bin/env python3
"""
Create module basic Flask app
"""
from flask import Flask, jsonify, request, abort
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'], strict_slashes=False)
def hello() -> str:
    """say welcome to the root path"""
    return jsonify({'message': 'Bienvenue'}), 200


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """create a user with post methods"""
    email = request.form.get('email', None)
    password = request.form.get('password', None)
    if email and password:
        try:
            AUTH.register_user(email, password)
        except ValueError:
            return jsonify({'message': 'email already registered'}), 400
        return jsonify({'email': email, 'message': 'user created'}), 200
    return jsonify({'message': 'should have email and password'})


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def session():
    """create session post module"""
    email = request.form.get('email', None)
    password = request.form.get('password', None)
    if email and password and AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        if session_id:
            response = jsonify({'email': email, 'message': 'logged in'})
            response.set_cookie('session_id', session_id)
            return response
    abort(401)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
