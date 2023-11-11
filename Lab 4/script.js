// ==UserScript==
// @name         Lab 4
// @namespace    https://cripto.tiiny.site/
// @version      0.1
// @description  Este código permite obtener la llave para el descifrado de los mensajes ocultos en la página web
// @author       Natalia
// @match        https://cripto.tiiny.site/
// @icon         https://www.google.com/s2/favicons?sz=64&domain=tiiny.site
// @grant        none
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.2.0/crypto-js.min.js#sha512-a+SUDuwNzXDvz4XrIcXHuCf089/iJAoN4lmrXJg18XnduKK6YlDHNRalv4yd1N40OKI80tFidF+rqTFKGPoWFQ==
// ==/UserScript==

function getKey() {
    var pText = document.querySelector("p").innerText; // se obtiene texto del parrafo
    var upper = pText.match(/[A-Z]/g);
    if (upper) {
        var key = upper.join("");
    }
    return key;
}
function getIds(){
    var ids = [];
    var elements = document.querySelectorAll('[class*="M"]'); // se obtienen elementos que contengan M en su clase (ejemplo: M1)
    elements.forEach(function(element) {
        ids.push(element.id); //se guarda id del elemento (msj cifrado)
    });
    return ids;
}
function msg(){
    var ids = getIds();
    console.log("La llave es: "+getKey());
    console.log("Los mensajes cifrados son: "+ids.length);
    //console.log(ids); //imprime ids
}
function printHtml(text){
    var body = document.body;
    var newPharr = document.createElement('p');
    newPharr.textContent = text;
    body.appendChild(newPharr);

}
function decryptMsg(){
    var ids = getIds();
    var key = getKey();
    var planeText = [];
    var keyWordArray = CryptoJS.enc.Utf8.parse(key); // Convertir la clave a formato WordArray
    for (var i = 0; i <= ids.length; i++) {
        var bytesId = CryptoJS.enc.Base64.parse(ids[i]);
        var TripleDES = CryptoJS.TripleDES.decrypt({ ciphertext: bytesId }, keyWordArray, { mode: CryptoJS.mode.ECB }).toString(CryptoJS.enc.Utf8);
        printHtml(TripleDES);
        console.log(ids[i]+" "+TripleDES);
    }
}
(function() {
    msg();
    decryptMsg();
})();
