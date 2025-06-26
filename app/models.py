
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

#sert à initialiser une instance de SQLAlchemy dans une application
db = SQLAlchemy()

class Etudiant(db.Model):
    __tablename__ = 'etudiant'
    id_etudiant = db.Column(db.Integer, primary_key=True)
    nom_etudiant = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    filiere = db.Column(db.String(50), nullable=False)
    promo = db.Column(db.Integer, nullable=False)
    login = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # One student → many stages
    stages = db.relationship('Stage', backref='etudiant', lazy=True)


class Entreprise(db.Model):
    __tablename__ = 'entreprise'
    id_entreprise = db.Column(db.Integer, primary_key=True)
    nom_entreprise = db.Column(db.String(100), nullable=False)
    lieu = db.Column(db.String(100), nullable=False)
    logo = db.Column(db.String(200))

    # One company → many stages
    stages = db.relationship('Stage', backref='entreprise', lazy=True)

class Domaine(db.Model):
    __tablename__ = 'domaine'
    id_domaine = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False, unique=True)

    # One domaine → many stages
    stages = db.relationship('Stage', backref='domaine', lazy=True)


class Stage(db.Model):
    __tablename__ = 'stage'
    id_stage = db.Column(db.Integer, primary_key=True)
    duree = db.Column(db.Integer, nullable=False)


    # Foreign keys
    id_etudiant = db.Column(db.Integer, db.ForeignKey('etudiant.id_etudiant'), nullable=False)
    id_entreprise = db.Column(db.Integer, db.ForeignKey('entreprise.id_entreprise'), nullable=False)
    id_domaine = db.Column(db.Integer, db.ForeignKey('domaine.id_domaine'), nullable=False)
