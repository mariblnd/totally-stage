from flask import Blueprint, render_template, request, url_for, redirect, current_app
from app.models import Entreprise
from app import db
import os

entreprise_bp = Blueprint('entreprise_bp', __name__)

@entreprise_bp.route('/add_entreprise', methods=['GET', 'POST'])
def add_entreprise():
    if request.method == 'POST':
        nom_entreprise = request.form.get('nom_entreprise')
        lieu = request.form.get('lieu')
        logo_file = request.files.get('logo')
        logo_filename = None
        if logo_file and logo_file.filename:
            logo_filename = logo_file.filename
            logo_path = os.path.join(current_app.root_path, 'static', 'logos', logo_filename)
            logo_path = os.path.abspath(logo_path)
            os.makedirs(os.path.dirname(logo_path), exist_ok=True)
            logo_file.save(logo_path)
        new_entreprise = Entreprise(nom_entreprise=nom_entreprise, lieu=lieu, logo=logo_filename)
        db.session.add(new_entreprise)
        db.session.commit()
        return redirect(url_for('stage_bp.add_stage'))
    return render_template('add_entreprise.html')