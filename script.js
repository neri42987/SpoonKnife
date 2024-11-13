function showAlert() {
    alert("Bonjour depuis le script JavaScript");
}
function showConsoleMessage() {
console.log("ce message est affiché dans la console."); 
}

window.onload = function() {
showAlert();
showConsoleMessage();
}; 

