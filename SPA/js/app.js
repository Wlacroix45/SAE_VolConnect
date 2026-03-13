import Utils from "./services/Utils.js";
import Home from "./views/pages/home.js";
import Error404 from "./views/pages/Error404.js";
import AeroportAll from "./views/pages/AeroportAll.js";
import AeroportShow from "./views/pages/AeroportShow.js";

const routes = {
    '/' : Home,
    '/aeroports' : AeroportAll,
    '/aeroports/:id' : AeroportShow

};

const router = async()=>{
    console.log("Appel router");
    const content = null || document.querySelector('#main');
    let request = Utils.parseRequestURL();
    let parsedUrl = (request.resource ? '/' + request.resource : '/') + (request.id ? '/:id' : '') + (request.verb ? '/' + request.verb : '');
    console.log(parsedUrl);
    let page= routes[parsedUrl] ? new routes[parsedUrl] : new Error404;
    if (page instanceof AeroportAll) {
        window.currentArticlePage = page;
    }
    content.innerHTML = await page.render();
    
}

window.addEventListener('hashchange', router);
window.addEventListener('load', router);