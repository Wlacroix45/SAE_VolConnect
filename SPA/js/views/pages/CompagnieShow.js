import CompagnieProvider from "../../services/CompagnieProvider.js"
import Utils  from "../../services/Utils.js";   

export default class CompagnieShow{
    async render(){
        let url = Utils.parseRequestURL();
        console.log("URL ", url);
        let compagnie = await CompagnieProvider.getCompagnie(url.id);
        console.log("La compagnie choisie ", compagnie);
        return `
            <div class="card border-info mb-3" style="max-width: 18rem; align-items: center;">
                <div class="card-header"> Id : ${compagnie.id_compagnie}</div>
                <div class="card-body text-info">
                    <h5 class="card-title">${compagnie.nom_comp}</h5>
                </div>
            </div>
        `;
    }
}
