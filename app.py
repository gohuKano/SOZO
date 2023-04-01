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

@app.route("/form_client_sinscrire", methods = ["POST"])
def form_client_sinscrire():

    try:
        # connecting to the database
        conn = get_db_connection()
        cur = conn.cursor()
        print("Connected to the database !")

        # get info from the user
        prenom = request.form.get('prenom')
        nom = request.form.get('nom')
        email = request.form.get("e-mail")
        password = request.form.get("password")
        print(prenom, nom, email, password)

        # write into the database, but precaution a prendre
        cur.execute(
            'INSERT INTO accounts (prenom, nom, password, email)'
            'VALUES (%s, %s, %s, %s)',
            (
                prenom,
                nom,
                password,
                email
            )
        )
        conn.commit()
        print("Data wrote into the database !")

    except Exception as e:
        print(e)

    return render_template("index.html")

@app.route("/form_client_se_connecter", methods = ["POST"])
def form_client_se_connecter():

    try:
        email = request.form.get("e-mail")
        password = request.form.get("password")

        print(email, password)

    except Exception as e:
        print(e)

    return render_template("index.html")


@app.route("/", methods = ["GET", "POST"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
