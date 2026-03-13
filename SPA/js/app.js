import Utils from "./services/Utils.js";
import Home from "./views/pages/home.js";
import Error404 from "./views/pages/Error404.js";
import AeroportAll from "./views/pages/AeroportAll.js";
import AeroportShow from "./views/pages/AeroportShow.js";
import TerminalAll from "./views/pages/TerminalAll.js";
import TerminalShow from "./views/pages/TerminalShow.js";
import CompagnieAll from "./views/pages/CompagnieAll.js";
import CompagnieShow from "./views/pages/CompagnieShow.js";
import VolAll from "./views/pages/VolAll.js";
import VolShow from "./views/pages/VolShow.js";

const routes = {
    '/' : Home,
    '/aeroports' : AeroportAll,
    '/aeroports/:id' : AeroportShow,
    '/terminaux' : TerminalAll,
    '/terminaux/:id' : TerminalShow,
    '/compagnies' : CompagnieAll,
    '/compagnies/:id' : CompagnieShow,
    '/vols' : VolAll,
    '/vols/:id' : VolShow

};

const router = async()=>{
    console.log("Appel router");
    const content = null || document.querySelector('#main');
    let request = Utils.parseRequestURL();
    let parsedUrl = (request.resource ? '/' + request.resource : '/') + (request.id ? '/:id' : '') + (request.verb ? '/' + request.verb : '');
    console.log(parsedUrl);
    let page= routes[parsedUrl] ? new routes[parsedUrl] : new Error404;
    if (page instanceof AeroportAll || page instanceof TerminalAll || page instanceof CompagnieAll || page instanceof VolAll){
        window.currentArticlePage = page;
    }
    content.innerHTML = await page.render();
    
}

window.addEventListener('hashchange', router);
window.addEventListener('load', router);