from flask_restx import Resource, Namespace, abort
from .models import *
from .api_models import *
from flask import request
ns = Namespace("api")

@ns.route("/compagnies")
class CompagnieCollection(Resource):
    """Ressource pour récupérer la liste des compagnies ou en créer une nouvelle."""
    @ns.marshal_list_with(compagnie_model)
    def get(self):
        """Récupère la liste des compagnies, avec possibilité de filtrer par nom."""
        nom_comp = request.args.get('nom_comp')
        if nom_comp:
            return Compagnie.query.filter(Compagnie.nom_comp.ilike(f"%{nom_comp}%")).all()
        return get_all_compagnies()
    
    @ns.expect(compagnie_input_model)
    def post(self):
        """Crée une nouvelle compagnie."""
        create_compagnie(nom_comp=ns.payload["nom_comp"])
        return {}, 201

@ns.route("/compagnies/<int:id_compagnie>")
@ns.response(404, 'Compagnie not found')
class CompagnieItem(Resource):
    """Ressource pour récupérer, modifier ou supprimer une compagnie spécifique."""
    @ns.marshal_with(compagnie_model)
    def get(self,id_compagnie):
        """Récupère une compagnie par son ID."""
        compagnie = get_compagnie(id_compagnie)
        if compagnie is None:
            abort(404,"Compagnie not found")
        return compagnie
    
    @ns.expect(compagnie_input_model)
    @ns.marshal_with(compagnie_model)
    def put(self,id_compagnie):
        """Modifie une compagnie existante."""
        compagnie = modify_compagnie(id_compagnie,ns.payload["nom_comp"])
        if compagnie is None:
            abort(404,"Compagnie not found")
        return compagnie, 200
    
    def delete(self,id_compagnie):
        """Supprime une compagnie par son ID."""
        delete_compagnie(id_compagnie)
        return {}, 204

@ns.route("/compagnies/<int:id_compagnie>/vols")
@ns.response(404, 'Vol not found')
class CompagnieVolsCollection(Resource):
    """Ressource pour récupérer les vols d'une compagnie spécifique."""
    @ns.marshal_list_with(vol_model)
    def get(self,id_compagnie):
        """Récupère les vols d'une compagnie par son ID."""
        vols = get_vols_by_compagnie(id_compagnie)
        if vols is None:
            abort(404,"Vol not found")
        return vols

@ns.route("/aeroports")
class AeroportCollection(Resource):
    """Ressource pour récupérer la liste des aéroports ou en créer un nouveau."""
    @ns.marshal_list_with(aeroport_model)
    def get(self):
        """Récupère la liste des aéroports, avec possibilité de filtrer par nom."""
        nom_aeroport = request.args.get('nom_aeroport')
        if nom_aeroport:
            return Aeroport.query.filter(Aeroport.nom_aeroport.ilike(f"%{nom_aeroport}%")).all()
        return get_all_aeroports()
    
    @ns.expect(aeroport_input_model)
    def post(self):
        """Crée un nouvel aéroport."""
        create_aeroport(nom_aeroport=ns.payload["nom_aeroport"], ville=ns.payload["ville"], pays=ns.payload["pays"])
        return {}, 201

@ns.route("/aeroports/<int:id_aeroport>")
@ns.response(404, 'Aeroport not found')
class AeroportItem(Resource):
    """Ressource pour récupérer, modifier ou supprimer un aéroport spécifique."""
    @ns.marshal_with(aeroport_model)
    def get(self,id_aeroport):
        """Récupère un aéroport par son ID."""
        aeroport = get_aeroport(id_aeroport)
        if aeroport is None:
            abort(404,"Aeroport not found")
        return aeroport       

    @ns.expect(aeroport_input_model)
    @ns.marshal_with(aeroport_model)
    def put(self,id_aeroport):
        """Modifie un aéroport existant."""
        aeroport = modify_aeroport(id_aeroport,ns.payload["nom_aeroport"], ns.payload["ville"], ns.payload["pays"])
        if aeroport is None:
            abort(404,"Aeroport not found")
        return aeroport, 200 
    
    def delete(self,id_aeroport):
        """Supprime un aéroport par son ID."""
        delete_aeroport(id_aeroport)
        return {}, 204

@ns.route("/aeroports/<int:id_aeroport>/terminaux")
@ns.response(404, 'Terminal not found')
class AeroportTerminalsCollection(Resource):
    """Ressource pour récupérer les terminaux d'un aéroport spécifique."""
    @ns.marshal_list_with(terminal_model)
    def get(self,id_aeroport):
        """Récupère les terminaux d'un aéroport par son ID."""
        terminaux = get_terminaux_by_aeroport(id_aeroport)
        if terminaux is None:
            abort(404,"Terminal not found")
        return terminaux

