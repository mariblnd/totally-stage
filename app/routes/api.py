from flask import Blueprint, jsonify, request, abort
from app.models import Stage, Domaine, Entreprise, Etudiant, db

api_bp = Blueprint('api_bp', __name__, url_prefix='/api')

# ----------- STAGES CRUD -----------
@api_bp.route('/stages', methods=['GET'])
def get_stages():
    stages = Stage.query.all()
    result = []
    for stage in stages:
        result.append({
            'id': stage.id_stage,
            'duree': stage.duree,
            'domaine': stage.domaine.nom,
            'entreprise': stage.entreprise.nom_entreprise,
            'etudiant': f"{stage.etudiant.prenom} {stage.etudiant.nom_etudiant}"
        })
    return jsonify(result)

@api_bp.route('/stages/<int:stage_id>', methods=['GET'])
def get_stage(stage_id):
    stage = Stage.query.get_or_404(stage_id)
    return jsonify({
        'id': stage.id_stage,
        'duree': stage.duree,
        'domaine': stage.domaine.nom,
        'entreprise': stage.entreprise.nom_entreprise,
        'etudiant': f"{stage.etudiant.prenom} {stage.etudiant.nom_etudiant}"
    })

@api_bp.route('/stages', methods=['POST'])
def create_stage():
    data = request.get_json()
    if not data:
        abort(400, 'No input data provided')
    try:
        domaine = Domaine.query.filter_by(nom=data['domaine']).first()
        entreprise = Entreprise.query.filter_by(nom_entreprise=data['entreprise']).first()
        etudiant = Etudiant.query.filter_by(nom_etudiant=data['etudiant'].split(' ')[1], prenom=data['etudiant'].split(' ')[0]).first()
        stage = Stage(duree=data['duree'], id_domaine=domaine.id_domaine, id_entreprise=entreprise.id_entreprise, id_etudiant=etudiant.id_etudiant)
        db.session.add(stage)
        db.session.commit()
        return jsonify({'message': 'Stage created', 'id': stage.id_stage}), 201
    except Exception as e:
        abort(400, str(e))

@api_bp.route('/stages/<int:stage_id>', methods=['PUT'])
def update_stage(stage_id):
    stage = Stage.query.get_or_404(stage_id)
    data = request.get_json()
    if not data:
        abort(400, 'No input data provided')
    try:
        if 'duree' in data:
            stage.duree = data['duree']
        if 'domaine' in data:
            domaine = Domaine.query.filter_by(nom=data['domaine']).first()
            stage.id_domaine = domaine.id_domaine
        if 'entreprise' in data:
            entreprise = Entreprise.query.filter_by(nom_entreprise=data['entreprise']).first()
            stage.id_entreprise = entreprise.id_entreprise
        if 'etudiant' in data:
            etudiant = Etudiant.query.filter_by(nom_etudiant=data['etudiant'].split(' ')[1], prenom=data['etudiant'].split(' ')[0]).first()
            stage.id_etudiant = etudiant.id_etudiant
        db.session.commit()
        return jsonify({'message': 'Stage updated'})
    except Exception as e:
        abort(400, str(e))

@api_bp.route('/stages/<int:stage_id>', methods=['DELETE'])
def delete_stage(stage_id):
    stage = Stage.query.get_or_404(stage_id)
    db.session.delete(stage)
    db.session.commit()
    return jsonify({'message': 'Stage deleted'})

# ----------- ENTREPRISES CRUD (exemple GET) -----------
@api_bp.route('/entreprises', methods=['GET'])
def get_entreprises():
    entreprises = Entreprise.query.all()
    return jsonify([
        {'id': e.id_entreprise, 'nom': e.nom_entreprise, 'lieu': e.lieu, 'logo': e.logo}
        for e in entreprises
    ])

# ----------- ETUDIANTS CRUD (exemple GET) -----------
@api_bp.route('/etudiants', methods=['GET'])
def get_etudiants():
    etudiants = Etudiant.query.all()
    return jsonify([
        {'id': e.id_etudiant, 'prenom': e.prenom, 'nom': e.nom_etudiant, 'filiere': e.filiere, 'promo': e.promo}
        for e in etudiants
    ])

# ----------- DOMAINES CRUD (exemple GET) -----------
@api_bp.route('/domaines', methods=['GET'])
def get_domaines():
    domaines = Domaine.query.all()
    return jsonify([
        {'id': d.id_domaine, 'nom': d.nom}
        for d in domaines
    ])