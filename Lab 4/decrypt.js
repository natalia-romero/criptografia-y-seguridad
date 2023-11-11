
const CryptoJS = require('crypto-js');
var key = "SEGUROSEGUROSEGUROSEGURO";
var msg = "c8zxLt/4Iuk=";
var keyWordArray = CryptoJS.enc.Utf8.parse(key); // Convertir la clave a formato WordArray
var bytesId = CryptoJS.enc.Base64.parse(msg);
var TripleDES = CryptoJS.TripleDES.decrypt({ ciphertext: bytesId }, keyWordArray, { mode: CryptoJS.mode.ECB }).toString(CryptoJS.enc.Utf8);
console.log("Mensaje cifrado: " +msg +" Mensaje decifrado: "+TripleDES);