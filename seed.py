# Fichier pour créer et remplir la bdd

from app import create_app, db
from app.models import Etudiant, Entreprise, Stage

app = create_app()

with app.app_context():

    #Création de la base de données
    db.create_all()

    #Ajout de données d'exemple
    entreprise = Entreprise(nom_entreprise="OpenAI", lieu="Paris")
    etudiant = Etudiant(nom_etudiant="Blanchard", prenom="Marie", filiere="IMAC", promo=2025)

    # Insertion des données dans la base de données
    db.session.add_all([entreprise, etudiant])
    db.session.commit()

    # Création d'un stage et association avec l'étudiant et l'entreprise
    stage = Stage(domaine="IA", duree=6, id_etudiant=etudiant.id_etudiant, id_entreprise=entreprise.id_entreprise)
    db.session.add(stage)
    db.session.commit()

    print("✓ Données insérées avec succès.")
