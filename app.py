# TODO : 
# quand le client est connecté, lui faire comprendre
# en changeant l'icone de connexion ou autre methode
# lorsqu'il est connecté, lui offrir la possibilité 
# de voir les settings ( adresse, ... ) de son compte.

# TODO :
# ajouter l'annimation dans le register.html lorsque
# le user client sur un input ( cf. voir site stone island )
# verifier les données rentrer par l'utilisateur : escape
# pour eviter les attaques par injections

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

def email_match(email, email_to_confirm):
    if email == email_to_confirm:
        return 1
    else: return 0

def password_match(password, password_to_confirm):
    if password == password_to_confirm:
        return 1
    else: return 0

def user_already_register(email):
    '''
    check if the email already exists in the database
    if the mail exist the function returns 1 and so the
    user is supposed to already has an account
    '''
    # search into the database if the email is already register
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'SELECT email FROM accounts WHERE email = %s',
        (email,)
    )
    existing_email = cur.fetchone()
    
    if existing_email:
        # return 1 if user already register
        # 1 is yes, the user is already register
        return 1
    else:
        # return 0 if user is not already register
        # 0 is no, the user is not already register
        return 0
    
def write_user_registration_in_db(prenom, nom, email, password):
    '''
    function that writes into the database
    the data is supposed to have been checked
    before writing to the database
    '''
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO accounts (prenom, nom, email, password)'
        'VALUES (%s, %s, %s, %s)',
        (
            prenom,
            nom,
            email,
            password
        )
    )
    conn.commit()

    print("data write into database")

@app.route("/register")
def register():
    return render_template("register.html")

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

            if not user_already_register(email):
                print("the user is not already register and so can be")
                if email_match(email, confirm_email) and password_match(password, confirm_password):
                    # the email and password match eachother
                    # every precaution taken the data can be written
                    write_user_registration_in_db(prenom, nom, email, password)
                    # every thing has been handled well
                    # the user can be redirected
                    return redirect(url_for("index"))
                else:
                    e = "email or password don't match"
                    print(e)
                    return redirect(url_for("register"))
            else:
                e = "the user is already register"
                print(e)
                return redirect(url_for("register"))

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
