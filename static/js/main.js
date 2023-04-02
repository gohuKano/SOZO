const button_form = document.getElementById("button-form");
const login_box = document.getElementById("login-box");
const login_box_blur = document.getElementById("login-box-blur");
const to_blur = document.querySelectorAll(".to-blur");

function openForm() {
    for (let i = 0; i < to_blur.length; i++) {
        to_blur[i].style.filter = "blur(1.5px)";
    }

    login_box_blur.style.display = "block";
    login_box_blur.style.opacity = 0.6;

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

            for (let i = 0; i < to_blur.length; i++) {
                to_blur[i].style.filter = "blur(0px)";
            }

            if (opacity <= 0) {
                login_box.style.display = "none";
                login_box_blur.style.display = "none";
                login_box_blur.style.opacity = 0;
                document.body.style.filter = "blur(0px)";

                clearInterval(interval);
            }
        }, 10);
    }

});
