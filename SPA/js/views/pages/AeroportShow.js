import AeroportProvider from "../../services/AeroportProvider.js"
import Utils  from "../../services/Utils.js";   

export default class AeroportShow{
    async render(){
        let url = Utils.parseRequestURL();
        let aeroport = await AeroportProvider.getAeroport(url.id);
        console.log("L'aeroport choisi ", aeroport);
        return `
            <div class="card border-info mb-3" style="max-width: 18rem; align-items: center;">
                <div class="card-header"> Id : ${aeroport.id}</div>
                <div class="card-body text-info">
                    <h5 class="card-title">${aeroport.nom_aeroport}</h5>
                </div>
            </div>
        `;
    }
}
