from .db import db
from dataclasses import dataclass
import json

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    token = db.Column(db.String(128), index=True, unique=True)
    # A User can only have one role
    role = db.Column(db.String(64), index=True, unique=True)
    #password_hash = db.Column(db.String(128))

    def toJSON(self):
        return {"id": self.id,"userame": self.username,"token": self.token,"role": self.role}