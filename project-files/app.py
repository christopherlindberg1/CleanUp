from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from os import listdir


app = Flask(__name__)

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
    '''accounts = account_collection.get_accounts()'''
    '''accounts=accounts # Tog bort denna då den ställde till med problem i fliken i webbläsaren '''
    return render_template("index.html", title="Start", author="Christopher")


@app.route("/to_do_list.html/")
def to_do_list():
    return render_template("to_do_list.html", title="To Do", author="Christopher")


@app.route("/calendar.html/")
def calendar():
    return render_template("calendar.html", title="Kalender", author="Martin")


@app.route("/cleaning_tips.html/")
def cleaning_tips():
    return render_template("cleaning_tips.html", title="Städtips")


@app.route("/register.html/", methods=["GET", "POST"])
def register():
    form = Registrera(request.form)
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

        redirect(url_for('index'))

        return render_template("register.html", form = form)

    return render_template("register.html", form=form, title="Registrera", author="Martin")


@app.route("/login.html/", methods=["GET", "POST"])
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
                app.logger.info("PASSWORD MATCHED")
        
        else:
            app.logger.info("NO USER")
    return render_template("login.html") #, title="Logga in", author="Martin/Anders"

@app.route("/my_account.html/")
def account():
    return render_template("my_account.html", title="Mitt konto")


@app.route("/my_home.html/")
def my_home():
    return render_template("my_home.html", title="Min bostad", author="Christopher")


@app.route("/static/<path:path>")
def serve_static_files(path):
    return send_from_directory("static", path)


class Registrera(Form):
    email = StringField("E-post", [validators.Length(min=5, max=50)])
    password = PasswordField("Lösenord", [validators.DataRequired(), validators.EqualTo("confirm", message="Fel lösenord")])
    confirm = PasswordField("Bekräfta lösenord")


if __name__ == "__main__":
    app.secret_key='secret123'
    app.run(debug=True)
