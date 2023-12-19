from flask import Flask
from app.main.views import main as main_template
from flask_sqlalchemy import SQLAlchemy
from app.models.user import app, db
import bcrypt


def create_app():
    def register_blueprints():
        app.register_blueprint(main_template)

    register_blueprints()

    return app


with app.app_context():
    db.create_all()
