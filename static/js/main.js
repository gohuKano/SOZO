const login_box = document.getElementById("login-box");
const button_form = document.getElementById("button-form");

function openForm() {
    console.log("Opening login box...");

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
    console.log("Clicked outside login box...");

    const isClickInside = login_box.contains(event.target);
    const button_formIsClicked = button_form.contains(event.target);

    console.log("isClickInside: ", isClickInside);

    if (!isClickInside && !button_formIsClicked && login_box.style.display === "block") {
        let opacity = 1;
        const interval = setInterval(function() {
            opacity -= 0.05;
            login_box.style.opacity = opacity;
            if (opacity <= 0) {
                login_box.style.display = "none";
                clearInterval(interval);
            }
        }, 10);

        console.log("Closing login box...");
    }
});
