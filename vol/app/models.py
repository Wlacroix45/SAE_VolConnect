from .extensions import db
from datetime import datetime

class Compagnie(db.Model):
    """Modèle de données pour une compagnie aérienne."""
    __tablename__ = 'Compagnie'
    id_compagnie = db.Column(db.Integer, primary_key=True)
    nom_comp = db.Column(db.String(100))

class Aeroport(db.Model):
    """Modèle de données pour un aéroport."""
    __tablename__ = 'Aeroport'
    id_aeroport = db.Column(db.Integer, primary_key=True)
    nom_aeroport = db.Column(db.String(100))
    ville = db.Column(db.String(100))
    pays = db.Column(db.String(100))

class Localiser(db.Model):
    """Modèle de données pour une localisation. La table relie les compagnies aériennes aux aéroports où elles opèrent."""
    __tablename__ = 'Localiser'
    id_aeroport = db.Column(db.Integer, db.ForeignKey('Aeroport.id_aeroport'), primary_key=True)
    id_compagnie = db.Column(db.Integer, db.ForeignKey('Compagnie.id_compagnie'),  primary_key=True)
    compagnie = db.relationship('Compagnie', backref=db.backref('Localiser', lazy="dynamic", cascade="all, delete-orphan"))
    aeroport = db.relationship('Aeroport', backref=db.backref('Localiser', lazy="dynamic", cascade="all, delete-orphan"))

class Terminal(db.Model):
    """Modèle de données pour un terminal."""
    __tablename__ = 'Terminal'
    id_terminal = db.Column(db.Integer, primary_key=True)
    nom_terminal = db.Column(db.String(100))
    id_aeroport = db.Column(db.ForeignKey('Aeroport.id_aeroport'))
    aeroport = db.relationship('Aeroport', backref=db.backref('Terminal', lazy="dynamic", cascade="all, delete-orphan"))

class Vol(db.Model):
    """Modèle de données pour un vol."""
    __tablename__ = 'Vol'
    id_vol = db.Column(db.Integer, primary_key=True)
    nom_vol = db.Column(db.String(100))
    id_compagnie = db.Column(db.Integer, db.ForeignKey('Compagnie.id_compagnie'))
    compagnie = db.relationship('Compagnie', backref=db.backref('Vol', lazy="dynamic", cascade="all, delete-orphan"))
    id_terminal_depart = db.Column(db.Integer, db.ForeignKey('Terminal.id_terminal'))
    id_terminal_arrivee = db.Column(db.Integer, db.ForeignKey('Terminal.id_terminal'))
    date_heure_depart = db.Column(db.DateTime)
    date_heure_arrivee = db.Column(db.DateTime)
    terminal_depart = db.relationship('Terminal', foreign_keys=[id_terminal_depart], backref=db.backref('Vol_depart', lazy="dynamic"))
    terminal_arrivee = db.relationship('Terminal', foreign_keys=[id_terminal_arrivee], backref=db.backref('Vol_arrivee', lazy="dynamic"))

def get_all_compagnies():
    """Récupère toutes les compagnies aériennes."""
    return Compagnie.query.all()

def create_compagnie(nom_comp):
    """Crée une nouvelle compagnie aérienne."""
    compagnie = Compagnie(nom_comp= nom_comp)
    db.session.add(compagnie)
    db.session.commit()
    return compagnie

def modify_compagnie(id,nom_comp):
    """Modifie une compagnie aérienne existante."""
    compagnie = Compagnie.query.get(id)
    if compagnie is None:
        return None
    compagnie.nom_comp = nom_comp
    db.session.commit()
    return compagnie

def get_all_aeroports():
    """Récupère tous les aéroports."""
    return Aeroport.query.all()

def create_aeroport(nom_aeroport, ville, pays):
    """Crée un nouvel aéroport."""
    aeroport = Aeroport(nom_aeroport=nom_aeroport, ville = ville, pays = pays)
    db.session.add(aeroport)
    db.session.commit()
    return aeroport

def modify_aeroport(id, nom_aeroport, ville, pays):
    """Modifie un aéroport existant."""
    aeroport = Aeroport.query.get(id)
    if aeroport is None:
        return None
    aeroport.nom_aeroport = nom_aeroport
    aeroport.ville = ville
    aeroport.pays = pays
    db.session.commit()
    return aeroport

def get_all_localiser():
    """Récupère toutes les localisations."""
    return Localiser.query.all()

