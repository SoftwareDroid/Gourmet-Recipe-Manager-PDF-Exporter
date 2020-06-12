from flask_jwt import jwt_required, current_identity
from . import admin
from app.model.authenticate_user import auth
from app.model.user_object import User
from flask import jsonify
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
