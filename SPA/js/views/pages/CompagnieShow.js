import CompagnieProvider from "../../services/CompagnieProvider.js"
import AeroportProvider from "../../services/AeroportProvider.js";
import LocaliserProvider from "../../services/LocaliserProvider.js";
import Utils  from "../../services/Utils.js";   

export default class CompagnieShow{
    getSelectedAeroportIds() {
        return Array.from(document.querySelectorAll('input[name="aeroports-localiser"]:checked'))
            .map((el) => Number(el.value));
    }

    async handleUpdateCompagnie(event) {
        event.preventDefault();
        const url = Utils.parseRequestURL();
        const id = url.id;
        const nom_comp = document.getElementById('inputNameCompagnie')?.value?.trim() ?? "";
        if (!id || !nom_comp) return;

        
        await CompagnieProvider.updateCompagnie(id, nom_comp);

        
        const selectedAeroportIds = new Set(this.getSelectedAeroportIds());
        const localisations = await LocaliserProvider.fetchLocalisations();
        const existingAeroportIds = new Set(
            (Array.isArray(localisations) ? localisations : [])
                .filter((l) => Number(l.id_compagnie) === Number(id))
                .map((l) => Number(l.id_aeroport))
        );

        const toAdd = Array.from(selectedAeroportIds).filter((aId) => !existingAeroportIds.has(aId));
        const toRemove = Array.from(existingAeroportIds).filter((aId) => !selectedAeroportIds.has(aId));

        await Promise.all(toAdd.map((aId) => LocaliserProvider.addLocalisation(aId, id)));
        await Promise.all(toRemove.map((aId) => LocaliserProvider.deleteLocalisation(aId, id)));

        const content = document.querySelector('#main');
        if (content) content.innerHTML = await this.render();
    }

    async handleDeleteCompagnie(event) {
        event.preventDefault();
        const url = Utils.parseRequestURL();
        const id = url.id;
        if (!id) return;
        const ok = confirm("Supprimer cette compagnie ?");
        if (!ok) return;
        await CompagnieProvider.deleteCompagnie(id);
        location.hash = "#/compagnies";
    }

    async render(){
        let url = Utils.parseRequestURL();
        console.log("URL ", url);
        let compagnie = await CompagnieProvider.getCompagnie(url.id);
        console.log("La compagnie choisie ", compagnie);

        const rawAeroports = await AeroportProvider.fetchAeroports(1000, 1, "");
        const aeroportsForSelect = Array.isArray(rawAeroports)
            ? rawAeroports
            : (Array.isArray(rawAeroports.items) ? rawAeroports.items : []);

        const localisations = await LocaliserProvider.fetchLocalisations();
        const aeroportIdsChecked = new Set(
            (Array.isArray(localisations) ? localisations : [])
                .filter((l) => Number(l.id_compagnie) === Number(compagnie.id_compagnie))
                .map((l) => Number(l.id_aeroport))
        );

        return `
            <div class="card border-info mb-3" style="max-width: 18rem; align-items: center;">
                <div class="card-header"> Id : ${compagnie.id_compagnie}</div>
                <div class="card-body text-info">
                    <h5 class="card-title">${compagnie.nom_comp}</h5>
                </div>
            </div>

            <a class="btn btn-outline-secondary mb-3" href="#/compagnies">Retour à la liste</a>

            <form onsubmit="window.currentArticlePage.handleUpdateCompagnie(event)">
                <div class="mb-3">
                    <label for="inputNameCompagnie" class="form-label">Nom de la compagnie</label>
                    <input type="text" class="form-control" id="inputNameCompagnie" value="${compagnie.nom_comp ?? ""}">
                </div>

                <div class="mb-3">
                    <div class="form-label">Aéroports localisés</div>
                    <div class="list-group">
                        ${aeroportsForSelect.map((a) => {
                            const checked = aeroportIdsChecked.has(Number(a.id_aeroport)) ? "checked" : "";
                            return `
                                <label class="list-group-item">
                                    <input class="form-check-input me-1" type="checkbox" name="aeroports-localiser" value="${a.id_aeroport}" ${checked}>
                                    ${a.nom_aeroport}
                                </label>
                            `;
                        }).join("\n")}
                    </div>
                </div>

                <button type="submit" class="btn btn-primary">Enregistrer</button>
                <button type="button" class="btn btn-danger" onclick="window.currentArticlePage.handleDeleteCompagnie(event)">Supprimer</button>
            </form>
        `;
    }
}
