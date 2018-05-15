from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from os import listdir
from functools import wraps

app = Flask(__name__)

#Author: Martin
def get_headlines():
    headlines = listdir("static/cleaning_articles")
    headline_list = []

    for headline in headlines:
        headline = headline[:-4]
        headline_list.append(headline)
    return headline_list


#Author: Martin
def get_title_content(a):
    headlines = listdir("static/cleaning_articles")
    headline_list = []
    for headline in headlines:
        if headline == a + ".txt":
            path = "static/cleaning_articles/" + headline
            asd = days_file = open(path,'r')
            text = asd.read()
        else:
            print("test")
    return(a + ": " +
    text)


def is_logged_in(f):
    ''' Används för att göra vissa sidor synliga för endast inloggade användare '''
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("För att ta del av den här sidan måste du logga in", "primary")
            return redirect(url_for("login"))
    return wrap


#Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'cudb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

#init MYSQL
mysql = MySQL(app)


@app.route("/")
def index():
    return render_template("index.html", author="Christopher")


@app.route("/edit/")
def edit_article():
    return render_template("edit.html", author="Martin")


@app.route("/update/", methods=["POST"])
def update():

    headline = request.form.get("headline")
    content = request.form.get("content")
    article_path = "static/cleaning_articles/" + str(headline) + ".txt"

    my_file = open(article_path, "w")
    my_file.write(content)
    my_file.close()

    return redirect("/article_list/")


@app.route("/to_do_list/")
@is_logged_in
def to_do_list():
    return render_template("to_do_list.html", title="To Do", author="Christopher")


@app.route("/calendar/")
@is_logged_in
def calendar():
    return render_template("calendar.html", title="Kalender", author="Martin")


@app.route("/cleaning_tips/")
def cleaning_tips():
    return render_template("cleaning_tips.html", title="Städtips", author="Christopher")


@app.route("/article_list/")
def article_list():
    return render_template("article_list.html", title="Lexikon A-Ö", headlines = get_headlines(), author="Martin")


@app.route("/static/cleaning_articles/<headline>")
def article(headline):
    titel = headline
    return render_template("article.html", test = get_title_content(titel), headlines = get_headlines(), author="Martin")


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
@is_logged_in
def account():
    return render_template("my_account.html", title="Mitt konto")


@app.route("/my_home/")
@is_logged_in
def my_home():
    return render_template("my_home.html", title="Min bostad", author="Christopher")


@app.route("/static/<path:path>")
def serve_static_files(path):
    return send_from_directory("static", path)


if __name__ == "__main__":
    app.secret_key='secret123'
    app.run(debug=True)
