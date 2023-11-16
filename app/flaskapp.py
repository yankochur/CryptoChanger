from flask import Flask
from app.main.views import main as main_template
from app.templates import main


def create_app():
    app = Flask(__name__)

    def register_blueprints():
        app.register_blueprint(main_template)

    register_blueprints()

    return app

