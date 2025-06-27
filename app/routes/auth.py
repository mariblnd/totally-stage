from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models import Etudiant, db

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        prenom = request.form['prenom']
        nom_etudiant = request.form['nom_etudiant']
        filiere = request.form['filiere']
        promo = request.form['promo']

        # Si le login existe déjà = message d'erreur
        if Etudiant.query.filter_by(login=login).first():
            flash("Ce nom d'utilisateur existe déjà. Choisissez-en un autre.")
            return render_template('add_etudiant.html')

        etudiant = Etudiant(
            login=login,
            prenom=prenom,
            nom_etudiant=nom_etudiant,
            filiere=filiere,
            promo=promo
        )
        etudiant.set_password(password)
        db.session.add(etudiant)
        db.session.commit()
        flash('Registration successful!')
        return redirect(url_for('auth_bp.login'))
    return render_template('add_etudiant.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        etudiant = Etudiant.query.filter_by(login=login).first()
        if etudiant and etudiant.check_password(password):
            session['etudiant_id'] = etudiant.id_etudiant
            flash('Logged in successfully!')
            return redirect(url_for('stage_bp.liste_stages'))
        else:
            flash('Invalid login or password')
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully!')
    return redirect(url_for('auth_bp.login'))  