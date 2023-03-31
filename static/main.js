// get the buttons to hide and show the form
const compte_button_show = document.getElementById("compte-button-show");
const compte_button_hide = document.getElementById("compte-button-hide");

// get the form_client element
const form_client = document.getElementById("form-client-div");


// when the compte_button element is touched by the user,
// the form will change its position and it will be visible by the user
compte_button_show.addEventListener("click", () => {

    form_client.style.top = "0vh";
    form_client.style.transition = "top 1s cubic-bezier(.12,1.01,.62,.96)";
});

compte_button_hide.addEventListener("click", () => {

    form_client.style.top = "-60vh";
    form_client.style.transition = "top 1s cubic-bezier(.12,1.01,.62,.96)";
});