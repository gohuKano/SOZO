const button_form = document.getElementById("button-form");
const login_box = document.getElementById("login-box");
const login_box_blur = document.getElementById("login-box-blur");
const to_blur = document.querySelectorAll('.to-blur');
const header = document.getElementById("header");

function enable_Form() {
    document.getElementById('login-box').classList.toggle("show");
    document.getElementById('login-box-blur').classList.toggle("show");
    document.body.classList.toggle('show');

    to_blur.forEach(element => {
          element.classList.toggle('show');
      });   
}

document.addEventListener('click', (event) => {
  // Vérifier si l'élément cliqué est dans la boîte de dialogue
  const isClickedInside = login_box.contains(event.target);
  const button_formIsClicked = button_form.contains(event.target);

  // Si l'élément cliqué n'est pas dans la boîte de dialogue, masquer la boîte de dialogue
  if (!isClickedInside && !button_formIsClicked ) {
    login_box.classList.remove('show');
    login_box_blur.classList.remove('show');
    document.body.classList.remove('show');

    to_blur.forEach(element => {
      element.classList.remove('show');
    });
  }
});

// to open responsive menu ( big burger mmmhhhhhhhhhhhhh )
const enable_burger = (e) => {
  document.getElementById('burger').classList.toggle("open");
  document.getElementById("mobile-only__nav").classList.toggle("mobile-only__nav-open");
};

document.addEventListener("mousewheel", function(event){
    if(event.wheelDelta > 0){
        header.classList.remove("hide");
  } else {
        header.classList.add("hide");
  }
})


