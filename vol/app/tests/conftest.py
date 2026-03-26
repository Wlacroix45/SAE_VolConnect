import pytest
from flask import Flask
from app.extensions import api, db
from app.views import ns
from app.models import *
from app.api_models import *
from datetime import datetime
from pathlib import Path

@pytest.fixture
def app():
    """Crée une instance de l'application Flask pour les tests."""
    app = Flask(__name__)
    instance_dir = Path(__file__).resolve().parents[2] / "instance"
    instance_dir.mkdir(parents=True, exist_ok=True)
    db_path = instance_dir / "dbtest.sqlite3"
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["WTF_CSRF_ENABLED"] = False
    api.init_app(app)
    db.init_app(app)
    if not any(name.startswith("api_compagnie_item") for name in app.view_functions):
        api.add_namespace(ns)
    if not any(name.startswith("api_aeroport_item") for name in app.view_functions):
        api.add_namespace(ns)
    if not any(name.startswith("api_terminal_item") for name in app.view_functions):
        api.add_namespace(ns)
    if not any(name.startswith("api_vol_item") for name in app.view_functions):
        api.add_namespace(ns)
    def get_uri(base_name):
        """Permer de trouver l'URI correspondant à un nom de ressource donné."""
        for name in app.view_functions:
            if name == base_name or name.startswith(base_name + "_"):
                return name
        return base_name
    compagnie_model["uri"].endpoint = get_uri("api_compagnie_item")
    aeroport_model["uri"].endpoint = get_uri("api_aeroport_item")
    terminal_model["uri"].endpoint = get_uri("api_terminal_item")
    vol_model["uri"].endpoint = get_uri("api_vol_item")
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
    vols_data = [
        ("AF101", datetime(2026, 4, 1, 10, 0, 0), datetime(2026, 4, 1, 12, 0, 0)),
        ("AF102", datetime(2026, 4, 1, 14, 0, 0), datetime(2026, 4, 1, 16, 0, 0)),
        ("AF103", datetime(2026, 4, 2, 9, 0, 0), datetime(2026, 4, 2, 11, 0, 0))
    ]
    
    for nom_vol, dep, arr in vols_data:
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
