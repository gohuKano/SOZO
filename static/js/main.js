const button_form = document.getElementById("button-form");
const login_box = document.getElementById("login-box");
const login_box_blur = document.getElementById("login-box-blur");

function openForm() {

    login_box_blur.style.display = "block";
    login_box_blur.style.opacity = 0.7;
    login_box_blur.style.filter = "blur(10px)";

    login_box.style.display = "block";
    login_box.style.opacity = 0;
    let opacity = 0;

    const interval = setInterval(function() {
        opacity += 0.05;
        login_box.style.opacity = opacity;
        if (opacity >= 1) {
            clearInterval(interval);
        }
    }, 10);
}

document.addEventListener('click', function(event) {

    const isClickInside = login_box.contains(event.target);
    const button_formIsClicked = button_form.contains(event.target);

    if (!isClickInside && !button_formIsClicked && login_box.style.display === "block") {
        let opacity = 1;
        const interval = setInterval(function() {
            opacity -= 0.05;
            login_box.style.opacity = opacity;
            login_box_blur.style.opacity -= 0.03;

            if (opacity <= 0) {
                login_box_blur.style.display = "none";
                login_box_blur.style.display = "none";
                login_box_blur.style.opacity = 0;

                clearInterval(interval);
            }
        }, 10);
    }
});
