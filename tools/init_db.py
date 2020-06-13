from app import db, app
from app.model.user_object import User
import secrets
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

def my_function():
    with app.app_context():
        db.create_all()
        token = secrets.token_urlsafe(64)
        hashed_token = generate_password_hash(token, "sha256")
        u = User(username='patrick', token=hashed_token, role="Admin")
        db.session.add(u)
        db.session.commit()
        print("Added Admin user Patrick with token:", token)

#TODO Check if file already exits create Permission and default Role Table
# Permission Table (ID, Name, Defaultlchemy tutorialValue)
# RoleToPermission (RoleID,PermissionID, Value)

my_function()