from marshmallow import Schema, fields

from setup_db import db


class User(db.Model):
    """
    Model for User
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    role = db.Column(db.String)


class UserSchema(Schema):
    """
    Schema for User
    """
    id = fields.Int(dump_only=True)
    username = fields.Str()
    password = fields.Str()
    role = fields.Str()

