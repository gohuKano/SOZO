// Temps en millisecondes avant que la boîte de dialogue apparaisse
// boite de dialogue de l'inscription a la newsletter
const DELAY = 1000;

// Fonction pour afficher la boîte de dialogue
function showPopup() {
  document.getElementById("newsletter-popup").style.display = "block";
}

// Fonction pour fermer la boîte de dialogue
function closePopup() {
  document.getElementById("newsletter-popup").style.display = "none";
}

// Démarre la minuterie pour afficher la boîte de dialogue
setTimeout(showPopup, DELAY);