from flask import Flask
from .models import db
from .routes import bp

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///totallystage.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'dev'

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(bp)
    return app

