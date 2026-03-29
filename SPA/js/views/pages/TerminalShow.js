import TerminalProvider from "../../services/TerminalProvider.js"
import AeroportProvider from "../../services/AeroportProvider.js";
import Utils  from "../../services/Utils.js";   

export default class TerminalShow{
    async handleUpdateTerminal(event) {
        event.preventDefault();
        const url = Utils.parseRequestURL();
        const id = url.id;
        const nom_terminal = document.getElementById('inputNameTerminal')?.value?.trim() ?? "";
        const id_aeroport = document.getElementById('selectAeroportTerminal')?.value;
        if (!id || !nom_terminal || !id_aeroport) return;
        await TerminalProvider.updateTerminal(id, nom_terminal, Number(id_aeroport));
        const content = document.querySelector('#main');
        if (content) content.innerHTML = await this.render();
    }

    async handleDeleteTerminal(event) {
        event.preventDefault();
        const url = Utils.parseRequestURL();
        const id = url.id;
        if (!id) return;
        const ok = confirm("Supprimer ce terminal ?");
        if (!ok) return;
        await TerminalProvider.deleteTerminal(id);
        location.hash = "#/terminaux";
    }

    async render(){
        let url = Utils.parseRequestURL();
        console.log("URL ", url);
        let terminal = await TerminalProvider.getTerminal(url.id);
        console.log("Le terminal choisi ", terminal);

        const rawAeroports = await AeroportProvider.fetchAeroports(1000, 1, "");
        const aeroportsForSelect = Array.isArray(rawAeroports)
            ? rawAeroports
            : (Array.isArray(rawAeroports.items) ? rawAeroports.items : []);

        return `
            <div class="card border-info mb-3" style="max-width: 18rem; align-items: center;">
                <div class="card-header"> Id : ${terminal.id_terminal}</div>
                <div class="card-body text-info">
                    <h5 class="card-title">${terminal.nom_terminal}</h5>
                </div>
            </div>

            <a class="btn btn-outline-secondary mb-3" href="#/terminaux">Retour à la liste</a>

            <form onsubmit="window.currentArticlePage.handleUpdateTerminal(event)">
                <div class="mb-3">
                    <label for="inputNameTerminal" class="form-label">Nom du terminal</label>
                    <input type="text" class="form-control" id="inputNameTerminal" value="${terminal.nom_terminal ?? ""}">
                </div>
                <div class="mb-3">
                    <label for="selectAeroportTerminal" class="form-label">Aéroport</label>
                    <select class="form-control" id="selectAeroportTerminal">
                        ${aeroportsForSelect.map((a) => `
                            <option value="${a.id_aeroport}" ${Number(a.id_aeroport) === Number(terminal.id_aeroport) ? "selected" : ""}>
                                ${a.nom_aeroport}
                            </option>
                        `).join("\n")}
                    </select>
                </div>
                <button type="submit" class="btn btn-primary">Enregistrer</button>
                <button type="button" class="btn btn-danger" onclick="window.currentArticlePage.handleDeleteTerminal(event)">Supprimer</button>
            </form>
        `;
    }
}
