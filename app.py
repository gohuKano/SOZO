# TODO : 
# quand le client est connecté, lui faire comprendre
# en changeant l'icone de connexion ou autre methode
# lorsqu'il est connecté, lui offrir la possibilité 
# de voir les settings ( adresse, ... ) de son compte.

# TODO :
# ajouter l'annimation dans le register.html lorsque
# le user client sur un input ( cf. voir site stone island )
# verifier les données rentrer par l'utilisateur : safemark
# pour eviter les attaques par injections

# TODO :
# Mettre à la taille les images du gros caca

# TODO :
# mettre petit bouton pour afficher le mot de passe
# ajouter bouton pour accpter la politique de confidentialité
# accepter la newsletter
# Voir Binance

# TODO :
# ajouter un easter egg dans l'erreur 404
# ex google : "Oops, il n'y a rien a voir ici"

# TODO :
# faire un fonction python validant le login
# ex (flask doc): 
# if valid_login(request.form['username'], request.form['password']):

from flask import Flask, render_template, request, redirect, url_for
import psycopg2
from markupsafe import escape

app = Flask(__name__)

name_of_db = "sozo_db"
username = "hugo_az"
password_database = "sozo"

def get_db_connection():

    conn = psycopg2.connect(
        host = "localhost",
        database = name_of_db,
        user = username,
        password = password_database
    )
    return conn

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/register_process", methods=["POST"])
def register_process():
    # testing if the method is POST
    if request.method == "POST":
        try:
            # get info from the user
            # use the escape() function to prevent
            # injection attacks
            prenom = escape(request.form.get("prenom"))
            nom = escape(request.form.get("nom"))
            email = escape(request.form.get("email"))
            confirm_email = escape(request.form.get("confirm-email"))
            password = escape(request.form.get("password-register"))
            confirm_password = escape(request.form.get("confirm-password"))
            
            print(prenom, nom, email, confirm_email, password, confirm_password)

            # interacting with the database : 
            # # check if the email already exists in the database
            # cur.execute(
            #     'SELECT email FROM accounts WHERE email = %s',
            #     (email,)
            # )
            # existing_email = cur.fetchone()

            # if existing_email:
            #     # display alert message
            #     print("This email is already registered.")
            #     return render_template(
            #                 "register.html",
            #                 alert_message="This email is already registered."
            #             )
            # else:
            #     # write into the database
            #     cur.execute(
            #         'INSERT INTO accounts (prenom, nom, password, email)'
            #         'VALUES (%s, %s, %s, %s)',
            #         (
            #             prenom,
            #             nom,
            #             password,
            #             email
            #         )
            #     )
            #     conn.commit()
            #     print("Data wrote into the database !")
            #     return render_template(
            #                 "register.html",
            #                 alert_message="Account created successfully."
            #             )
            
            return redirect(url_for("index"))

        except Exception as e:
            print(e)
            return redirect(url_for("index"))
    else: 
        return redirect(url_for("index"))


@app.route("/login", methods=["POST"])
def login():

    try:
        # getting data from the user
        email = request.form.get("e-mail")
        password = request.form.get("password")

        print(email, password)

        # connecting to the database
        conn = get_db_connection()
        cur = conn.cursor()

        # check if the email and password match a record in the database
        cur.execute(
            "SELECT * FROM accounts WHERE email = %s AND password = %s",
            (email, password)
        )
        user = cur.fetchone()

        if user:
            # display alert message
            print("Logged in successfully.")
            return redirect(url_for("index"))
        else:
            # display alert message
            print("Invalid email or password.")
            return redirect(url_for("index"))

    except Exception as e:
        print(e)
        return redirect(url_for("index"))

@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template('404.html'), 404

@app.route("/", methods = ["GET", "POST"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
