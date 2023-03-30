# TODO: ajouter la possibilité de zoomer lorsque que 
# l'user passe la sourie sur l'image
# créer un onglet de connexion

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
