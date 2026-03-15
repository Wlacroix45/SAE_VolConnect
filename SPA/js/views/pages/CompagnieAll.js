import CompagnieProvider from "../../services/CompagnieProvider.js";

export default class CompagnieAll{
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
        const nomRentre = document.querySelector('#compagnie-search-input');
        this.nomCherche = nomRentre ? nomRentre.value.trim() : "";
        await this.setPage(1);
    }

    async render() {
        const rawCompagnies = await CompagnieProvider.fetchCompagnies(this.items_per_page, 1, this.nomCherche);
        const allCompagnies = Array.isArray(rawCompagnies)
            ? rawCompagnies
            : (Array.isArray(rawCompagnies.items) ? rawCompagnies.items : []);
        this.total_pages = Math.max(1, Math.ceil(allCompagnies.length / this.items_per_page));
        this.page_ac = Math.min(Math.max(1, this.page_ac), this.total_pages);
        const start = (this.page_ac - 1) * this.items_per_page;
        const compagnies = allCompagnies.slice(start, start + this.items_per_page);
        let view = `
            <h2 style="text-align: center;">Toutes les compagnies</h2>
            <form class="d-flex" role="search" onsubmit="window.currentArticlePage.submitFilter(event)">
                <input
                    id="compagnie-search-input"
                    class="form-control me-2"
                    type="search"
                    placeholder="Chercher par nom"
                    aria-label="Search"
                    value="${this.nomCherche}"
                />
                <button class="btn btn-outline-success" type="submit">Filtrer</button>
            </form>

            <ul class="list-group">
                ${compagnies.map((compagnie) => `
                    <li class="list-group-item">
                        <a class="list-group-item list-group-item-action" href="#/compagnies/${compagnie.id_compagnie}">
                            ${compagnie.nom_comp}
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
        `;

        return view;
    }
}

