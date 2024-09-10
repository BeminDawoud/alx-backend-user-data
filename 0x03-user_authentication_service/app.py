#!/usr/bin/env python3
"""flask module
"""
from flask import Flask, jsonify, request
from auth import Auth
from user import User

app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def hello_world():
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["Post"], strict_slashes=False)
def users():
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
