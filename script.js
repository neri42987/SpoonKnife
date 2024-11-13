function showAlert() {
    alert("Bonjour depuis le script JavaScript");
}
function showConsoleMessage() {
console.log("ce message est affiché dans la console."); 
}
var teams = [];
function addTeam(team) {
    if (!teams.includes(team)) {
        teams.push(team);
        console.log(team + " has been added to the list");
    } else {
        console.log(team + " is already on the list");
    }
}
//testttt 
function showList() {
    console.log("Finals liste :");
    teams.forEach(function(team) {
        console.log(team);
    });
}

//testtttttt
window.onload = function() {
showAlert();
showConsoleMessage();
addTeam("T1");
addTeam("GENG");
addTeam("HLE");
showList(); 

}; 

