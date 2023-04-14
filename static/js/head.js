const button_form = document.getElementById("button-form");
const login_box = document.getElementById("login-box");
const login_box_blur = document.getElementById("login-box-blur");
const logged_box = document.getElementById("logged-box");
const logged_box_blur = document.getElementById("logged-box-blur");
const to_blur = document.querySelectorAll('.to-blur');
const header = document.getElementById("header");

function enable_loginBox() {
  document.getElementById('login-box').classList.toggle("show");
  document.getElementById('login-box-blur').classList.toggle("show");
  document.body.classList.toggle('show');

  to_blur.forEach(element => {
    element.classList.toggle('show');
  });   
}

function enable_loggedBox() {
  document.getElementById('logged-box').classList.toggle("show");
  document.getElementById('logged-box-blur').classList.toggle("show");
  document.body.classList.toggle('show');

  to_blur.forEach(element => {
    element.classList.toggle('show');
  });   
}

document.addEventListener('click', (event) => {
  // Vérifier si l'élément cliqué est dans la boîte de dialogue
  const isClickedInside = login_box.contains(event.target) | logged_box.contains(event.target);
  const button_formIsClicked = button_form.contains(event.target);

  // Si l'élément cliqué n'est pas dans la boîte de dialogue, masquer la boîte de dialogue
  if (!isClickedInside && !button_formIsClicked ) {
    login_box.classList.remove('show');
    login_box_blur.classList.remove('show');
    logged_box.classList.remove('show');
    logged_box_blur.classList.remove('show');
    document.body.classList.remove('show');

    to_blur.forEach(element => {
      element.classList.remove('show');
    });
  }
});

const show_psw_log = (e) => {
  document.getElementById('login-box__input__img--hide').classList.add("show");
  document.getElementById("login-box__input__img--show").classList.add("show");
  document.querySelector('input[name="password"]').type = "text";
};

const hide_psw_log = (e) => {
  document.getElementById('login-box__input__img--hide').classList.remove("show");
  document.getElementById("login-box__input__img--show").classList.remove("show");
  document.querySelector('input[name="password"]').type = "password";
};

// to open responsive menu ( big burger mmmhhhhhhhhhhhhh )
const enable_burger = (e) => {
  document.getElementById('burger').classList.toggle("open");
  document.getElementById("mobile-only__nav").classList.toggle("mobile-only__nav-open");
};

let prevScrollpos = window.pageYOffset;

window.addEventListener("scroll", function() {
  let currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    header.classList.remove("hide");
  } else {
    header.classList.add("hide");
  }
  prevScrollpos = currentScrollPos;
});
