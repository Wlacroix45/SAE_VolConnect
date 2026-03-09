from .extensions import db
from datetime import datetime

class Compagnie(db.Model):
    __tablename__ = 'Compagnie'
    id_compagnie = db.Column(db.Integer, primary_key=True)
    nom_comp = db.Column(db.String(100))

class Aeroport(db.Model):
    __tablename__ = 'Aeroport'
    id_aeroport = db.Column(db.Integer, primary_key=True)
    nom_aeroport = db.Column(db.String(100))
    ville = db.Column(db.String(100))
    pays = db.Column(db.String(100))

class Localiser(db.Model):
    __tablename__ = 'Localiser'
    id_aeroport = db.Column(db.Integer, db.ForeignKey('Aeroport.id_aeroport'), primary_key=True)
    id_compagnie = db.Column(db.Integer, db.ForeignKey('Compagnie.id_compagnie'),  primary_key=True)
    compagnie = db.relationship('Compagnie', backref=db.backref('Localiser', lazy="dynamic", cascade="all, delete-orphan"))
    aeroport = db.relationship('Aeroport', backref=db.backref('Localiser', lazy="dynamic", cascade="all, delete-orphan"))

class Terminal(db.Model):
    __tablename__ = 'Terminal'
    id_terminal = db.Column(db.Integer, primary_key=True)
    nom_terminal = db.Column(db.String(100))
    id_aeroport = db.Column(db.ForeignKey('Aeroport.id_aeroport'))
    aeroport = db.relationship('Aeroport', backref=db.backref('Terminal', lazy="dynamic", cascade="all, delete-orphan"))

class Vol(db.Model):
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
    return Compagnie.query.all()

def create_compagnie(nom_comp):
    compagnie = Compagnie(nom_comp= nom_comp)
    db.session.add(compagnie)
    db.session.commit()
    return compagnie

def modify_compagnie(id,nom_comp):
    compagnie = Compagnie.query.get(id)
    if compagnie is None:
        return None
    compagnie.nom_comp = nom_comp
    db.session.commit()
    return compagnie

def get_all_aeroports():
    return Aeroport.query.all()

def create_aeroport(nom_aeroport, ville, pays):
    aeroport = Aeroport(nom_aeroport=nom_aeroport, ville = ville, pays = pays)
    db.session.add(aeroport)
    db.session.commit()
    return aeroport

def modify_aeroport(id, nom_aeroport, ville, pays):
    aeroport = Aeroport.query.get(id)
    if aeroport is None:
        return None
    aeroport.nom_aeroport = nom_aeroport
    aeroport.ville = ville
    aeroport.pays = pays
    db.session.commit()
    return aeroport

def get_all_localiser():
    return Localiser.query.all()

def create_localiser(id_aeroport, id_compagnie):
    localiser = Localiser(id_aeroport=id_aeroport, id_compagnie=id_compagnie)
    db.session.add(localiser)
    db.session.commit()
    return localiser

def get_all_terminaux():
    return Terminal.query.all()

def create_terminal(nom_terminal, id_aeroport):
    terminal = Terminal(nom_terminal=nom_terminal, id_aeroport=id_aeroport)
    db.session.add(terminal)
    db.session.commit()
    return terminal

def modify_terminal(id, nom_terminal, id_aeroport):
    terminal = Terminal.query.get(id)
    if terminal is None:
        return None
    terminal.nom_terminal = nom_terminal
    terminal.id_aeroport = id_aeroport
    db.session.commit()
    return terminal

def get_all_vols():
    return Vol.query.all()

def create_vol(nom_vol, id_compagnie):
    vol = Vol(nom_vol=nom_vol, id_compagnie=id_compagnie)
    db.session.add(vol)
    db.session.commit()
    return vol

def modify_vol(id, nom_vol, id_compagnie):
    vol = Vol.query.get(id)
    if vol is None:
        return None
    vol.nom_vol = nom_vol
    vol.id_compagnie = id_compagnie
    db.session.commit()
    return vol


def get_all_partir():
    return Partir.query.all()

def create_partir(id_terminal, id_vol, date_heure_depart):
    if isinstance(date_heure_depart, str):
        date_heure_depart = datetime.fromisoformat(date_heure_depart)
    partir = Partir(id_terminal=id_terminal, id_vol=id_vol, date_heure_depart=date_heure_depart)
    db.session.add(partir)
    db.session.commit()
    return partir

def get_all_arriver():
    return Arriver.query.all()

def create_arriver(id_terminal, id_vol, date_heure_arrivee):
    if isinstance(date_heure_arrivee, str):
        date_heure_arrivee = datetime.fromisoformat(date_heure_arrivee)
    arrivee = Arriver(id_terminal=id_terminal, id_vol=id_vol, date_heure_arrivee=date_heure_arrivee)
    db.session.add(arrivee)
    db.session.commit()
    return arrivee

def get_compagnie(id):
    return Compagnie.query.get(id)

def get_aeroport(id):
    return Aeroport.query.get(id)

def get_terminal(id):
    return Terminal.query.get(id)

def get_vol(id):
    return Vol.query.get(id)

def delete_compagnie(id):
    compagnie = Compagnie.query.get(id)
    if compagnie:
        db.session.delete(compagnie)
        db.session.commit()

def delete_aeroport(id):
    aeroport = Aeroport.query.get(id)
    if aeroport:
        db.session.delete(aeroport)
        db.session.commit()

def delete_terminal(id):
    terminal = Terminal.query.get(id)
    if terminal:
        db.session.delete(terminal)
        db.session.commit()

def delete_vol(id):
    vol = Vol.query.get(id)
    if vol:
        db.session.delete(vol)
        db.session.commit()

def get_vols_by_compagnie(id_compagnie):
    return Vol.query.filter_by(id_compagnie=id_compagnie).all()

def get_terminaux_by_aeroport(id_aeroport):
    return Terminal.query.filter_by(id_aeroport=id_aeroport).all()

def get_departs_by_terminal(id_terminal):
    departs = Partir.query.filter_by(id_terminal=id_terminal).all()
    result = []
    for depart in departs:
        vol = Vol.query.get(depart.id_vol)
        result.append({
            "id_vol": vol.id_vol,
            "nom_vol": vol.nom_vol,
            "id_compagnie": vol.id_compagnie,
            "date_heure_depart": depart.date_heure_depart
        })
    return result

def get_arrivees_by_terminal(id_terminal):
    arrivees = Arriver.query.filter_by(id_terminal=id_terminal).all()
    result = []
    for arrivee in arrivees:
        vol = Vol.query.get(arrivee.id_vol)
        result.append({
            "id_vol": vol.id_vol,
            "nom_vol": vol.nom_vol,
            "id_compagnie": vol.id_compagnie,
            "date_heure_arrivee": arrivee.date_heure_arrivee
        })
    return result