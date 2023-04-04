const button_form = document.getElementById("button-form");
const login_box = document.getElementById("login-box");
const login_box_blur = document.getElementById("login-box-blur");
const to_blur = document.querySelectorAll(".to-blur");

function enable_Form() {
    document.getElementById('login-box').classList.toggle("show");

    for (let i = 0; i < to_blur.length; i++) {
        to_blur[i].style.filter = "blur(1.5px)";
    }

    login_box_blur.style.display = "block";
    login_box_blur.style.opacity = 0.6;
    


    // Obtenez la largeur et la hauteur de la fenêtre de l'utilisateur
    const windowWidth = window.innerWidth;
    const windowHeight = window.innerHeight;

    // Obtenez la largeur et la hauteur de la boîte de dialogue
    const loginBoxWidth = login_box.offsetWidth;
    const loginBoxHeight = login_box.offsetHeight;

    // Calculez les coordonnées de la position X et Y pour centrer la boîte de dialogue
    const loginBoxPosX = (windowWidth - loginBoxWidth) / 2;
    const loginBoxPosY = (windowHeight - loginBoxHeight) / 2;

    // Définissez les coordonnées de position X et Y
    login_box.style.left = loginBoxPosX + 'px';
    login_box.style.top = loginBoxPosY + 'px';

    // Montrez la boîte de dialogue
    login_box.style.display = "block";
    login_box.style.opacity = 0;
    let opacity = 0;


    // to change :
    const interval = setInterval(function() {
        opacity += 0.05;
        login_box.style.opacity = opacity;
        if (opacity >= 1) {
            clearInterval(interval);
        }
    }, 10);

    // Empêchez le défilement de la page
    document.documentElement.style.overflow = 'hidden';
}
    

document.addEventListener('click', function(event) {

    const isClickInside = login_box.contains(event.target);
    const button_formIsClicked = button_form.contains(event.target);

    if (!isClickInside && !button_formIsClicked && login_box.style.display === "block") {
        let opacity = 1;
        const interval = setInterval(function() {
            document.documentElement.style.overflow = 'visible';
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

                clearInterval(interval);
            }
        }, 10);
    }

});

// to open responsive menu ( big burger mmmhhhhhhhhhhhhh )
const enable_burger = (e) => {
    document.getElementById('burger').classList.toggle("open");
    document.getElementById("mobile-only__nav").classList.toggle("mobile-only__nav-open");
};
