# file: server/app/__init__.py
from flask import Flask
from flask_jwt import JWT
from werkzeug.security import safe_str_cmp
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.admin import admin
from app.model.db import db

#from app.model.user_database import authenticate, identity
# skipping over jwt authenticate() and identity() creation
# https://pythonhosted.org/Flask-JWT/
# ...

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

#jwt = JWT(app, authenticate, identity)
app.register_blueprint(admin, url_prefix='/admin3')