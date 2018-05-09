from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from os import listdir
from functools import wraps

app = Flask(__name__)


def get_headlines():
    headlines = listdir("static/cleaning_articles")
    headline_list = []

    for headline in headlines:
        headline = headline[:-4]
        headline_list.append(headline)
    return headline_list


def get_title_content(a):
    headlines = listdir("static/cleaning_articles")
    headline_list = []
    for headline in headlines:
        if headline == a + ".txt":
            path = "static/cleaning_articles" + headline
            asd = days_file = open(path,'r')
            text = asd.read()
        else:
            print("test")
    return(a + " : " + text)

#Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'clean417k(dj'
app.config['MYSQL_DB'] = 'cudb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

#init MYSQL
mysql = MySQL(app)


@app.route("/")
def index():
    return render_template("index.html", author="Christopher")


@app.route("/to_do_list/")
def to_do_list():
    return render_template("to_do_list.html", title="To Do", author="Christopher")


@app.route("/calendar/")
def calendar():
    return render_template("calendar.html", title="Kalender", author="Martin")


@app.route("/cleaning_tips/")
def cleaning_tips():
    return render_template("cleaning_tips.html", title="Städtips", author="Christopher")


@app.route("/article_list/")
def article_list():
    return render_template("article_list.html", title="Lista A-Ö", headlines = get_headlines())


@app.route("/static/cleaning_articles/<headline>")
def wiki(headline):
    titel=headline
    return render_template("article.html", test=get_titlecontent(titel), headlines = get_headlines())


class Register(Form):
    email = StringField("E-post", [validators.Length(min=5, max=50)])
    password = PasswordField("Lösenord", [validators.DataRequired(), validators.EqualTo("confirm", message="Fel lösenord")])
    confirm = PasswordField("Bekräfta lösenord")


@app.route("/register/", methods=["GET", "POST"])
def register():
    form = Register(request.form)
    if request.method == "POST" and form.validate():
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # Create cursor
        cur = mysql.connection.cursor()

        # Execute query
        cur.execute("INSERT INTO user_password(email, password) VALUES (%s, %s)", (email, password))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        # Registration message with categories
        flash('Du är nu registrerad och kan logga in', 'success')
        return redirect(url_for("login"))

    return render_template("register.html", form=form, title="Registrera", author="Martin")


@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #Get forms Fields
        email = request.form["email"]
        password_candidate = request.form["password"]

        #create cursor
        cur = mysql.connection.cursor()

        #Get user my email
        result = cur.execute("SELECT * FROM user_password WHERE email = %s", [email])

        if result > 0:
            #Get stored hash
            data = cur.fetchone()
            password = data["password"]

            #compare Passwords
            if sha256_crypt.verify(password_candidate, password):
                session["logged_in"] = True
                session["username"] = email
                flash("Du är nu inloggad", "success")
                return redirect(url_for("index"))
            else:
                error = "Ogiltigt lösenord"
                return render_template("/login.html", error=error)
            cur.close()
        else:
            error = "Ingen användare hittades med denna epost"
            return render_template("/login.html", error=error)

    return render_template("login.html", title="Logga in", author="Martin/Anders")


@app.route("/logout/")
def logout():
    session.clear()
    return redirect(url_for("index"))


@app.route("/my_account/")
def account():
    return render_template("my_account.html", title="Mitt konto")


@app.route("/my_home/")
def my_home():
    return render_template("my_home.html", title="Min bostad", author="Christopher")


@app.route("/static/<path:path>")
def serve_static_files(path):
    return send_from_directory("static", path)





if __name__ == "__main__":
    app.secret_key='secret123'
    app.run(debug=True)
