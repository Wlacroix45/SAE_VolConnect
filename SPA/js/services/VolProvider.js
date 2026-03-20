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
}