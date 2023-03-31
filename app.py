# TODO: 
# ajouter la possibilité de zoomer lorsque que 
# l'user passe la sourie sur l'image
# 
# créer un onglet de connexion...
# 
# Finir l'affichage du texte pour la troisieme image
#
# Changer le nom des ul li en français


from flask import Flask, render_template


app = Flask(__name__)

@app.route("/form_client", methods = ["GET", "POST"])
def form_client():

    print("ok")

    return render_template("index.html")


@app.route("/", methods = ["GET", "POST"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
