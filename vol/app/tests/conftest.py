import pytest
from flask import Flask
from flask_restx import Api
from app.extensions import db
from app.views import ns
from app.models import *
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
    db.init_app(app)
    test_api = Api(app)
    test_api.add_namespace(ns)
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
def aeroport_test():
    """Crée un aéroport."""
    return create_aeroport("Charles de Gaulle", "Paris", "France")


@pytest.fixture
def terminal_test(aeroport_test):
    """Crée un terminal."""
    return create_terminal("Terminal 1", aeroport_test.id_aeroport)


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
def localiser_test(compagnie_test, aeroport_test):
    """Crée une localisation (la compagnie opère à l'aéroport)."""
    return create_localiser(aeroport_test.id_aeroport, compagnie_test.id_compagnie)

@pytest.fixture
def clean_db(app):
    """Assure que la base de données est propre avant chaque test."""
    yield
    db.session.remove()
    db.drop_all()
    db.create_all()
