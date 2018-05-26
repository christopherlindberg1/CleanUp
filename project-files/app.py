from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt
from functools import wraps
import yaml

# Nedan importeras funktioner och klasser från egna filer
from functions import get_headlines, get_title_content
from forms import Register, Login, ArticleForm

app = Flask(__name__)

''' Konfigurationen nedan används för att få tillgång till vår
online MySQL-databas. Lösenord och annan information hämtas från
en annan fil - db.yaml - som inte pushas upp på git. filen ligger i en mapp två nivåer
över denna fil. För att kunna köra applikaitonen med denna konfiguration behövs därför
en fil med de rätta inloggningsuppgifterna till online-databasen
'''
#db = yaml.load(open("..\..\db.yaml"))
db = yaml.load(open("../../db.yaml"))
app.config['MYSQL_HOST'] = db["mysql_host"]
app.config['MYSQL_USER'] = db["mysql_user"]
app.config['MYSQL_PASSWORD'] = db["mysql_password"]
app.config['MYSQL_DB'] = db["mysql_db"]
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


'''
Konfigurationen nedan används när applikationen skriver och läser
till en MySQL-databasserver som finns installerad på datorn
'''
'''
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'cudb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
'''


mysql = MySQL(app)


def is_logged_in(f):
    '''Används för att göra vissa sidor synliga för endast inloggade användare'''
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("För att ta del av den här sidan måste du logga in", "primary")
            return redirect(url_for("login"))
    return wrap


@app.route("/")
def index():
    return render_template("index.html", author="Christopher")

# @app.route("/edit/")
# def edit_article():
#     return render_template("edit.html", author="Martin")

@app.route("/edit/", methods=['GET', 'POST'])
@is_logged_in
def add_article():
    form = ArticleForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        body = form.body.data

        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO articles(title, body, author) VALUES(%s, %s, %s)",(title, body, session['username']))

        mysql.connection.commit()

        cur.close()

        flash('Artikeln har sparats!', 'success')

        return redirect(url_for('article_list'))

    return render_template('edit.html', form=form, author="Martin/Josef")


@app.route("/update/", methods=["POST"])
def update():
    '''Skapar variabler för rubrik och innehåll och skriver in som textfil på rätt plats. Omdirigerar därefter användaren tillbaka till Lexikon-sidan.'''
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
    article_path = "static/cleaning_articles/" + str(headline) + ".txt"

    with open(article_path, "r") as my_file:
        content = my_file.read()

    return render_template("article.html", headline=headline, content=content, author="Martin")



'''
@app.route("/static/cleaning_articles/<headline>")
def article(headline):
    titel = headline
    return render_template("article.html", content = get_title_content(titel), headlines = get_headlines(), author="Martin")
'''


@app.route("/register/", methods=["GET", "POST"])
def register():
    '''Funktion för registrering. Validerar formulär och skriver till databas.'''
    form = Register(request.form)
    if request.method == "POST" and form.validate():
        try:
            username = form.username.data.strip().lower().title()
            email = form.email.data
            password = sha256_crypt.encrypt(str(form.password.data))

            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO user_password(username, email, password) VALUES(%s, %s, %s)", (username, email, password))
            mysql.connection.commit()
            cur.close()

            flash('Du är nu registrerad och kan logga in', 'success')
            return redirect(url_for("login"))
        except:
            flash('Det finns redan ett konto registrerat på denna e-post', 'danger')
            return redirect (url_for("register"))
    else:
        return render_template("register.html", form=form, title="Registrera", author="Martin/Christopher")


@app.route("/login/", methods=["GET", "POST"])
def login():
    '''Funktion för inloggning. Kontrollerar med data i databas.'''
    form = Login(request.form)
    if request.method == "POST":

        email = request.form["email"]
        password_candidate = request.form["password"]

        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM user_password WHERE email = %s", [email])

        if result > 0:
            data = cur.fetchone()
            password = data["password"]
            username = data["username"]

            if sha256_crypt.verify(password_candidate, password):
                session["logged_in"] = True
                session["username"] = email
                flash("Välkommen " + username + "!", "success")
                return redirect(url_for("index"))
            else:
                flash("Ogiltigt lösenord", "danger")
                return render_template("login.html", form=form)
            cur.close()
        else:
            flash("Ingen användare med denna epost hittades", "danger")
            return render_template("login.html", form=form)
    else:
        return render_template("login.html", form=form, title="Logga in", author="Martin/Anders/Christopher")


@app.route("/logout/")
@is_logged_in
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
