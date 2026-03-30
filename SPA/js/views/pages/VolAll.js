import VolProvider from "../../services/VolProvider.js";
import CompagnieProvider from "../../services/CompagnieProvider.js";
import TerminalProvider from "../../services/TerminalProvider.js";

export default class VolAll{
    constructor() {
        this.page_ac = 1;
        this.items_per_page = 10;
        this.total_pages = null;
        this.nomCherche = "";
    }

    async setPage(newPage) {
        const maxPage = this.total_pages || 1;
        this.page_ac = Math.min(Math.max(1, newPage), maxPage);

        const content = document.querySelector("#main");
        content.innerHTML = await this.render();
    }

    async submitFilter(event) {
        event.preventDefault();
        const nomRentre = document.querySelector('#vol-search-input');
        this.nomCherche = nomRentre ? nomRentre.value.trim() : "";
        await this.setPage(1);
    }

    async handleAddVol(event) {
        event.preventDefault();
        const nom_vol = document.getElementById('inputNameVol')?.value?.trim() ?? "";
        const id_compagnie = document.getElementById('selectCompagnieVol')?.value;
        const id_terminal_depart = document.getElementById('selectTerminalDepartVol')?.value;
        const id_terminal_arrivee = document.getElementById('selectTerminalArriveeVol')?.value;
        const date_heure_depart = document.getElementById('inputDateDepartVol')?.value;
        const date_heure_arrivee = document.getElementById('inputDateArriveeVol')?.value;

        if (!nom_vol || !id_compagnie || !id_terminal_depart || !id_terminal_arrivee || !date_heure_depart || !date_heure_arrivee) {
            return;
        }

        await VolProvider.addVol(
            nom_vol,
            Number(id_compagnie),
            Number(id_terminal_depart),
            Number(id_terminal_arrivee),
            date_heure_depart,
            date_heure_arrivee,
        );
        await this.setPage(1);
    }

    async render() {
        const rawVols = await VolProvider.fetchVols(this.items_per_page, 1, this.nomCherche);
        const allVols = Array.isArray(rawVols)
            ? rawVols
            : (Array.isArray(rawVols.items) ? rawVols.items : []);
        this.total_pages = Math.max(1, Math.ceil(allVols.length / this.items_per_page));
        this.page_ac = Math.min(Math.max(1, this.page_ac), this.total_pages);
        const start = (this.page_ac - 1) * this.items_per_page;
        const vols = allVols.slice(start, start + this.items_per_page);

        const rawCompagnies = await CompagnieProvider.fetchCompagnies(1000, 1, "");
        const compagniesForSelect = Array.isArray(rawCompagnies)
            ? rawCompagnies
            : (Array.isArray(rawCompagnies.items) ? rawCompagnies.items : []);

        const rawTerminaux = await TerminalProvider.fetchTerminaux(2000, 1, "");
        const terminauxForSelect = Array.isArray(rawTerminaux)
            ? rawTerminaux
            : (Array.isArray(rawTerminaux.items) ? rawTerminaux.items : []);

        let view = `
            <h2 style="text-align: center;">Tous les vols</h2>
            <form class="d-flex" role="search" onsubmit="window.currentArticlePage.submitFilter(event)">
                <input
                    id="vol-search-input"
                    class="form-control me-2"
                    type="search"
                    placeholder="Chercher par nom"
                    aria-label="Search"
                    value="${this.nomCherche}"
                />
                <button class="btn btn-outline-success" type="submit">Filtrer</button>
            </form>

            <ul class="list-group">
                ${vols.map((vol) => `
                    <li class="list-group-item">
                        <a class="list-group-item list-group-item-action" href="#/vols/${vol.id_vol}">
                            ${vol.nom_vol}
                        </a>
                    </li>
                `).join("\n")}
            </ul>

            <nav aria-label="Page navigation exemple">
                <ul class="pagination">
                    <li class="page-item ${this.page_ac === 1 ? "disabled" : ""}">
                        <a class="page-link" href="#" onclick="event.preventDefault(); window.currentArticlePage.setPage(${this.page_ac - 1})" aria-label="Previous">
                            <span aria-hidden="true">&laquo;</span>
                        </a>
                    </li>

                    ${Array.from({ length: this.total_pages }, (_, i) => i + 1)
                        .map((page) => `
                            <li class="page-item ${this.page_ac === page ? "active" : ""}">
                                <a class="page-link" href="#" onclick="event.preventDefault(); window.currentArticlePage.setPage(${page})">${page}</a>
                            </li>
                        `)
                        .join("\n")}

                    <li class="page-item ${this.page_ac === this.total_pages ? "disabled" : ""}">
                        <a class="page-link" href="#" onclick="event.preventDefault(); window.currentArticlePage.setPage(${this.page_ac + 1})" aria-label="Next">
                            <span aria-hidden="true">&raquo;</span>
                        </a>
                    </li>
                </ul>
            </nav>

            <form>
                <div class="mb-3">
                    <label for="inputNameVol" class="form-label">Nom du vol</label>
                    <input type="text" class="form-control" id="inputNameVol">
                </div>
                <div class="mb-3">
                    <label for="selectCompagnieVol" class="form-label">Compagnie</label>
                    <select class="form-control" id="selectCompagnieVol">
                        ${compagniesForSelect.map((c) => `
                            <option value="${c.id_compagnie}">${c.nom_comp}</option>
                        `).join("\n")}
                    </select>
                </div>
                <div class="mb-3">
                    <label for="selectTerminalDepartVol" class="form-label">Terminal de départ</label>
                    <select class="form-control" id="selectTerminalDepartVol">
                        ${terminauxForSelect.map((t) => `
                            <option value="${t.id_terminal}">${t.nom_terminal}</option>
                        `).join("\n")}
                    </select>
                </div>
                <div class="mb-3">
                    <label for="selectTerminalArriveeVol" class="form-label">Terminal d'arrivée</label>
                    <select class="form-control" id="selectTerminalArriveeVol">
                        ${terminauxForSelect.map((t) => `
                            <option value="${t.id_terminal}">${t.nom_terminal}</option>
                        `).join("\n")}
                    </select>
                </div>
                <div class="mb-3">
                    <label for="inputDateDepartVol" class="form-label">Date/heure départ</label>
                    <input type="datetime-local" lang="fr-FR" class="form-control" id="inputDateDepartVol" step="60">
                </div>
                <div class="mb-3">
                    <label for="inputDateArriveeVol" class="form-label">Date/heure arrivée</label>
                    <input type="datetime-local" lang="fr-FR" class="form-control" id="inputDateArriveeVol" step="60">
                </div>
                <input type="button" onclick="event.preventDefault(); window.currentArticlePage.handleAddVol(event)" class="btn btn-primary" value="Ajouter">
            </form>
        `;

        return view;
    }
}

