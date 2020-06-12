from flask import Blueprint
from flask_httpauth import HTTPTokenAuth

user_service = Blueprint('user_service', __name__)
auth = HTTPTokenAuth(scheme='Bearer')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

tokens = {
    "secret-token-1": "john",
    "secret-token-2": "susan"
}

@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]

@auth.get_user_roles
def get_user_roles(user):
    print(user)
    if user == "john":
        return ["admin","user"]
    return ["user"]


@user_service.route('/admin')
@auth.login_required(role='admin')
def admins_only():
    return "Hello {}, you are an admin!".format(account_api.current_user())