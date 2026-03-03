from .extensions import db
class Companie(db.Model):
    id_companie = db.Column(db.Integer, primary_key=True)
    nom_comp = db.Column(db.String(100))

class Aeroport(db.Model):
    id_aeroport = db.Column(db.Integer, primary_key=True)
    nom_aeroport = db.Column(db.String(100))
    ville = db.Column(db.String(100))
    pays = db.Column(db.String(100))

class Localiser(db.Model):
    id_aeroport = db.Column(db.Integer, db.ForeignKey('Aeroport.id_aeroport'), primary_key=True)
    id_companie = db.Column(db.Integer, db.ForeignKey('Companie.id_companie'),  primary_key=True)
    companie = db.relationship('Companie', backref=db.backref ('Localiser', lazy="dynamic"))
    aeroport = db.relationship('Aeroport', backref=db.backref ('Localiser', lazy="dynamic"))
