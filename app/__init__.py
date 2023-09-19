from flask import Flask
from .main.views import main


def create_app():
    app = Flask(__name__)

    def register_blueprints():
        app.register_blueprint(main)


    register_blueprints()
    return app

