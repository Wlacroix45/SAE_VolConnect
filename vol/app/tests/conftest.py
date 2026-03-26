import pytest
from flask import Flask
from app.extensions import api, db
from app.views import ns
from app.models import *
from datetime import datetime


@pytest.fixture
def app():
    """Création et configuration d'une nouvelle instance d'application pour chaque test."""
    app = Flask(__name__)
    
    # Configuration de test
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["WTF_CSRF_ENABLED"] = False
    
    # Initialisation des extensions
    api.init_app(app)
    db.init_app(app)
    api.add_namespace(ns)
    
    # Création des tables dans le contexte de l'application
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    """Permet de tester les requêtes HTTP."""
    return app.test_client()

@pytest.fixture
def app_context(app):
    """Fournit un contexte d'application pour les tests qui en ont besoin."""
    with app.app_context():
        yield app


# ==================== Insertions pour le jeux de données de test ====================

@pytest.fixture
def compagnie_test():
    """Crée une compagnie aérienne"""
    return create_compagnie("Air France")


@pytest.fixture
def compagnies_test():
    """Crée plusieurs compagnies aériennes."""
    compagnies = []
    noms = ["Air France", "Lufthansa", "KLM", "Ryanair"]
    for nom in noms:
        compagnies.append(create_compagnie(nom))
    return compagnies


@pytest.fixture
def aeroport_test():
    """Crée un aéroport."""
    return create_aeroport("Charles de Gaulle", "Paris", "France")


@pytest.fixture
def aeroports_test():
    """Crée plusieurs aéroports."""
    aeroports = []
    data = [
        ("Charles de Gaulle", "Paris", "France"),
        ("Orly", "Paris", "France"),
        ("Frankfurt", "Frankfurt", "Germany"),
        ("Amsterdam Airport", "Amsterdam", "Netherlands")
    ]
    for nom, ville, pays in data:
        aeroports.append(create_aeroport(nom, ville, pays))
    return aeroports


@pytest.fixture
def terminal_test(aeroport_test):
    """Crée un terminal."""
    return create_terminal("Terminal 1", aeroport_test.id_aeroport)


@pytest.fixture
def terminals_test(aeroport_test):
    """Crée plusieurs terminaux."""
    terminals = []
    for i in range(1, 4):
        terminals.append(create_terminal(f"Terminal {i}", aeroport_test.id_aeroport))
    return terminals


@pytest.fixture
def vol_test(compagnie_test, terminal_test):
    """Crée un vol de test."""
    return create_vol(
        nom_vol="AF101",
        id_compagnie=compagnie_test.id_compagnie,
        id_terminal_depart=terminal_test.id_terminal,
        id_terminal_arrivee=terminal_test.id_terminal,
        date_heure_depart=datetime(2026, 4, 1, 10, 0, 0),
        date_heure_arrivee=datetime(2026, 4, 1, 12, 0, 0)
    )


@pytest.fixture
def vols_test(compagnie_test, terminals_test):
    """Crée plusieurs vols de test."""
    vols = []
    flights_data = [
        ("AF101", datetime(2026, 4, 1, 10, 0, 0), datetime(2026, 4, 1, 12, 0, 0)),
        ("AF102", datetime(2026, 4, 1, 14, 0, 0), datetime(2026, 4, 1, 16, 0, 0)),
        ("AF103", datetime(2026, 4, 2, 9, 0, 0), datetime(2026, 4, 2, 11, 0, 0))
    ]
    
    for nom_vol, dep, arr in flights_data:
        vols.append(create_vol(
            nom_vol=nom_vol,
            id_compagnie=compagnie_test.id_compagnie,
            id_terminal_depart=terminals_test[0].id_terminal,
            id_terminal_arrivee=terminals_test[1].id_terminal,
            date_heure_depart=dep,
            date_heure_arrivee=arr
        ))
    return vols


@pytest.fixture
def localiser_test(compagnie_test, aeroport_test):
    """Crée une localisation (la compagnie opère à l'aéroport)."""
    return create_localiser(aeroport_test.id_aeroport, compagnie_test.id_compagnie)


# ==================== UTILITY FIXTURES ====================

@pytest.fixture
def clean_db(app):
    """Assure que la base de données est propre avant chaque test."""
    yield
    db.session.remove()
    db.drop_all()
    db.create_all()
