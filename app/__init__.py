# file: server/app/__init__.py
from flask import Flask
from flask_jwt import JWT
from werkzeug.security import safe_str_cmp
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.admin import admin
from app.model.db import db
import secrets

#from app.model.user_database import authenticate, identity
# skipping over jwt authenticate() and identity() creation
# https://pythonhosted.org/Flask-JWT/
# ...

def run():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app, db)
    import os
    if not os.path.exists(Config.SQLALCHEMY_DATABASE_URI):
        config.init_db(db,app)
        return


    # Init database

    print("Ich bin hier")


    #jwt = JWT(app, authenticate, identity)
    app.register_blueprint(admin, url_prefix='/admin3')

    import os
    path = os.path.abspath(os.path.dirname(__file__))
    app.run(ssl_context=(path + '/cert.pem', path + '/key.pem'))

