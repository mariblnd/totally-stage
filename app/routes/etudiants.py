from flask import Blueprint, render_template, request, url_for, redirect
from app.models import Stage, Etudiant, Entreprise
from app import db

etudiant_bp = Blueprint('etudiant_bp', __name__)


@etudiant_bp.route('/add_etudiant', methods=['GET', 'POST'])
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