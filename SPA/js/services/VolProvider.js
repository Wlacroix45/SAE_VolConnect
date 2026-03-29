import { VOL } from "../config.js";

export default class VolProvider{
    static fetchVols = async (nb=10, page_ac=1, nom_vol="") =>{
        const options = {
            method : "GET",
            headers : {
                'Content-Type': 'application/json',
            }
        };

        try{
            const params = new URLSearchParams({
                _page: page_ac,
                _per_page: nb
            });            
            if (nom_vol && nom_vol.trim() !== "") {
                params.set("nom_vol", nom_vol.trim());
            }
                   
            const response = await fetch(`${VOL}?${params.toString()}`);
            const json = await response.json();
            return json;
        }catch(err){
            console.log('Error getting documents.', err);
            return [];
        }
    }

    static getVol = async (id) =>{
        const options = {
            method : "GET",
            headers : {
                'Content-Type': 'application/json',
            }
        };

        try{
            const response = await fetch(`${VOL}/${id}`);
            const json = await response.json();
            return json;
        }catch(err){
            console.log('Error getting documents.', err);
        }
    }

    static addVol = async (nom_vol, id_compagnie, id_terminal_depart, id_terminal_arrivee, date_heure_depart, date_heure_arrivee) => {
        const options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                nom_vol,
                id_compagnie: Number(id_compagnie),
                id_terminal_depart: Number(id_terminal_depart),
                id_terminal_arrivee: Number(id_terminal_arrivee),
                date_heure_depart,
                date_heure_arrivee,
            })
        };

        try {
            const response = await fetch(`${VOL}`, options);
            const json = await response.json();
            return json;
        } catch (err) {
            console.log('Error creating document', err);
        }
    }

    static updateVol = async (id, nom_vol, id_compagnie, id_terminal_depart, id_terminal_arrivee, date_heure_depart, date_heure_arrivee) => {
        const options = {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                nom_vol,
                id_compagnie: Number(id_compagnie),
                id_terminal_depart: Number(id_terminal_depart),
                id_terminal_arrivee: Number(id_terminal_arrivee),
                date_heure_depart,
                date_heure_arrivee,
            })
        };

        try {
            const response = await fetch(`${VOL}/${id}`, options);
            const json = await response.json();
            return json;
        } catch (err) {
            console.log('Error updating document', err);
        }
    }

    static deleteVol = async (id) => {
        const options = {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
            },
        };

        try {
            const response = await fetch(`${VOL}/${id}`, options);
            return response.ok;
        } catch (err) {
            console.log('Error deleting document', err);
            return false;
        }
    }
}