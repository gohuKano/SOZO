# TODO :
# verifier les données rentrer par l'utilisateur : escape
# pour eviter les attaques par injections
# refuser la validation du mdp du user 
# si il ne respecte pas les conditions pour le mot de passe

# TODO :
# ajouter un easter egg dans l'erreur 404
# ex google : "Oops, il n'y a rien a voir ici"

# TODO :
# ajouter la possibilité de se connecter avec google ou apple
# compliqué pour le moment car il faut avoir numéro NUND --> voir site apple developer

# TODO :
# faire la page profile client html

# TODO :
# changer le login form
# ecrire un message pour faire comprendre a l'utilisateur
# qu'il est connecte ex: 'Bonjour Hugo.'
# dans le login form changé ajouter 3 boutons :
# i) Acceder à mon profile
# ii) Bouton Deconexion
# iii) Mon historique de commande


from flask import Flask, render_template, request, redirect, url_for, session
import psycopg2
from markupsafe import escape

# our libs
from tests.test_auth import *
from tests.test_newslatter import *


app = Flask(__name__)
app.secret_key = 'sozo'

NAME_OF_DB = "sozo_db"
USERNAME = "postgres"
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

                    # write the registration in the db
                    write_user_registration_in_db(get_db_connection(), prenom, nom, email, password)
                    # every thing has been handled well
                    # the user can be redirected
                    print("write into database")
                    return redirect(url_for("index"))
                else:
                    e = "email or password don't match"
                    print(e)
                    return redirect(url_for("register"))
            else:
                e = "the user is already register"
                print(e)
                return redirect(url_for("register"))
        except Exception as e:
            print(e)
            return redirect(url_for("index"))
    else: 
        return redirect(url_for("index"))


@app.route("/login_process", methods=["POST"])
def login_process():
    if request.method == "POST":
        try:
            # getting data from the user
            email = escape(request.form.get("e-mail"))
            password = escape(request.form.get("password"))

            print(email, password)

            if user_has_account(get_db_connection(), email, password):
                name_of_user = get_user_data(get_db_connection(), email, password, 1)
                print(name_of_user)

                session['name_of_user'] = name_of_user
                return redirect(url_for("index"))
            else:
                return redirect(url_for("index"))
            
        except Exception as e:
            print(e)
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))
    
@app.route("/subscribe_to_newslatter", methods=["POST"])
def subscribe_to_newslatter():
    if request.method == "POST":
        try:
            # getting data from the user
            email = escape(request.form.get("email"))
            prenom = escape(request.form.get("prenom"))
            nom = escape(request.form.get("nom"))

            if not verify_subscription_newslatter(get_db_connection(), email, prenom, nom):
                # the user wants to subscribe and is not already subscribed
                # on peut donc l'inscrire
                # ecris dans la db, table newsletter
                subscription_to_newslatters(get_db_connection(), prenom, nom, email)
                print("the user has subscribed")
                return redirect(url_for("index.html"))
            else:
                # le user veut s'inscrire MAIS est deja inscrit
                error_message = "le user veut s'inscrire MAIS est deja inscrit"
                print(error_message)
                return redirect(url_for("index.html"), erro_message = error_message)

        except Exception as e:
            print(e)
            return redirect(url_for("index.html"))
    else:
        return redirect(url_for("index.html"))

@app.route("/unsubscribe")
def unsubscribe():
    return render_template("newsletter/unsubscribe.html")

@app.route("/unsubscribe_process", methods=["POST"])
def unsubscribe_process():
    if request.method == "POST":
        try:
            # getting data from the user
            email = escape(request.form.get("email"))
            prenom = escape(request.form.get("prenom"))
            nom = escape(request.form.get("nom"))
            
            if verify_subscription_newslatter(get_db_connection(), email, prenom, nom):
                # l'user est bien deja subscribed
                # faire suppression de l'user dans la table newslatter:
                remove_from_newsletter(get_db_connection(), email)
                print("the user has unsubscribe")
                # user s'est desabonné de la newslatter
                return redirect(url_for("index"))
            else:
                # l'user n'etait pas inscrit a la newslatter
                print("the user was not subscribe")
                return redirect(url_for("unsubscribe"))
        except Exception as e:
            print(e)
            return redirect(url_for("index"))
    else:
        return redirect(url_for("unsubscribe"))
    
@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template('404.html'), 404

@app.route("/", methods = ["GET", "POST"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
