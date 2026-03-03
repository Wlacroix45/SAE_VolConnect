from .extensions import db

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
    companie = db.relationship('Companie', backref=db.backref ('Localiser', lazy="dynamic"))
    aeroport = db.relationship('Aeroport', backref=db.backref ('Localiser', lazy="dynamic"))

class Terminal(db.Model):
    __tablename__ = 'Terminal'
    id_terminal = db.Column(db.Integer, primary_key=True)
    nom_terminal = db.Column(db.String(100))
    id_aeroport = db.Column(db.ForeignKey('Aeroport.id_aeroport'))
    aeroport = db.relationship('Aeroport', backref=db.backref ('Terminal', lazy="dynamic"))

class Vol(db.Model):
    __tablename__ = 'Vol'
    id_vol = db.Column(db.Integer, primary_key=True)
    nom_vol = db.Column(db.String(100))
    id_companie = db.Column(db.Integer, db.ForeignKey('Companie.id_companie'))
    companie = db.relationship('Companie', backref=db.backref ('Vol', lazy="dynamic"))

class Partir(db.Model):
    __tablename__ = 'Partir'
    id_terminal = db.Column(db.Integer, db.ForeignKey('Terminal.id_terminal'), primary_key=True)
    id_vol = db.Column(db.Integer, db.ForeignKey('Vol.id_vol'), primary_key=True)
    date_heure_depart = db.Column(db.DateTime)
    terminal = db.relationship('Terminal', backref=db.backref ('Partir', lazy="dynamic"))
    vol = db.relationship('Vol', backref=db.backref ('Partir', lazy="dynamic"))

class Arriver(db.Model):
    __tablename__ = 'Arriver'
    id_terminal = db.Column(db.Integer, db.ForeignKey('Terminal.id_terminal'), primary_key=True)
    id_vol = db.Column(db.Integer, db.ForeignKey('Vol.id_vol'), primary_key=True)
    date_heure_arrivee = db.Column(db.DateTime)
    terminal = db.relationship('Terminal', backref=db.backref ('Arriver', lazy="dynamic"))
    vol = db.relationship('Vol', backref=db.backref ('Arriver', lazy="dynamic"))
