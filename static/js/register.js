const emailInput = document.querySelector('input[name="email"]');
const confirmEmailInput = document.querySelector('input[name="confirm-email"]');
const borderEmail = document.getElementById("border-email")
const borderConfirmEmail = document.getElementById("border-confirm-email");
const passwordInput = document.querySelector('input[name="password-register"]');
const confirmPasswordInput = document.querySelector('input[name="confirm-password"]');
const borderPassword = document.getElementById("border-password")
const borderConfirmPassword = document.getElementById("border-confirm-password");
const img_show = document.getElementById("register__box__img--show");
const img_hide = document.getElementById("register__box__img--hide");
const img_show_2 = document.getElementById("register__box__img_2--show");
const img_hide_2 = document.getElementById("register__box__img_2--hide");
const passwordDialog = document.getElementById("password-dialog");
const registerForm = document.getElementById("register-form");
var passwordLength = document.getElementById("password-length");
var passwordUppercase = document.getElementById("password-uppercase");
var passwordNumber = document.getElementById("password-number");
var passwordSpecial = document.getElementById("password-special");
const char_speciaux = /[!@#$%^&*(),.?":{}|<>]/; // caractères spéciaux autorisés
const chiffres = /[0-9]/; // chiffres autorisés
const minuscules = /[a-z]/; // minuscules autorisées
const majuscules = /[A-Z]/; // majuscules autorisées


emailInput.addEventListener('input', function() {
  const email = emailInput.value;
  const confirmEmail = confirmEmailInput.value;

  if (email !== confirmEmail && email != ""){
    // #c0392b = rouge
    borderConfirmEmail.style.borderColor = "#c0392b";
    borderEmail.style.borderColor = "#c0392b";
  } else if (email == ""){
    borderConfirmEmail.style.borderColor = "#000";
    borderEmail.style.borderColor = "#000";
  } else if (email === confirmEmail) {
    borderConfirmEmail.style.borderColor = "#27ae60";
    borderEmail.style.borderColor = "#27ae60";
  }
});

confirmEmailInput.addEventListener('input', function() {
  const email = emailInput.value;
  const confirmEmail = confirmEmailInput.value;

  if (email !== confirmEmail && email != ""){
    // #c0392b = rouge
    borderConfirmEmail.style.borderColor = "#c0392b";
    borderEmail.style.borderColor = "#c0392b";
  } else if (email == ""){
    borderConfirmEmail.style.borderColor = "#000";
    borderEmail.style.borderColor = "#000";
  } else if (email === confirmEmail) {
    borderConfirmEmail.style.borderColor = "#27ae60";
    borderEmail.style.borderColor = "#27ae60";
  }
});

confirmPasswordInput.addEventListener('input', function() {
  const password = passwordInput.value;
  const confirmPassword = confirmPasswordInput.value;


  const hasCharSpeciaux = char_speciaux.test(password);
  const hasChiffres = chiffres.test(password);
  const hasMinuscules = minuscules.test(password);
  const hasMajuscules = majuscules.test(password);
  const hasMinLength = password.length >= 8;

  if (password != confirmPassword){
    borderConfirmPassword.style.borderColor = "#c0392b";
    borderPassword.style.borderColor = "#c0392b";
  } else if (hasCharSpeciaux && hasChiffres && hasMinuscules && hasMajuscules && hasMinLength) {
    borderConfirmPassword.style.borderColor = "#27ae60";
    borderPassword.style.borderColor = "#27ae60";
  }
  if (password == "") {
    borderPassword.style.borderColor = "#000";
    borderConfirmPassword.style.borderColor = "#000";
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

    const hasCharSpeciaux = char_speciaux.test(password);
    const hasChiffres = chiffres.test(password);
    const hasMinuscules = minuscules.test(password);
    const hasMajuscules = majuscules.test(password);
    const hasMinLength = password.length >= 8;

    if (hasMinLength) {
      passwordLength.style.color = "green";
    } else {
      passwordLength.style.color = "white";
    }
    
    if (hasMajuscules) {
      passwordUppercase.style.color = "green";
    } else {
      passwordUppercase.style.color = "white";
    }
    
    if (hasChiffres) {
      passwordNumber.style.color = "green";
    } else {
      passwordNumber.style.color = "white";
    }
    
    if (hasCharSpeciaux) {
      passwordSpecial.style.color = "green";
    } else {
      passwordSpecial.style.color = "white";
    }



    if (hasCharSpeciaux && hasChiffres && hasMinuscules && hasMajuscules && hasMinLength) {
      borderPassword.style.borderColor = "green";
    } else if ((hasCharSpeciaux || hasChiffres || hasMinuscules || hasMajuscules) && password.length >= 8) {
      borderPassword.style.borderColor = "orange";
    } else {
      borderPassword.style.borderColor = "red";
    }
    if (password == "") {
      borderPassword.style.borderColor = "#000";
      borderConfirmPassword.style.borderColor = "#000";
    }
});

const show_psw = (e) => {
  img_hide.classList.add("show");
  img_show.classList.add("show");
  passwordInput.type = "text";
};

const hide_psw = (e) => {
  document.getElementById('register__box__img--hide').classList.remove("show");
  document.getElementById("register__box__img--show").classList.remove("show");
  passwordInput.type = "password";
};

const show_psw_2 = (e) => {
  img_hide_2.classList.add("show");
  img_show_2.classList.add("show");
  confirmPasswordInput.type = "text";
};

const hide_psw_2 = (e) => {
  document.getElementById('register__box__img_2--hide').classList.remove("show");
  document.getElementById("register__box__img_2--show").classList.remove("show");
  confirmPasswordInput.type = "password";
};


// prevent the user to send the form if the
// password and confirmPassword doesnt match
registerForm.addEventListener('submit', (event) => {
  const email = emailInput.value;
  const confirmEmail = confirmEmailInput.value;
  const password = passwordInput.value;
  const confirmPassword = confirmPasswordInput.value;

  const hasCharSpeciaux = char_speciaux.test(password);
  const hasChiffres = chiffres.test(password);
  const hasMinuscules = minuscules.test(password);
  const hasMajuscules = majuscules.test(password);
  const hasMinLength = password.length >= 8;

  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  const validEmail = emailPattern.test(email);

  // verification of emails
  if (email !== confirmEmail) {
    event.preventDefault();
    alert('Les adresses e-mail ne correspondent pas.');
  }

  // verification is email is valid
  if (!validEmail) {
    event.preventDefault();
    alert('L\'adresse e-mail n\'est pas valide.');
  }

  // verification of passwords
  if (password!== confirmPassword) {
    event.preventDefault();
    alert('Les mots de passes ne correspondent pas.');
  }

  // verification of password security
  if (!(hasCharSpeciaux && hasChiffres && hasMinuscules && hasMajuscules && hasMinLength)) {
    event.preventDefault();
    alert('Le mot de passe n\'est pas assez securisé');
  }
});
