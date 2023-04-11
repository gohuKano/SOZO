# TODO : 
# quand le client est connecté, lui faire comprendre
# en changeant l'icone de connexion ou autre methode
# lorsqu'il est connecté, lui offrir la possibilité 
# de voir les settings ( adresse, ... ) de son compte.

# TODO :
# verifier les données rentrer par l'utilisateur : escape
# pour eviter les attaques par injections
# refuser la validation du mdp du user 
# si il ne respecte pas les conditions pour le mot de passe

# TODO :
# ajouter bouton pour accpter la politique de confidentialité
# accepter la newsletter
# voir Binance

# TODO :
# ajouter un easter egg dans l'erreur 404
# ex google : "Oops, il n'y a rien a voir ici"

# TODO :
# ajouter la possibilité de se connecté avec google ou apple


from flask import Flask, render_template, request, redirect, url_for
import psycopg2
from markupsafe import escape
from tests.test_auth import *
# functions, from test_auth that need the database connection :
# user_already_register(get_db_connection, email)
# write_user_registration_in_db(get_db_connection, prenom, nom, email, password)


app = Flask(__name__)

NAME_OF_DB = "sozo_db"
USERNAME = "hugo_az"
PASSWORD_OF_DB = "sozo"

def get_db_connection():
    conn = psycopg2.connect(
        host = "localhost",
        database = NAME_OF_DB,
        user = USERNAME,
        password = PASSWORD_OF_DB
    )
    return conn

@app.route("/register")
def register():
    return render_template("auth/register.html")

@app.route("/register_process", methods=["POST"])
def register_process():
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

            if not user_already_register(get_db_connection(), email):
                print("the user is not already register and so can be")
                if email_match(email, confirm_email) and password_match(password, confirm_password):
                    # the email and password match eachother
                    # every precaution taken the data can be written
                    # write_user_registration_in_db(get_db_connection(), prenom, nom, email, password)
                    # every thing has been handled well
                    # the user can be redirected
                    print("write into database")
                    return redirect(url_for("index"))
                else:
                    e = "email or password don't match"
                    print(e)
                    return redirect(url_for("register"), e = e)
            else:
                e = "the user is already register"
                print(e)
                return redirect(url_for("register"), e = e)

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
