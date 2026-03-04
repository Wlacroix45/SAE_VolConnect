from .extensions import db
from datetime import datetime

class Companie(db.Model):
    __tablename__ = 'Companie'
    id_companie = db.Column(db.Integer, primary_key=True)
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
    id_companie = db.Column(db.Integer, db.ForeignKey('Companie.id_companie'),  primary_key=True)
    companie = db.relationship('Companie', backref=db.backref('Localiser', lazy="dynamic", cascade="all, delete-orphan"))
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
    id_companie = db.Column(db.Integer, db.ForeignKey('Companie.id_companie'))
    companie = db.relationship('Companie', backref=db.backref('Vol', lazy="dynamic", cascade="all, delete-orphan"))

class Partir(db.Model):
    __tablename__ = 'Partir'
    id_terminal = db.Column(db.Integer, db.ForeignKey('Terminal.id_terminal'), primary_key=True)
    id_vol = db.Column(db.Integer, db.ForeignKey('Vol.id_vol'), primary_key=True)
    date_heure_depart = db.Column(db.DateTime)
    terminal = db.relationship('Terminal', backref=db.backref('Partir', lazy="dynamic", cascade="all, delete-orphan"))
    vol = db.relationship('Vol', backref=db.backref('Partir', lazy="dynamic", cascade="all, delete-orphan"))

class Arriver(db.Model):
    __tablename__ = 'Arriver'
    id_terminal = db.Column(db.Integer, db.ForeignKey('Terminal.id_terminal'), primary_key=True)
    id_vol = db.Column(db.Integer, db.ForeignKey('Vol.id_vol'), primary_key=True)
    date_heure_arrivee = db.Column(db.DateTime)
    terminal = db.relationship('Terminal', backref=db.backref('Arriver', lazy="dynamic", cascade="all, delete-orphan"))
    vol = db.relationship('Vol', backref=db.backref('Arriver', lazy="dynamic", cascade="all, delete-orphan"))

def get_all_companies():
    return Companie.query.all()

def create_companie(nom_comp):
    companie = Companie(nom_comp= nom_comp)
    db.session.add(companie)
    db.session.commit()
    return companie

def modify_companie(id,nom_comp):
    companie = Companie.query.get(id)
    if companie is None:
        return None
    companie.nom_comp = nom_comp
    db.session.commit()
    return companie

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

def create_localiser(id_aeroport, id_companie):
    localiser = Localiser(id_aeroport=id_aeroport, id_companie=id_companie)
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

def create_vol(nom_vol, id_companie):
    vol = Vol(nom_vol=nom_vol, id_companie=id_companie)
    db.session.add(vol)
    db.session.commit()
    return vol

def modify_vol(id, nom_vol, id_companie):
    vol = Vol.query.get(id)
    if vol is None:
        return None
    vol.nom_vol = nom_vol
    vol.id_companie = id_companie
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

def get_companie(id):
    return Companie.query.get(id)

def get_aeroport(id):
    return Aeroport.query.get(id)

def get_terminal(id):
    return Terminal.query.get(id)

def get_vol(id):
    return Vol.query.get(id)

def delete_companie(id):
    companie = Companie.query.get(id)
    if companie:
        db.session.delete(companie)
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