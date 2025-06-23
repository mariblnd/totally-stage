from flask import Blueprint, render_template, request
from app.models import Stage, Etudiant, Entreprise
from app import db

stage_bp = Blueprint('stage_bp', __name__)

# Route pour afficher la liste des stages
@stage_bp.route('/')
def liste_stages():
    # Récupération de tous les stages depuis la base de données
    stages = Stage.query.all()
    # Rendu du template avec la liste des stages
    return render_template('index.html', stages=stages)

@stage_bp.route('/add_stage', methods=['GET', 'POST'])
def add_stage():
    if request.method == 'POST':
        # Récupération des données du formulaire
        domaine = request.form.get('domaine')
        duree = request.form.get('duree')
        id_etudiant = request.form.get('id_etudiant')
        id_entreprise = request.form.get('id_entreprise')

        # Création d'un nouvel objet Stage
        new_stage = Stage(
            domaine=domaine,
            duree=duree,
            id_etudiant=id_etudiant,
            id_entreprise=id_entreprise
        )
        db.session.add(new_stage)
        db.session.commit()
        return render_template('add_stage.html', message="Stage ajouté avec succès !", etudiants=Etudiant.query.all(), entreprises=Entreprise.query.all())

    # Cas GET : afficher le formulaire
    etudiants = Etudiant.query.all()
    entreprises = Entreprise.query.all()
    return render_template('add_stage.html', etudiants=etudiants, entreprises=entreprises)

