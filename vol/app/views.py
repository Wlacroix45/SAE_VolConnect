from flask_restx import Resource, Namespace
from .models import *
from .api_models import *
# creation du namespace, racine de tous les endpoints
ns = Namespace("api")

@ns.route("/companies")
class CompanieCollection(Resource):
    @ns.marshal_list_with(companie_model)
    def get(self):
        return get_all_companies()
    
    @ns.expect(companie_input_model)
    def post(self):
        create_companie(nom_comp=ns.payload["nom_comp"])
        return {}, 201

@ns.route("/aeroports")
class AeroportCollection(Resource):
    @ns.marshal_list_with(aeroport_model)
    def get(self):
        return get_all_aeroports()
    
    @ns.expect(aeroport_input_model)
    def post(self):
        create_aeroport(nom_aeroport=ns.payload["nom_aeroport"], ville=ns.payload["ville"], pays=ns.payload["pays"])
        return {}, 201        

@ns.route("/localisations")
class LocaliserCollection(Resource):
    @ns.marshal_list_with(localiser_model)
    def get(self):
        return get_all_localiser()
    
    @ns.expect(localiser_input_model)
    def post(self):
        create_localiser(id_aeroport=ns.payload["id_aeroport"], id_companie=ns.payload["id_companie"])
        return {}, 201
    
@ns.route("/terminaux")
class TerminalCollection(Resource):
    @ns.marshal_list_with(terminal_model)
    def get(self):
        return get_all_terminaux()
    
    @ns.expect(terminal_input_model)
    def post(self):
        create_terminal(nom_terminal=ns.payload["nom_terminal"], id_aeroport=ns.payload["id_aeroport"])
        return {}, 201

@ns.route("/departs")
class PartirCollection(Resource):
    @ns.marshal_list_with(partir_model)
    def get(self):
        return get_all_partir()
    
    @ns.expect(partir_input_model)
    def post(self):
        create_partir(id_terminal=ns.payload["id_terminal"], id_vol=ns.payload["id_vol"], date_heure_depart=ns.payload["date_heure_depart"])
        return {}, 201

@ns.route("/arrivees")
class ArriverCollection(Resource):
    @ns.marshal_list_with(arriver_model)
    def get(self):
        return get_all_arriver()

    @ns.expect(arriver_input_model)
    def post(self):
        create_arriver(id_terminal=ns.payload["id_terminal"], id_vol=ns.payload["id_vol"], date_heure_arrivee=ns.payload["date_heure_arrivee"])
        return {}, 201

@ns.route("/vols")
class VolCollection(Resource):
    @ns.marshal_list_with(vol_model)
    def get(self):
        return get_all_vols()
    
    @ns.expect(vol_input_model)
    def post(self):
        create_vol(nom_vol=ns.payload["nom_vol"], id_companie=ns.payload["id_companie"])
        return {}, 201