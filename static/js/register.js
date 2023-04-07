// get value for email
const emailInput = document.querySelector('input[name="email"]');
const confirmEmailInput = document.querySelector('input[name="confirm-email"]');
const borderEmail = document.getElementById("border-email")
const borderConfirmEmail = document.getElementById("border-confirm-email");

// get value for password
const passwordInput = document.querySelector('input[name="password-register"]');
const confirmPasswordInput = document.querySelector('input[name="confirm-password"]');
const borderPassword = document.getElementById("border-password")
const borderConfirmPassword = document.getElementById("border-confirm-password");

confirmEmailInput.addEventListener('input', function() {
  const email = emailInput.value;
  const confirmEmail = confirmEmailInput.value;
  if (email !== confirmEmail){
    borderConfirmEmail.style.borderColor = "#c0392b";
    borderEmail.style.borderColor = "#c0392b";
  } else {
    borderConfirmEmail.style.borderColor = "#27ae60";
    borderEmail.style.borderColor = "#27ae60";
  }
});

confirmPasswordInput.addEventListener('input', function() {
  const password = passwordInput.value;
  const confirmPassword = confirmPasswordInput.value;
  if (password !== confirmPassword){
    borderConfirmPassword.style.borderColor = "#c0392b";
    borderPassword.style.borderColor = "#c0392b";
  } else {
    borderConfirmPassword.style.borderColor = "#27ae60";
    borderPassword.style.borderColor = "#27ae60";
  }
});

passwordInput.addEventListener('input', function() {
    // fonction qui verifie si le mot de passe est fort
    // il faut que le mot de passe ai un caractere special
    // 1 chifre une minuscule et une majuscule
    // je veux afficher borderPassword.style.borderColor en vert lorsque le
    // mot de passe est fort, en orange lorsque le mot de passe est intermediare
    // et en rouge lorsque le mot de passe est faible.

    const password = passwordInput.value;
    const char_speciaux = /[!@#$%^&*(),.?":{}|<>]/; // caractères spéciaux autorisés
    const chiffres = /[0-9]/; // chiffres autorisés
    const minuscules = /[a-z]/; // minuscules autorisées
    const majuscules = /[A-Z]/; // majuscules autorisées

    const hasCharSpeciaux = char_speciaux.test(password);
    const hasChiffres = chiffres.test(password);
    const hasMinuscules = minuscules.test(password);
    const hasMajuscules = majuscules.test(password);
    const hasMinLength = password.length >= 8;

    if (hasCharSpeciaux && hasChiffres && hasMinuscules && hasMajuscules && hasMinLength) {
        borderPassword.style.borderColor = "green";
    } else if ((hasCharSpeciaux || hasChiffres || hasMinuscules || hasMajuscules) && password.length >= 8) {
        borderPassword.style.borderColor = "orange";
    } else {
        borderPassword.style.borderColor = "red";
    }

    if (password.length < 8 || !hasCharSpeciaux || !hasChiffres || !hasMinuscules || !hasMajuscules) {
      // Afficher la boîte de dialogue avec les conditions
      const passwordDialog = document.getElementById("password-dialog");
      passwordDialog.style.display = "block";
    }
});


const closePasswordDialog = document.getElementById("close-password-dialog");

closePasswordDialog.addEventListener("click", function() {

  const passwordDialog = document.getElementById("password-dialog");
  passwordDialog.style.display = "none";
  
});

