# TODO: 
# ajouter la possibilité de zoomer lorsque que 
# l'user passe la sourie sur l'image
# 
# créer un onglet de connexion...
# 
# Finir l'affichage du texte pour la troisieme image
#
# Changer le nom des ul li en français


from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/form_client_sinscrire", methods = ["POST"])
def form_client_sinscrire():

    try:
        nom = request.form.get('nom')
        prenom = request.form.get('prenom')
        email = request.form.get("e-mail")
        password = request.form.get("password")

        print(nom, prenom, email, password)

    except Exception as e:
        print(e)

    return render_template("index.html")

@app.route("/form_client_se_connecter", methods = ["POST"])
def form_client_se_connecter():

    try:
        nom = request.form.get('nom')
        prenom = request.form.get('prenom')
        email = request.form.get("e-mail")
        password = request.form.get("password")

        print(nom, prenom, email, password)

    except Exception as e:
        print(e)

    return render_template("index.html")


@app.route("/", methods = ["GET", "POST"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
