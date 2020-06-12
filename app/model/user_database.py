from werkzeug.security import safe_str_cmp
from flask_httpauth import HTTPTokenAuth
class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id
auth = HTTPTokenAuth(scheme='Bearer')

auth = HTTPTokenAuth(scheme='Bearer')

tokens = {
    "secret-token-1": "john",
    "secret-token-2": "susan"
}

@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]


#def authenticate(username, password):
#    user = username_table.get(username, None)
#    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
#        return user

#def identity(payload):
#    user_id = payload['identity']