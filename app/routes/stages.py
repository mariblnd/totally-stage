from flask import Blueprint, render_template, request, url_for, redirect
from app.models import Stage, Etudiant, Entreprise, Domaine
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
        domaine_nom = request.form.get('domaine_nom')
        duree = request.form.get('duree')
        etudiant_nom = request.form.get('etudiant_nom')
        entreprise_nom = request.form.get('entreprise_nom')

        # Find domain by name
        domaine = Domaine.query.filter_by(nom=domaine_nom).first()
        # Find student by name
        etudiant = Etudiant.query.filter(
            (Etudiant.prenom + ' ' + Etudiant.nom_etudiant) == etudiant_nom
        ).first()
        # Find company by name
        entreprise = Entreprise.query.filter_by(nom_entreprise=entreprise_nom).first()

        if not etudiant or not entreprise:
            # Handle error: student or company not found
            return "Student or company not found", 400

        new_stage = Stage(
            duree=duree,
            id_etudiant=etudiant.id_etudiant,
            id_entreprise=entreprise.id_entreprise,
            id_domaine=domaine.id_domaine
        )
        db.session.add(new_stage)
        db.session.commit()
        return redirect(url_for('stage_bp.liste_stages'))

    etudiants = Etudiant.query.all()
    entreprises = Entreprise.query.all()
    domaines = Domaine.query.all()
    return render_template('add_stage.html', etudiants=etudiants, entreprises=entreprises, domaines=domaines)



@stage_bp.route('/update_stage/<int:stage_id>', methods=['GET', 'POST'])
def update_stage(stage_id):
    stage = Stage.query.get_or_404(stage_id)
    etudiants = Etudiant.query.all()
    entreprises = Entreprise.query.all()
    domaines = Domaine.query.all()

    if request.method == 'POST':
        domaine_nom = request.form.get('domaine_nom')
        duree = request.form.get('duree')
        etudiant_nom = request.form.get('etudiant_nom')
        entreprise_nom = request.form.get('entreprise_nom')

        # Trouver les objets correspondants
        domaine = Domaine.query.filter_by(nom=domaine_nom).first()
        etudiant = Etudiant.query.filter(
            (Etudiant.prenom + ' ' + Etudiant.nom_etudiant) == etudiant_nom
        ).first()
        entreprise = Entreprise.query.filter_by(nom_entreprise=entreprise_nom).first()

        if not domaine or not etudiant or not entreprise:
            return "Domaine, étudiant ou entreprise non trouvé", 400

        # Mettre à jour le stage
        stage.duree = duree
        stage.id_etudiant = etudiant.id_etudiant
        stage.id_entreprise = entreprise.id_entreprise
        stage.id_domaine = domaine.id_domaine

        db.session.commit()
        return redirect(url_for('stage_bp.liste_stages'))

    return render_template(
        'update_stage.html',
        stage=stage,
        etudiants=etudiants,
        entreprises=entreprises,
        domaines=domaines
    )

@stage_bp.route('/delete_stage/<int:stage_id>', methods=['POST'])
def delete_stage(stage_id):
    stage = Stage.query.get_or_404(stage_id)
    db.session.delete(stage)
    db.session.commit()
    return redirect(url_for('stage_bp.liste_stages'))



