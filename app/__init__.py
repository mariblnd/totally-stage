#Ce fichier crée l'application Flask

from flask import Flask
from .models import db
from .routes.stages import stage_bp
from .routes.entreprises import entreprise_bp
from .routes.etudiants import etudiant_bp
from .routes.api import api_bp
from app.routes.auth import auth_bp


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///totallystage.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'dev'

    db.init_app(app)

    app.register_blueprint(stage_bp)
    app.register_blueprint(entreprise_bp)
    app.register_blueprint(etudiant_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(auth_bp)

    @app.before_request
    def require_login():
        from flask import session, request, redirect, url_for
        allowed_routes = ['auth_bp.login', 'auth_bp.register', 'static']
        if 'etudiant_id' not in session and request.endpoint not in allowed_routes:
            return redirect(url_for('auth_bp.login'))

    return app
