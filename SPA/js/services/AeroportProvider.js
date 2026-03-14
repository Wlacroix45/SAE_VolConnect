import { AEROPORT } from "../config.js";

export default class AeroportProvider{
    static fetchAeroports = async (nb=10, page_ac=1, nomAeroport="") =>{
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

            if (nomAeroport && nomAeroport.trim() !== "") {
                params.set("nom_aeroport", nomAeroport.trim());
            }

            const response = await fetch(`${AEROPORT}?${params.toString()}`);
            const json = await response.json();
            return json;
        }catch(err){
            console.log('Error getting documents.', err);
            return [];
        }
    }

    static getAeroport = async (id) =>{
        const options = {
            method : "GET",
            headers : {
                'Content-Type': 'application/json',
            }
        };

        try{
            const response = await fetch(`${AEROPORT}/${id}`);
            const json = await response.json();
            return json;
        }catch(err){
            console.log('Error getting documents.', err);
        }
    }
}