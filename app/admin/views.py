from flask_jwt import jwt_required, current_identity
from . import admin
from app.model.authenticate_user import auth
from app.model.db import db
from app.model.user_object import User
from flask import jsonify, request, Response
from werkzeug.security import generate_password_hash, check_password_hash

# TODO Verbesserung Token basiertes Login System https://realpython.com/token-based-authentication-with-flask/

import secrets
import json
# file: server/app/admin/views.py
@admin.route('/protected')
#@jwt_required()
@auth.login_required
def protected():
    return "Hello, {}!".format(auth.current_user())

@auth.login_required
@admin.route('/users', methods=['GET'])
def get_users():
    return jsonify([u.toJSON() for u in User.query.all()])

@auth.login_required
@admin.route('/create', methods=['POST'])
def add_users():
    content = request.json
    role = content["role"]
    if role == "owner":
        return Response("{'error':'cannot create a new owner'}", status=403, mimetype='application/json')
    token = secrets.token_urlsafe(64)
    u = User(username=content["username"], token=token, role=role)
    db.session.add(u)
    db.session.commit()
    return jsonify([u.toJSON()])