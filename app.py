# TODO : 
# quand le client est connecté, lui faire comprendre
# en changeant l'icone de connexion ou autre methode
# lorsqu'il est connecté, lui offrir la possibilité 
# de voir les settings ( adresse, ... ) de son compte.

# TODO :
# ajouter l'annimation dans le register.html lorsque
# le user client sur un input ( cf. voir site stone island )

from flask import Flask, render_template, request
import psycopg2

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

    # if request.method == "POST":
    #     try:
    #         # connecting to the database
    #         conn = get_db_connection()
    #         cur = conn.cursor()
    #         print("Connected to the database !")

    #         # get info from the user
    #         prenom = request.form.get('prenom')
    #         nom = request.form.get('nom')
    #         email = request.form.get("e-mail")
    #         password = request.form.get("password")
    #         print(prenom, nom, email, password)

    #         # check if the email already exists in the database
    #         cur.execute(
    #             'SELECT email FROM accounts WHERE email = %s',
    #             (email,)
    #         )
    #         existing_email = cur.fetchone()

    #         if existing_email:
    #             # display alert message
    #             print("This email is already registered.")
    #             return render_template(
    #                         "register.html",
    #                         alert_message="This email is already registered."
    #                     )
    #         else:
    #             # write into the database
    #             cur.execute(
    #                 'INSERT INTO accounts (prenom, nom, password, email)'
    #                 'VALUES (%s, %s, %s, %s)',
    #                 (
    #                     prenom,
    #                     nom,
    #                     password,
    #                     email
    #                 )
    #             )
    #             conn.commit()
    #             print("Data wrote into the database !")
    #             return render_template(
    #                         "register.html",
    #                         alert_message="Account created successfully."
    #                     )

    #     except Exception as e:
    #         print(e)
    #         return render_template(
    #                     "register.html",
    #                     alert_message="An error occurred. Please try again later."
    #             )
    # else: 
    #     return render_template("register.html")

# @app.route("/register_process", methods=["POST"])
# def 

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
            return render_template(
                    "login.html", 
                    alert_message="Logged in successfully."
                )
        else:
            # display alert message
            print("Invalid email or password.")
            return render_template(
                        "index.html",
                        alert_message="Invalid email or password."
                    )

    except Exception as e:
        print(e)
        return render_template(
                "index.html",
                alert_message="An error occurred. Please try again later."
                )

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route("/", methods = ["GET", "POST"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