@ns.route("/localisations")
class LocaliserCollection(Resource):
    """Ressource pour récupérer la liste des localisations ou en créer une nouvelle. Une localisation
    représente le fait qu'une compagnie opère à un aéroport donné."""
    @ns.marshal_list_with(localiser_model)
    def get(self):
        """Récupère la liste des localisations."""
        return get_all_localiser()
    
    @ns.expect(localiser_input_model)
    def post(self):
        """Crée une nouvelle localisation."""
        create_localiser(id_aeroport=ns.payload["id_aeroport"], id_compagnie=ns.payload["id_compagnie"])
        return {}, 201

@ns.route("/localisations/<int:id_aeroport>/<int:id_compagnie>")
@ns.response(404, 'Localiser not found')
class LocaliserItem(Resource):
    def delete(self, id_aeroport, id_compagnie):
        delete_localiser(id_aeroport, id_compagnie)
        return {}, 204
    
@ns.route("/terminaux")
class TerminalCollection(Resource):
    """Ressource pour récupérer la liste des terminaux ou en créer un nouveau."""
    @ns.marshal_list_with(terminal_model)
    def get(self):
        """Récupère la liste des terminaux, avec possibilité de filtrer par nom."""
        nom_terminal = request.args.get('nom_terminal')
        if nom_terminal:
            return Terminal.query.filter(Terminal.nom_terminal.ilike(f"%{nom_terminal}%")).all()
        return get_all_terminaux()
    
    @ns.expect(terminal_input_model)
    def post(self):
        """Crée un nouveau terminal."""
        create_terminal(nom_terminal=ns.payload["nom_terminal"], id_aeroport=ns.payload["id_aeroport"])
        return {}, 201
    
@ns.route("/terminaux/<int:id_terminal>")
@ns.response(404, 'Terminal not found')
class TerminalItem(Resource):
    """Ressource pour récupérer, modifier ou supprimer un terminal spécifique."""
    @ns.marshal_with(terminal_model)
    def get(self,id_terminal):
        """Récupère un terminal par son ID."""
        terminal = get_terminal(id_terminal)
        if terminal is None:
            abort(404,"Terminal not found")
        return terminal  

    @ns.expect(terminal_input_model)
    @ns.marshal_with(terminal_model)
    def put(self,id_terminal):
        """Modifie un terminal existant."""
        terminal = modify_terminal(id_terminal,ns.payload["nom_terminal"], ns.payload["id_aeroport"])
        if terminal is None:
            abort(404,"Terminal not found")
        return terminal, 200 

    def delete(self,id_terminal):
        """Supprime un terminal par son ID."""
        delete_terminal(id_terminal)
        return {}, 204 

@ns.route("/vols")
class VolCollection(Resource):
    """Ressource pour récupérer la liste des vols ou en créer un nouveau."""
    @ns.marshal_list_with(vol_model)
    def get(self):
        """Récupère la liste des vols, avec possibilité de filtrer par nom."""
        nom_vol = request.args.get('nom_vol')
        if nom_vol:
            return Vol.query.filter(Vol.nom_vol.ilike(f"%{nom_vol}%")).all()
        return get_all_vols()
    
    @ns.expect(vol_input_model)
    def post(self):
        """Crée un nouveau vol."""
        create_vol(nom_vol=ns.payload["nom_vol"], id_compagnie=ns.payload["id_compagnie"], id_terminal_depart=ns.payload["id_terminal_depart"], id_terminal_arrivee=ns.payload["id_terminal_arrivee"], date_heure_depart=ns.payload["date_heure_depart"], date_heure_arrivee=ns.payload["date_heure_arrivee"])
        return {}, 201

@ns.route("/vols/<int:id_vol>")
@ns.response(404, 'Vol not found')
class VolItem(Resource):
    """Ressource pour récupérer, modifier ou supprimer un vol spécifique."""
    @ns.marshal_with(vol_model)
    def get(self,id_vol):
        """Récupère un vol par son ID."""
        vol = get_vol(id_vol)
        if vol is None:
            abort(404,"Vol not found")
        return vol   
    
    @ns.expect(vol_input_model)
    @ns.marshal_with(vol_model)
    def put(self,id_vol):
        """Modifie un vol existant."""  
        vol = modify_vol(id_vol,ns.payload["nom_vol"], ns.payload["id_compagnie"], ns.payload["id_terminal_depart"], ns.payload["id_terminal_arrivee"], ns.payload["date_heure_depart"], ns.payload["date_heure_arrivee"])
        if vol is None:
            abort(404,"Vol not found")
        return vol, 200  
    
    def delete(self,id_vol):
        """Supprime un vol par son ID."""
        delete_vol(id_vol)
        return {}, 204