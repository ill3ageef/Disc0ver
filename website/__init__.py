import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash

db = SQLAlchemy()
DB_NAME = "database.db"

sk = {
    "BI": "Biology",
    "PH": "Physics",
    "CH": "Chemistry",
    "SS": "Social Science",
    "AS": "Astrology",
    "CS": "Computer Science",
    "NA": "Natural Science",
    "GE": "Geology",
    "ES": "Earth Science",
    "NU": "Neuro Science",
    "ME": "Medicine"
}


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'inn0v8'  # encrypt the cookies and session data
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}?check_same_thread=False'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Project

    with app.app_context():
        
        db.create_all()
        

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app