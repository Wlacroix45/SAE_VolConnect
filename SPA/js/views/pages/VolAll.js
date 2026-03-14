import VolProvider from "../../services/VolProvider.js";

export default class VolAll{
    constructor() {
        this.page_ac = 1;
        this.items_per_page = 10;
        this.total_pages = null;
        this.nomCherche = "";
    }

    async setPage(newPage) {
        this.page_ac = newPage;
        const content = document.querySelector('#main');
        content.innerHTML = await this.render();
    }

    async submitFilter(event) {
        event.preventDefault();
        const nomRentre = document.querySelector('#compagnie-search-input');
        this.nomCherche = nomRentre ? nomRentre.value.trim() : "";
        await this.setPage(1);
    }

    async render(){
        let vols = await VolProvider.fetchVols(10, this.page_ac, this.nomCherche);
        let view = `
            <h2 style="text-align: center;">Tous les vols</h2>
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
                ${vols.map(
                    vols => 
                        `
                            <li class="list-group-item"><a class="list-group-item list-group-item-action" href="#/vols/${vols.id_vol}">${vols.nom_vol}</a></li>
                    `
                ).join("\n")}
             </ul>

            <nav aria-label="Page navigation exemple">
                <ul class="pagination">
                    <li class="page-item ${this.page_ac === 1 ? 'disabled' : ''}">
                        <a class="page-link" href="#" onclick="event.preventDefault(); window.currentArticlePage.setPage(${Math.max(1, this.page_ac - 1)})" aria-label="Previous">
                        <span aria-hidden="true">&laquo;</span>
                        </a>
                    </li>
                    <li class="page-item ${this.page_ac === 1 ? 'active' : ''}">
                        <a class="page-link" href="#" onclick="event.preventDefault(); window.currentArticlePage.setPage(1)">1</a>
                    </li>
                    <li class="page-item ${this.page_ac === 2 ? 'active' : ''}">
                        <a class="page-link" href="#" onclick="event.preventDefault(); window.currentArticlePage.setPage(2)">2</a>
                    </li>
                    <li class="page-item ${this.page_ac === 3 ? 'active' : ''}">
                        <a class="page-link" href="#" onclick="event.preventDefault(); window.currentArticlePage.setPage(3)">3</a>
                    </li>
                    <li class="page-item">
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

