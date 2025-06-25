from app import create_app, db
from app.models import Etudiant, Entreprise, Stage, Domaine

app = create_app()

with app.app_context():

    # Création de la base de données
    db.create_all()

    # Ajout de 50 domaines
    domaines_noms = [
        "Informatique", "Finance", "Marketing", "Ressources humaines", "Droit", "Santé", "Éducation", "Ingénierie",
        "Architecture", "Art", "Communication", "Commerce", "Gestion", "Logistique", "Tourisme", "Agroalimentaire",
        "Environnement", "Énergie", "Transport", "Automobile", "Aéronautique", "Spatial", "Biotechnologie",
        "Chimie", "Physique", "Mathématiques", "Statistiques", "Recherche", "Développement durable", "Mode",
        "Audiovisuel", "Journalisme", "Traduction", "Interprétariat", "Sécurité", "Défense", "Sport", "Culture",
        "Patrimoine", "Urbanisme", "Immobilier", "Assurance", "Banque", "Distribution", "Vente", "Publicité",
        "Relations internationales", "Sciences politiques", "Psychologie", "Sociologie", "Anthropologie", "Graphisme"
    ]
    domaines = [Domaine(nom=nom) for nom in domaines_noms]
    db.session.add_all(domaines)
    db.session.commit()
