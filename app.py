from flask import Flask, render_template, request, redirect, url_for, session
import psycopg2
from markupsafe import escape
from datetime import timedelta

# our libs
from tests.test_auth import *
from tests.test_newsletter import *

app = Flask(__name__)

# database parametres
NAME_OF_DB = "sozo_db"
USERNAME = "postgres"
PASSWORD_OF_DB = "sozo"

# cookies parametres
app.secret_key = 'sozo'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_REFRESH_EACH_REQUEST'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

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
            checkbox_subscribe_newsletter = bool(escape(request.form.get("checkbox_subscribe_newsletter")))

            if not user_already_register(get_db_connection(), email):
                print("the user is not already register and so can be")
                if email_match(email, confirm_email) and password_match(password, confirm_password):
                    # the email and password match eachother
                    # every precaution taken the data can be written

                    # write the registration in the db :
                    write_user_registration_in_db(get_db_connection(), prenom, nom, email, password)
                    print("user registered into db where table : account")

                    # subscribe the user to the newsletter
                    if not verify_subscription_newsletter(get_db_connection(), email):
                        if checkbox_subscribe_newsletter:
                            # the user is not already subscribed to the newsletter
                            subscription_to_newsletters(get_db_connection(), prenom, nom, email)

                            # send a email to 

                            return redirect(url_for("index"))
                        else:
                            return redirect(url_for("index"))
                    else:
                        # the user is somehow already subscribed to the newsletter
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
            login_checkbox = bool(request.form.get("login_checkbox"))
            # checking if the user has an account
            if user_has_account(get_db_connection(), email, password):
                session['prenom'] = get_user_data(get_db_connection(), email, password, 1)
                session['nom']  = get_user_data(get_db_connection(), email, password, 2)
                if login_checkbox:
                    app.config['SESSION_PERMANENT'] = True
                    app.config['SESSION_USE_SIGNER'] = True
                    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=365)
                    return redirect(url_for("index"))
                return redirect(url_for("index"))
            else:
                return redirect(url_for("index"))
        except Exception as e:
            print(e)
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

@app.route("/logout_process", methods=["POST"])
def logout_process():
    if request.method == "POST":
        try:
            # kill all session element if there is some
            if len(session) > 0:
                for element in list(session.keys()):
                    session.pop(element)
                return redirect(url_for("index"))
            else:
                return redirect(url_for("index"))
        except Exception as e:
            print(e)
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

@app.route("/subscribe_to_newsletter", methods=["POST"])
def subscribe_to_newsletter():
    if request.method == "POST":
        try:
            # getting data from the user
            email = escape(request.form.get("email"))
            prenom = escape(request.form.get("prenom"))
            nom = escape(request.form.get("nom"))

            if not verify_subscription_newsletter(get_db_connection(), email):
                # the user wants to subscribe and is not already subscribed
                # on peut donc l'inscrire
                # ecris dans la db, table newsletter
                subscription_to_newsletters(get_db_connection(), prenom, nom, email)
                print("the user has subscribed")
                return redirect(url_for("index"))
            else:
                # le user veut s'inscrire MAIS est deja inscrit
                error_message = "le user veut s'inscrire MAIS est deja inscrit"
                print(error_message)
                return redirect(url_for("index"))

        except Exception as e:
            print(e)
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

@app.route("/unsubscribe")
def unsubscribe():
    return render_template("newsletter/unsubscribe.html")

@app.route("/unsubscribe_process", methods=["POST"])
def unsubscribe_process():
    if request.method == "POST":
        try:
            # getting data from the user
            email = escape(request.form.get("email"))
            if verify_subscription_newsletter(get_db_connection(), email):
                # l'user est bien deja subscribed
                # faire suppression de l'user dans la table newsletter:
                remove_from_newsletter(get_db_connection(), email)
                print("the user has unsubscribe")
                # user s'est desabonné de la newsletter
                return redirect(url_for("index"))
            else:
                # l'user n'etait pas inscrit a la newsletter
                print("the user was not subscribe")
                return redirect(url_for("unsubscribe"))
        except Exception as e:
            print(e)
            return redirect(url_for("index"))
    else:
        return redirect(url_for("unsubscribe"))
    
@app.route("/account")
def account():
    return render_template("client/account.html")

@app.route("/cart")
def cart():
    return render_template("client/cart.html")

@app.route("/command")
def command():
    return render_template("client/command.html")
    
@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template('404.html'), 404

@app.route("/", methods = ["GET", "POST"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
