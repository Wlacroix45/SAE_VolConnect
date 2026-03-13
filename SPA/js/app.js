import Utils from "./services/Utils.js";
import Home from "./views/pages/home.js";
import Error404 from "./views/pages/Error404.js";

const routes = {
    '/' : Home
};

const router = async()=>{
    console.log("Appel router");
    const content = null || document.querySelector('#main');
    let request = Utils.parseRequestURL();
    let parsedUrl = (request.resource ? '/' + request.resource : '/') + (request.id ? '/:id' : '') + (request.verb ? '/' + request.verb : '');
    console.log(parsedUrl);
    let page= routes[parsedUrl] ? new routes[parsedUrl] : new Error404;
    content.innerHTML = await page.render();
}

window.addEventListener('hashchange', router);
window.addEventListener('load', router);