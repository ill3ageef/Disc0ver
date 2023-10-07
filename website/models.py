from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.ext.associationproxy import association_proxy


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    fullname = db.Column(db.String(150))
    password = db.Column(db.String(150))
    skills = db.relationship('Skill')
    created_projects = db.relationship('Project')


class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))