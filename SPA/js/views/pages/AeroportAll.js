import AeroportProvider from "../../services/AeroportProvider.js";

export default class AeroportAll{
    constructor() {
        this.page_ac = 1;
        this.items_per_page = 10;
        this.total_pages = null;
    }

    async setPage(newPage) {
        this.page_ac = newPage;
        const content = document.querySelector('#main');
        content.innerHTML = await this.render();
    }

    async render(){
        let aeroports = await AeroportProvider.fetchAeroports(10, this.page_ac);
        let view = `
            <h2 style="text-align: center;">Tous les aeroports</h2>
            <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search"/>
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
            <ul class="list-group">
                ${aeroports.map(
                    aeroports => 
                        `
                            <li class="list-group-item"><a class="list-group-item list-group-item-action" href="#/aeroports/${aeroports.id_aeroport}">${aeroports.nom_aeroport}</a></li>
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

