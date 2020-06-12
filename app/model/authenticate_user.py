from werkzeug.security import safe_str_cmp
from flask_httpauth import HTTPTokenAuth
from app.model.user_object import User

auth = HTTPTokenAuth(scheme='Bearer')

@auth.verify_token
def verify_token(token):
    u: User = User.query.filter_by(token=token).first()
    if u is not None:
        return u.username
    return None

@auth.get_user_roles
def get_user_roles(user):
    u: User = User.query.filter_by(username=user).first()
    if u is not None:
        return [u.role]
#def authenticate(username, password):
#    user = username_table.get(username, None)
#    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
#        return user

#def identity(payload):
#    user_id = payload['identity']