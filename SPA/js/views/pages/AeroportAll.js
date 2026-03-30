import AeroportProvider from "../../services/AeroportProvider.js";

export default class AeroportAll {
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
        const nomRentre = document.querySelector('#aeroport-search-input');
        this.nomCherche = nomRentre ? nomRentre.value.trim() : "";
        await this.setPage(1);
    }

    async handleAddAeroport(event) {
        event.preventDefault();
        const name = document.getElementById('inputNameAeroport').value.trim();
        const ville = document.getElementById('inputVilleAeroport').value.trim();
        const pays = document.getElementById('inputPaysAeroport').value.trim();
        await AeroportProvider.addAeroport(name, ville, pays);
        await this.setPage(1);
    }





    async render() {
        const rawAeroports = await AeroportProvider.fetchAeroports(this.items_per_page, 1, this.nomCherche);
        const allAeroports = Array.isArray(rawAeroports)
            ? rawAeroports
            : (Array.isArray(rawAeroports.items) ? rawAeroports.items : []);
        this.total_pages = Math.max(1, Math.ceil(allAeroports.length / this.items_per_page));
        this.page_ac = Math.min(Math.max(1, this.page_ac), this.total_pages);
        const start = (this.page_ac - 1) * this.items_per_page;
        const aeroports = allAeroports.slice(start, start + this.items_per_page);
        let view = `
            <h2 style="text-align: center;">Tous les aeroports</h2>
            <form class="d-flex" role="search" onsubmit="window.currentArticlePage.submitFilter(event)">
                <input
                    id="aeroport-search-input"
                    class="form-control me-2"
                    type="search"
                    placeholder="Chercher par nom"
                    aria-label="Search"
                    value="${this.nomCherche}"
                />
                <button class="btn btn-outline-success" type="submit">Filtrer</button>
            </form>

            <ul class="list-group">
                ${aeroports.map((aeroport) => `
                    <li class="list-group-item">
                        <a class="list-group-item list-group-item-action" href="#/aeroports/${aeroport.id_aeroport}">
                            ${aeroport.nom_aeroport}
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
                    <label for="inputNameAeroport" class="form-label">Nom de l'aéroport</label>
                    <input type="text" class="form-control" id="inputNameAeroport">
                </div>
                <div class="mb-3">
                    <label for="inputVilleAeroport" class="form-label">Ville de l'aéroport</label>
                    <input type="text" class="form-control" id="inputVilleAeroport">
                </div>
                 <div class="mb-3">
                    <label for="inputPaysAeroport" class="form-label">Pays de l'aéroport</label>
                    <input type="text" class="form-control" id="inputPaysAeroport">
                </div>
                <input type="button" onclick="event.preventDefault(); window.currentArticlePage.handleAddAeroport(event)" class="btn btn-primary" value="Ajouter">
            </form>
        `;

        return view;
    }
}

