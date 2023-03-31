// get the element in the html
const compte_button_show = document.getElementById("compte-button-show");
const compte_button_hide = document.getElementById("compte-button-hide");
const form_client = document.getElementById("form-client-div");


// when the compte_button element is touched by the user,
// the form will change its position and it will be visible by the user
compte_button_show.addEventListener("click", () => {

    form_client.style.top = "0vh";
    form_client.style.transition = "top 0.7s ease-in-out";
});