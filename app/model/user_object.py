from .db import db
from dataclasses import dataclass
import json

# One Use can have k Roles and every Role can have 0 to k permissions

user_to_roles = db.Table('user_to_roles', db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)






class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    token = db.Column(db.String(128), index=True, unique=True)
    roles = db.relationship(
        "Role",
        secondary=user_to_roles,
        back_populates="users")
    def toJSON(self):
        return {"id": self.id,"userame": self.username,"token": self.token,"role": self.role}

class PermissionToRole(db.Model):
    __tablename__ = 'permission_to_role'
    permission_name = db.Column(db.Integer, db.ForeignKey('permission.name'), primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), primary_key=True)
    value = db.Column(db.Integer)

    permission = db.relationship("Permission", back_populates="role_association")
    role = db.relationship("Role", back_populates="permission_association")

class Role(db.Model):
    __tablename__ = 'role'
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(64), index=True, unique=True)
    users = db.relationship(
        "User",
        secondary=user_to_roles,
        back_populates="roles")

    permission_association = db.relationship("PermissionToRole", back_populates="role")


class Permission(db.Model):
    __tablename__ = 'permission'
    name = db.Column(db.String(64), primary_key=True, index=True, unique=True)
    default_value = db.Column(db.Integer)
    role_association = db.relationship("PermissionToRole", back_populates="permission")


