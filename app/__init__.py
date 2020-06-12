# file: server/app/__init__.py
from flask import Flask
from flask_jwt import JWT
from werkzeug.security import safe_str_cmp

from app.admin import admin
#from app.model.user_database import authenticate, identity
# skipping over jwt authenticate() and identity() creation
# https://pythonhosted.org/Flask-JWT/
# ...

app = Flask(__name__)

app.config.from_object('config')

#jwt = JWT(app, authenticate, identity)
app.register_blueprint(admin, url_prefix='/admin3')