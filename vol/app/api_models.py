from flask_restx import fields
from .extensions import api

companie_model = api.model("Companie",{
"id_companie": fields.Integer,
"nom_comp":fields.String
})

companie_input_model = api.model("CompanieInput",{
    "nom_comp": fields.String
})

aeroport_model = api.model("Aeroport",{
    "id_aeroport": fields.Integer,
    "nom_aeroport": fields.String,
    "ville": fields.String,
    "pays": fields.String
})

aeroport_input_model = api.model("AeroportInput",{
    "nom_aeroport": fields.Integer,
    "ville": fields.String,
    "pays": fields.String
})

localiser_model = api.model("Localiser",{
    "id_aeroport": fields.Integer,
    "id_companie": fields.Integer
})

localiser_input_model = api.model("LocaliserInput",{
    "id_aeroport": fields.Integer,
    "id_companie": fields.Integer
})


terminal_model = api.model("Terminal",{
    "id_terminal": fields.Integer,
    "nom_terminal": fields.String,
    "id_aeroport": fields.Integer
})

terminal_input_model = api.model("TerminalInput",{
    "nom_terminal": fields.String,
    "id_aeroport": fields.Integer
})

partir_model = api.model("Partir",{
    "id_terminal": fields.Integer,
    "id_vol": fields.Integer,
    "date_heure_depart": fields.DateTime
})

partir_input_model = api.model("PartirInput",{
    "id_terminal": fields.Integer,
    "id_vol": fields.Integer,
    "date_heure_depart": fields.DateTime
})

arriver_model = api.model("Arriver",{
    "id_terminal": fields.Integer,
    "id_vol": fields.Integer,
    "date_heure_arrivee": fields.DateTime
})

arriver_input_model = api.model("ArriverPut",{
    "id_terminal": fields.Integer,
    "id_vol": fields.Integer,
    "date_heure_arrivee": fields.DateTime
})

vol_model = api.model("Vol",{
    "id_vol": fields.Integer,
    "nom_vol": fields.String,
    "id_companie": fields.Integer
})

vol_input_model = api.model("Vol",{
    "nom_vol": fields.String,
    "id_companie": fields.Integer
})