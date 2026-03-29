import VolProvider from "../../services/VolProvider.js"
import CompagnieProvider from "../../services/CompagnieProvider.js";
import TerminalProvider from "../../services/TerminalProvider.js";
import Utils  from "../../services/Utils.js";   

export default class VolShow{
    toDatetimeLocalValue(isoString) {
        if (!isoString || typeof isoString !== "string") return "";
        return isoString.slice(0, 16);
    }

    async handleUpdateVol(event) {
        event.preventDefault();
        const url = Utils.parseRequestURL();
        const id = url.id;
        const nom_vol = document.getElementById('inputNameVol')?.value?.trim() ?? "";
        const id_compagnie = document.getElementById('selectCompagnieVol')?.value;
        const id_terminal_depart = document.getElementById('selectTerminalDepartVol')?.value;
        const id_terminal_arrivee = document.getElementById('selectTerminalArriveeVol')?.value;
        const date_heure_depart = document.getElementById('inputDateDepartVol')?.value;
        const date_heure_arrivee = document.getElementById('inputDateArriveeVol')?.value;
        if (!id || !nom_vol || !id_compagnie || !id_terminal_depart || !id_terminal_arrivee || !date_heure_depart || !date_heure_arrivee) return;

        await VolProvider.updateVol(
            id,
            nom_vol,
            Number(id_compagnie),
            Number(id_terminal_depart),
            Number(id_terminal_arrivee),
            date_heure_depart,
            date_heure_arrivee,
        );
        const content = document.querySelector('#main');
        if (content) content.innerHTML = await this.render();
    }

    async handleDeleteVol(event) {
        event.preventDefault();
        const url = Utils.parseRequestURL();
        const id = url.id;
        if (!id) return;
        const ok = confirm("Supprimer ce vol ?");
        if (!ok) return;
        await VolProvider.deleteVol(id);
        location.hash = "#/vols";
    }

    async render(){
        let url = Utils.parseRequestURL();
        console.log("URL ", url);
        let vol = await VolProvider.getVol(url.id);
        console.log("Le vol choisi ", vol);

        const rawCompagnies = await CompagnieProvider.fetchCompagnies(1000, 1, "");
        const compagniesForSelect = Array.isArray(rawCompagnies)
            ? rawCompagnies
            : (Array.isArray(rawCompagnies.items) ? rawCompagnies.items : []);

        const rawTerminaux = await TerminalProvider.fetchTerminaux(2000, 1, "");
        const terminauxForSelect = Array.isArray(rawTerminaux)
            ? rawTerminaux
            : (Array.isArray(rawTerminaux.items) ? rawTerminaux.items : []);

        return `
            <div class="card border-info mb-3" style="max-width: 18rem; align-items: center;">
                <div class="card-header"> Id : ${vol.id_vol}</div>
                <div class="card-body text-info">
                    <h5 class="card-title">${vol.nom_vol}</h5>
                </div>
            </div>

            <a class="btn btn-outline-secondary mb-3" href="#/vols">Retour à la liste</a>

            <form onsubmit="window.currentArticlePage.handleUpdateVol(event)">
                <div class="mb-3">
                    <label for="inputNameVol" class="form-label">Nom du vol</label>
                    <input type="text" class="form-control" id="inputNameVol" value="${vol.nom_vol ?? ""}">
                </div>
                <div class="mb-3">
                    <label for="selectCompagnieVol" class="form-label">Compagnie</label>
                    <select class="form-control" id="selectCompagnieVol">
                        ${compagniesForSelect.map((c) => `
                            <option value="${c.id_compagnie}" ${Number(c.id_compagnie) === Number(vol.id_compagnie) ? "selected" : ""}>
                                ${c.nom_comp}
                            </option>
                        `).join("\n")}
                    </select>
                </div>
                <div class="mb-3">
                    <label for="selectTerminalDepartVol" class="form-label">Terminal de départ</label>
                    <select class="form-control" id="selectTerminalDepartVol">
                        ${terminauxForSelect.map((t) => `
                            <option value="${t.id_terminal}" ${Number(t.id_terminal) === Number(vol.id_terminal_depart) ? "selected" : ""}>
                                ${t.nom_terminal}
                            </option>
                        `).join("\n")}
                    </select>
                </div>
                <div class="mb-3">
                    <label for="selectTerminalArriveeVol" class="form-label">Terminal d'arrivée</label>
                    <select class="form-control" id="selectTerminalArriveeVol">
                        ${terminauxForSelect.map((t) => `
                            <option value="${t.id_terminal}" ${Number(t.id_terminal) === Number(vol.id_terminal_arrivee) ? "selected" : ""}>
                                ${t.nom_terminal}
                            </option>
                        `).join("\n")}
                    </select>
                </div>
                <div class="mb-3">
                    <label for="inputDateDepartVol" class="form-label">Date/heure départ (24h)</label>
                    <input type="datetime-local" lang="fr-FR" class="form-control" id="inputDateDepartVol" step="60" value="${this.toDatetimeLocalValue(vol.date_heure_depart)}">
                </div>
                <div class="mb-3">
                    <label for="inputDateArriveeVol" class="form-label">Date/heure arrivée (24h)</label>
                    <input type="datetime-local" lang="fr-FR" class="form-control" id="inputDateArriveeVol" step="60" value="${this.toDatetimeLocalValue(vol.date_heure_arrivee)}">
                </div>
                <button type="submit" class="btn btn-primary">Enregistrer</button>
                <button type="button" class="btn btn-danger" onclick="window.currentArticlePage.handleDeleteVol(event)">Supprimer</button>
            </form>
        `;
    }
}