def create_localiser(id_aeroport, id_compagnie):
    """Crée une nouvelle localisation."""
    existing = Localiser.query.get((id_aeroport, id_compagnie))
    if existing is not None:
        return existing
    localiser = Localiser(id_aeroport=id_aeroport, id_compagnie=id_compagnie)
    db.session.add(localiser)
    db.session.commit()
    return localiser

def delete_localiser(id_aeroport, id_compagnie):
    """Supprimme une localisation."""
    localiser = Localiser.query.get((id_aeroport, id_compagnie))
    if localiser:
        db.session.delete(localiser)
        db.session.commit()

def get_all_terminaux():
    """Récupère tous les terminaux."""
    return Terminal.query.all()

def create_terminal(nom_terminal, id_aeroport):
    """Crée un nouveau terminal."""
    terminal = Terminal(nom_terminal=nom_terminal, id_aeroport=id_aeroport)
    db.session.add(terminal)
    db.session.commit()
    return terminal

def modify_terminal(id, nom_terminal, id_aeroport):
    """Modifie un terminal existant."""
    terminal = Terminal.query.get(id)
    if terminal is None:
        return None
    terminal.nom_terminal = nom_terminal
    terminal.id_aeroport = id_aeroport
    db.session.commit()
    return terminal

def get_all_vols():
    """Récupère tous les vols."""
    return Vol.query.all()

def create_vol(nom_vol, id_compagnie, id_terminal_depart, id_terminal_arrivee, date_heure_depart, date_heure_arrivee):
    """Crée un nouveau vol."""
    if isinstance(date_heure_depart, str):
        date_heure_depart = datetime.fromisoformat(date_heure_depart)
    if isinstance(date_heure_arrivee, str):
        date_heure_arrivee = datetime.fromisoformat(date_heure_arrivee)
    
    vol = Vol(nom_vol=nom_vol, id_compagnie=id_compagnie, id_terminal_depart=id_terminal_depart, id_terminal_arrivee=id_terminal_arrivee, date_heure_depart=date_heure_depart, date_heure_arrivee=date_heure_arrivee)
    db.session.add(vol)
    db.session.commit()
    return vol

def modify_vol(id, nom_vol, id_compagnie, id_terminal_depart, id_terminal_arrivee, date_heure_depart, date_heure_arrivee):
    """Modifie un vol existant."""
    vol = Vol.query.get(id)
    if vol is None:
        return None
    if isinstance(date_heure_depart, str):
        date_heure_depart = datetime.fromisoformat(date_heure_depart)
    if isinstance(date_heure_arrivee, str):
        date_heure_arrivee = datetime.fromisoformat(date_heure_arrivee)
    vol.nom_vol = nom_vol
    vol.id_compagnie = id_compagnie
    vol.id_terminal_depart = id_terminal_depart
    vol.id_terminal_arrivee = id_terminal_arrivee
    vol.date_heure_depart = date_heure_depart
    vol.date_heure_arrivee = date_heure_arrivee
    db.session.commit()
    return vol

def get_compagnie(id):
    """Récupère une compagnie aérienne par son ID."""
    return Compagnie.query.get(id)

def get_aeroport(id):
    """Récupère un aéroport par son ID."""
    return Aeroport.query.get(id)

def get_terminal(id):
    """Récupère un terminal par son ID."""
    return Terminal.query.get(id)

def get_vol(id):
    """Récupère un vol par son ID."""
    return Vol.query.get(id)

def delete_compagnie(id):
    """Supprime une compagnie aérienne par son ID."""
    compagnie = Compagnie.query.get(id)
    if compagnie:
        db.session.delete(compagnie)
        db.session.commit()

def delete_aeroport(id):
    """Supprime un aéroport par son ID."""
    aeroport = Aeroport.query.get(id)
    if aeroport:
        db.session.delete(aeroport)
        db.session.commit()

def delete_terminal(id):
    """Supprime un terminal par son ID."""
    terminal = Terminal.query.get(id)
    if terminal:
        db.session.delete(terminal)
        db.session.commit()

def delete_vol(id):
    """Supprime un vol par son ID."""
    vol = Vol.query.get(id)
    if vol:
        db.session.delete(vol)
        db.session.commit()

def get_vols_by_compagnie(id_compagnie):
    """Récupère tous les vols d'une compagnie aérienne spécifique."""
    return Vol.query.filter_by(id_compagnie=id_compagnie).all()

def get_terminaux_by_aeroport(id_aeroport):
    """Récupère tous les terminaux d'un aéroport spécifique."""
    return Terminal.query.filter_by(id_aeroport=id_aeroport).all()



