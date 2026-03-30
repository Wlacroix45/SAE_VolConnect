import AeroportProvider from "../../services/AeroportProvider.js"
import CompagnieProvider from "../../services/CompagnieProvider.js";
import LocaliserProvider from "../../services/LocaliserProvider.js";
import Utils  from "../../services/Utils.js";   

export default class AeroportShow{
    async handleUpdateAeroport(event) {
        event.preventDefault();
        const url = Utils.parseRequestURL();
        const id = url.id;
        const nom_aeroport = document.getElementById('inputNameAeroport')?.value?.trim() ?? "";
        const ville = document.getElementById('inputVilleAeroport')?.value?.trim() ?? "";
        const pays = document.getElementById('inputPaysAeroport')?.value?.trim() ?? "";
        if (!id || !nom_aeroport || !ville || !pays) return;
        await AeroportProvider.updateAeroport(id, nom_aeroport, ville, pays);
        const content = document.querySelector('#main');
        if (content) content.innerHTML = await this.render();
    }

    async handleDeleteAeroport(event) {
        event.preventDefault();
        const url = Utils.parseRequestURL();
        const id = url.id;
        if (!id) return;
        const ok = confirm("Supprimer cet aéroport ?");
        if (!ok) return;
        await AeroportProvider.deleteAeroport(id);
        location.hash = "#/aeroports";
    }

    async render(){
        let url = Utils.parseRequestURL();
        console.log("URL ", url);
        let aeroport = await AeroportProvider.getAeroport(url.id);
        console.log("L'aeroport choisi ", aeroport);

        const localisations = await LocaliserProvider.fetchLocalisations();
        const rawCompagnies = await CompagnieProvider.fetchCompagnies(1000, 1, "");
        const compagnies = Array.isArray(rawCompagnies)
            ? rawCompagnies
            : (Array.isArray(rawCompagnies.items) ? rawCompagnies.items : []);

        const compagnieIds = new Set(
            (Array.isArray(localisations) ? localisations : [])
                .filter((l) => Number(l.id_aeroport) === Number(aeroport.id_aeroport))
                .map((l) => Number(l.id_compagnie))
        );
        const compagniesLocalisees = compagnies.filter((c) => compagnieIds.has(Number(c.id_compagnie)));

        return `
            <div class="card border-info mb-3" style="max-width: 18rem; align-items: center;">
                <div class="card-header"> Id : ${aeroport.id_aeroport}</div>
                <div class="card-body text-info">
                    <h5 class="card-title">${aeroport.nom_aeroport}</h5>
                </div>
            </div>

            <h5>Compagnies localisées</h5>
            <ul class="list-group mb-3">
                ${compagniesLocalisees.length === 0 ? `
                    <li class="list-group-item">Aucune compagnie</li>
                ` : compagniesLocalisees.map((c) => `
                    <li class="list-group-item">
                        <a class="list-group-item list-group-item-action" href="#/compagnies/${c.id_compagnie}">${c.nom_comp}</a>
                    </li>
                `).join("\n")}
            </ul>

            <a class="btn btn-outline-secondary mb-3" href="#/aeroports">Retour à la liste</a>

            <form onsubmit="window.currentArticlePage.handleUpdateAeroport(event)">
                <div class="mb-3">
                    <label for="inputNameAeroport" class="form-label">Nom de l'aéroport</label>
                    <input type="text" class="form-control" id="inputNameAeroport" value="${aeroport.nom_aeroport ?? ""}">
                </div>
                <div class="mb-3">
                    <label for="inputVilleAeroport" class="form-label">Ville</label>
                    <input type="text" class="form-control" id="inputVilleAeroport" value="${aeroport.ville ?? ""}">
                </div>
                <div class="mb-3">
                    <label for="inputPaysAeroport" class="form-label">Pays</label>
                    <input type="text" class="form-control" id="inputPaysAeroport" value="${aeroport.pays ?? ""}">
                </div>
                <button type="submit" class="btn btn-primary">Enregistrer</button>
                <button type="button" class="btn btn-danger" onclick="window.currentArticlePage.handleDeleteAeroport(event)">Supprimer</button>
            </form>
        `;
    }
}
