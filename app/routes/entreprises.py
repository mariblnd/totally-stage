from flask import Blueprint, render_template, request, url_for, redirect
from app.models import Stage, Etudiant, Entreprise
from app import db

entreprise_bp = Blueprint('entreprise_bp', __name__)

@entreprise_bp.route('/add_entreprise', methods=['GET', 'POST'])
def add_entreprise():
    if request.method == 'POST':
        nom_entreprise = request.form.get('nom_entreprise')
        lieu = request.form.get('lieu')
        new_entreprise = Entreprise(nom_entreprise=nom_entreprise, lieu=lieu)
        db.session.add(new_entreprise)
        db.session.commit()
        return redirect(url_for('stage_bp.add_stage'))
    return render_template('add_entreprise.html')