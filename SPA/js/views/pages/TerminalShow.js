import TerminalProvider from "../../services/TerminalProvider.js"
import Utils  from "../../services/Utils.js";   

export default class TerminalShow{
    async render(){
        let url = Utils.parseRequestURL();
        console.log("URL ", url);
        let terminal = await TerminalProvider.getTerminal(url.id);
        console.log("Le terminal choisi ", terminal);
        return `
            <div class="card border-info mb-3" style="max-width: 18rem; align-items: center;">
                <div class="card-header"> Id : ${terminal.id_terminal}</div>
                <div class="card-body text-info">
                    <h5 class="card-title">${terminal.nom_terminal}</h5>
                </div>
            </div>
        `;
    }
}
