import { TERMINAL } from "../config.js";

export default class TerminalProvider{
    static fetchTerminaux = async (nb=10, page_ac=1, nom_terminal="") =>{
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
            if (nom_terminal && nom_terminal.trim() !== "") {
                params.set("nom_terminal", nom_terminal.trim());
            }
                               
            const response = await fetch(`${TERMINAL}?${params.toString()}`);
            const json = await response.json();
            return json;
        }catch(err){
            console.log('Error getting documents.', err);
            return [];
        }
    }

    static getTerminal = async (id) =>{
        const options = {
            method : "GET",
            headers : {
                'Content-Type': 'application/json',
            }
        };

        try{
            const response = await fetch(`${TERMINAL}/${id}`);
            const json = await response.json();
            return json;
        }catch(err){
            console.log('Error getting documents.', err);
        }
    }

    static addTerminal = async (nom_terminal, id_aeroport) => {
        const options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ nom_terminal, id_aeroport: Number(id_aeroport) }),
        };

        try {
            const response = await fetch(`${TERMINAL}`, options);
            const json = await response.json();
            return json;
        } catch (err) {
            console.log('Error creating document', err);
        }
    }

    static updateTerminal = async (id, nom_terminal, id_aeroport) => {
        const options = {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ nom_terminal, id_aeroport: Number(id_aeroport) }),
        };

        try {
            const response = await fetch(`${TERMINAL}/${id}`, options);
            const json = await response.json();
            return json;
        } catch (err) {
            console.log('Error updating document', err);
        }
    }

    static deleteTerminal = async (id) => {
        const options = {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
            },
        };

        try {
            const response = await fetch(`${TERMINAL}/${id}`, options);
            return response.ok;
        } catch (err) {
            console.log('Error deleting document', err);
            return false;
        }
    }
}