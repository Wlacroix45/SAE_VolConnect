from flask_restx import Resource, Namespace, abort
from .models import *
from .api_models import *
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

@ns.route("/companies/<int:id>")
@ns.response(404, 'Companie not found')
class CompanieItem(Resource):
    @ns.marshal_with(companie_model)
    def get(self,id):
        companie = get_companie(id)
        if companie is None:
            abort(404,"Companie not found")
        return companie
    
    @ns.expect(companie_input_model)
    @ns.marshal_with(companie_model)
    def put(self,id):
        companie = modify_companie(id,ns.payload["nom_comp"])
        if companie is None:
            abort(404,"Companie not found")
        return companie, 200
    
    def delete(self,id):
        delete_companie(id)
        return {}, 204

@ns.route("/aeroports")
class AeroportCollection(Resource):
    @ns.marshal_list_with(aeroport_model)
    def get(self):
        return get_all_aeroports()
    
    @ns.expect(aeroport_input_model)
    def post(self):
        create_aeroport(nom_aeroport=ns.payload["nom_aeroport"], ville=ns.payload["ville"], pays=ns.payload["pays"])
        return {}, 201

@ns.route("/aeroports/<int:id>")
@ns.response(404, 'Aeroport not found')
class AeroportItem(Resource):
    @ns.marshal_with(aeroport_model)
    def get(self,id):
        aeroport = get_aeroport(id)
        if aeroport is None:
            abort(404,"Aeroport not found")
        return aeroport       

    @ns.expect(aeroport_input_model)
    @ns.marshal_with(aeroport_model)
    def put(self,id):
        aeroport = modify_aeroport(id,ns.payload["nom_aeroport"], ns.payload["ville"], ns.payload["pays"])
        if aeroport is None:
            abort(404,"Aeroport not found")
        return aeroport, 200 
    
    def delete(self,id):
        delete_aeroport(id)
        return {}, 204

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
    
    

@ns.route("/terminaux/<int:id>")
@ns.response(404, 'Terminal not found')
class TerminalItem(Resource):
    @ns.marshal_with(terminal_model)
    def get(self,id):
        terminal = get_terminal(id)
        if terminal is None:
            abort(404,"Terminal not found")
        return terminal  

    @ns.expect(terminal_input_model)
    @ns.marshal_with(terminal_model)
    def put(self,id):
        terminal = modify_terminal(id,ns.payload["nom_terminal"], ns.payload["id_aeroport"])
        if terminal is None:
            abort(404,"Terminal not found")
        return terminal, 200 

    def delete(self,id):
        delete_terminal(id)
        return {}, 204 

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

@ns.route("/vols/<int:id>")
@ns.response(404, 'Vol not found')
class VolItem(Resource):
    @ns.marshal_with(vol_model)
    def get(self,id):
        vol = get_vol(id)
        if vol is None:
            abort(404,"Vol not found")
        return vol   
    
    @ns.expect(vol_input_model)
    @ns.marshal_with(vol_model)
    def put(self,id):
        vol = modify_vol(id,ns.payload["nom_vol"], ns.payload["id_companie"])
        if vol is None:
            abort(404,"Vol not found")
        return vol, 200  
    
    def delete(self,id):
        delete_vol(id)
        return {}, 204