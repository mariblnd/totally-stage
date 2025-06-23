#Ce fichier crée l'application Flask

from flask import Flask
from .models import db
from .routes.stages import stage_bp

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///totallystage.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'dev'

    db.init_app(app)

    app.register_blueprint(stage_bp)

    return app
