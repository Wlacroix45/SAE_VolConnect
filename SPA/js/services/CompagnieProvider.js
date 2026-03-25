import { COMPAGNIE } from "../config.js";

export default class CompagnieProvider{
    static fetchCompagnies = async (nb=10, page_ac=1, nom_compagnie="") =>{
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
            
            if (nom_compagnie && nom_compagnie.trim() !== "") {
                params.set("nom_comp", nom_compagnie.trim());
            }
            
            const response = await fetch(`${COMPAGNIE}?${params.toString()}`);
            const json = await response.json();
            return json;
        }catch(err){
            console.log('Error getting documents.', err);
            return [];
        }
    }

    static getCompagnie = async (id) =>{
        const options = {
            method : "GET",
            headers : {
                'Content-Type': 'application/json',
            }
        };

        try{
            const response = await fetch(`${COMPAGNIE}/${id}`);
            const json = await response.json();
            return json;
        }catch(err){
            console.log('Error getting documents.', err);
        }
    }

            static addCompagnie=async(nom_comp) =>{
            const options= {
            method : 'POST',
            headers :{
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({nom_comp})
            };
            try{
                const response= await fetch(`${COMPAGNIE}`, options);
                const json= await response.json();
                return json;
            }catch(err){
                console.log('Error getting document',err)
            }
        }
}