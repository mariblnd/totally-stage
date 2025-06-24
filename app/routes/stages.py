from flask import Blueprint, render_template, request, url_for, redirect
from app.models import Stage, Etudiant, Entreprise
from app import db

stage_bp = Blueprint('stage_bp', __name__)

@stage_bp.route('/')
def liste_stages():
    # Récupération de tous les stages depuis la base de données
    sort = request.args.get('sort')
    if sort == 'desc':
        stages = Stage.query.order_by(Stage.duree.desc()).all()
    elif sort == 'asc':
        stages = Stage.query.order_by(Stage.duree.asc()).all()
    else:
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

        # Création d'un nouvel objet Stage = Permet d'ajouter une ligne dans la table Stage
        new_stage = Stage(
            domaine=domaine,
            duree=duree,
            id_etudiant=id_etudiant,
            id_entreprise=id_entreprise
        )
        db.session.add(new_stage)
        db.session.commit()
        return redirect(url_for('stage_bp.liste_stages'))
        
    
    # Cas GET : afficher le formulaire
    etudiants = Etudiant.query.all()
    entreprises = Entreprise.query.all()
    return render_template('add_stage.html', etudiants=etudiants, entreprises=entreprises)


@stage_bp.route('/update_stage/<int:stage_id>', methods=['GET', 'POST'])
def update_stage(stage_id):

    # Récupérer le stage à modifier
    stage = Stage.query.get_or_404(stage_id)

    # Récupérer la liste des étudiants / entreprises
    etudiants = Etudiant.query.all()
    entreprises = Entreprise.query.all()

    if request.method == 'POST':
        stage.domaine = request.form['domaine']
        stage.duree = request.form['duree']
        stage.id_etudiant = request.form['id_etudiant']
        stage.id_entreprise = request.form['id_entreprise']
        db.session.commit()
        return redirect(url_for('stage_bp.liste_stages'))  # index.html

    return render_template(
        'update_stage.html',
        stage=stage,
        etudiants=etudiants,
        entreprises=entreprises
    )

@stage_bp.route('/delete_stage/<int:stage_id>', methods=['POST'])
def delete_stage(stage_id):
    stage = Stage.query.get_or_404(stage_id)
    db.session.delete(stage)
    db.session.commit()
    return redirect(url_for('stage_bp.liste_stages'))

@stage_bp.route('/add_etudiant', methods=['GET', 'POST'])
def add_etudiant():
    if request.method == 'POST':
        nom_etudiant = request.form.get('nom_etudiant')
        prenom = request.form.get('prenom')
        filiere = request.form.get('filiere')
        promo = request.form.get('promo')
        new_etudiant = Etudiant(nom_etudiant=nom_etudiant, prenom=prenom, filiere=filiere, promo=promo)
        db.session.add(new_etudiant)
        db.session.commit()
        return redirect(url_for('stage_bp.add_stage'))
    return render_template('add_etudiant.html')

@stage_bp.route('/add_entreprise', methods=['GET', 'POST'])
def add_entreprise():
    if request.method == 'POST':
        nom_entreprise = request.form.get('nom_entreprise')
        lieu = request.form.get('lieu')
        new_entreprise = Entreprise(nom_entreprise=nom_entreprise, lieu=lieu)
        db.session.add(new_entreprise)
        db.session.commit()
        return redirect(url_for('stage_bp.add_stage'))
    return render_template('add_entreprise.html')