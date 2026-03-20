import VolProvider from "../../services/VolProvider.js"
import Utils  from "../../services/Utils.js";   

export default class VolShow{
    async render(){
        let url = Utils.parseRequestURL();
        console.log("URL ", url);
        let vol = await VolProvider.getVol(url.id);
        console.log("Le vol choisi ", vol);
        return `
            <div class="card border-info mb-3" style="max-width: 18rem; align-items: center;">
                <div class="card-header"> Id : ${vol.id_vol}</div>
                <div class="card-body text-info">
                    <h5 class="card-title">${vol.nom_vol}</h5>
                </div>
            </div>
        `;
    }
}
