import { AEROPORT } from "../config.js";

export default class AeroportProvider{
    static fetchAeroports = async (nb=10, page_ac=1, nom_aeroport="") =>{
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

            if (nom_aeroport && nom_aeroport.trim() !== "") {
                params.set("nom_aeroport", nom_aeroport.trim());
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

        static addAeroport=async(nom_aeroport, ville, pays) =>{
        const options= {
        method : 'POST',
        headers :{
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({nom_aeroport, ville, pays})
        };
        try{
            const response= await fetch(`${AEROPORT}`, options);
            const json= await response.json();
            return json;
        }catch(err){
            console.log('Error getting document',err)
        }
    }


}