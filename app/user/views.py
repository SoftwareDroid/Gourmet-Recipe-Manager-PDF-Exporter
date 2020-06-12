from flask_jwt import jwt_required, current_identity
from . import user
from flask import request, jsonify

# file: server/app/admin/views.py



@user.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)

