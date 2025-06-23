from flask import Blueprint, render_template
from app.models import Stage

stage_bp = Blueprint('stage_bp', __name__)

# Route pour afficher la liste des stages
@stage_bp.route('/')
def liste_stages():
    # Récupération de tous les stages depuis la base de données
    stages = Stage.query.all()
    # Rendu du template avec la liste des stages
    return render_template('index.html', stages=stages)

# @stage_bp.route('/add')
# def add_stage():
    # Cette route pourrait être utilisée pour ajouter un nouveau stage

    #Je te laisse créer le formulaire et la logique pour add un stage
