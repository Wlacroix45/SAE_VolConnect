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


@ns.route("/aeroports")
class AeroportCollection(Resource):
    @ns.marshal_list_with(aeroport_model)
    def get(self):
        return get_all_aeroports()

@ns.route("/localisations")
class LocaliserCollection(Resource):
    @ns.marshal_list_with(localiser_model)
    def get(self):
        return get_all_localiser()

@ns.route("/terminaux")
class TerminalCollection(Resource):
    @ns.marshal_list_with(terminal_model)
    def get(self):
        return get_all_terminaux()

@ns.route("/departs")
class PartirCollection(Resource):
    @ns.marshal_list_with(partir_model)
    def get(self):
        return get_all_partir()

@ns.route("/arrivees")
class ArriverCollection(Resource):
    @ns.marshal_list_with(arriver_model)
    def get(self):
        return get_all_arriver()

@ns.route("/vols")
class VolCollection(Resource):
    @ns.marshal_list_with(vol_model)
    def get(self):
        return get_all_vols()