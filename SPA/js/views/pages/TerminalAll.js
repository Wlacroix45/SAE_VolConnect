import TerminalProvider from "../../services/TerminalProvider.js";
import AeroportProvider from "../../services/AeroportProvider.js";

export default class TerminalAll{
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
        const nomRentre = document.querySelector('#terminal-search-input');
        this.nomCherche = nomRentre ? nomRentre.value.trim() : "";
        await this.setPage(1);
    }

    async handleAddTerminal(event) {
        event.preventDefault();
        const nom_terminal = document.getElementById('inputNameTerminal')?.value?.trim() ?? "";
        const id_aeroport = document.getElementById('selectAeroportTerminal')?.value;
        if (!nom_terminal || !id_aeroport) return;
        await TerminalProvider.addTerminal(nom_terminal, Number(id_aeroport));
        await this.setPage(1);
    }

    async render() {
        const rawTerminaux = await TerminalProvider.fetchTerminaux(this.items_per_page, 1, this.nomCherche);
        const allTerminaux = Array.isArray(rawTerminaux)
            ? rawTerminaux
            : (Array.isArray(rawTerminaux.items) ? rawTerminaux.items : []);
        this.total_pages = Math.max(1, Math.ceil(allTerminaux.length / this.items_per_page));
        this.page_ac = Math.min(Math.max(1, this.page_ac), this.total_pages);
        const start = (this.page_ac - 1) * this.items_per_page;
        const terminaux = allTerminaux.slice(start, start + this.items_per_page);
        const aeroportCache = new Map();

        const rawAeroports = await AeroportProvider.fetchAeroports(1000, 1, "");
        const aeroportsForSelect = Array.isArray(rawAeroports)
            ? rawAeroports
            : (Array.isArray(rawAeroports.items) ? rawAeroports.items : []);

        let view = `
            <h2 style="text-align: center;">Tous les terminaux</h2>
            <form class="d-flex" role="search" onsubmit="window.currentArticlePage.submitFilter(event)">
                <input
                    id="terminal-search-input"
                    class="form-control me-2"
                    type="search"
                    placeholder="Chercher par nom"
                    aria-label="Search"
                    value="${this.nomCherche}"
                />
                <button class="btn btn-outline-success" type="submit">Filtrer</button>
            </form>

            <ul class="list-group">
                ${(
                    await Promise.all(
                        terminaux.map(async (terminal) => {
                            let aeroport = aeroportCache.get(terminal.id_aeroport);
                            if (!aeroport) {
                                aeroport = await AeroportProvider.getAeroport(terminal.id_aeroport);
                                aeroportCache.set(terminal.id_aeroport, aeroport);
                            }

                            return `
                                <li class="list-group-item">
                                    <a class="list-group-item list-group-item-action" href="#/terminaux/${terminal.id_terminal}">
                                        ${terminal.nom_terminal} ${aeroport?.nom_aeroport ?? "Aeroport inconnu"}
                                    </a>
                                </li>
                            `;
                        })
                    )
                ).join("\n")}
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
                    <label for="inputNameTerminal" class="form-label">Nom du terminal</label>
                    <input type="text" class="form-control" id="inputNameTerminal">
                </div>
                <div class="mb-3">
                    <label for="selectAeroportTerminal" class="form-label">Aéroport</label>
                    <select class="form-control" id="selectAeroportTerminal">
                        ${aeroportsForSelect.map((a) => `
                            <option value="${a.id_aeroport}">${a.nom_aeroport}</option>
                        `).join("\n")}
                    </select>
                </div>
                <input type="button" onclick="event.preventDefault(); window.currentArticlePage.handleAddTerminal(event)" class="btn btn-primary" value="Ajouter">
            </form>
        `;

        return view;
    }
}

