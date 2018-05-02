from flask import Flask, render_template
from flask_mysqldb import MySQL
import calendar
'''import account_collection'''
from os import listdir

app = Flask(__name__)


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
    return render_template("calendar.html", calendar.calendar(2018), title="Kalender", author="Martin")


@app.route("/cleaning_tips.html/")
def cleaning_tips():
    return render_template("cleaning_tips.html", title="Städtips")


@app.route("/cleaning_tips/<room>.html")
def rooms(room):
    rooms = listdir("static/cleaning_articles")


    return render_template("room.html", rooms=rooms)


@app.route("/register.html/")
def register():
    return render_template("register.html", title="Registrera", author="Martin")


@app.route("/login.html/")
def login():
    return render_template("login.html", title="Logga in", author="Martin")


@app.route("/my_account.html/")
def account():
    return render_template("my_account.html", title="Mitt konto")


@app.route("/my_home.html/")
def my_home():
    return render_template("my_home.html", title="Min bostad", author="Christopher")


@app.route("/static/<path:path>")
def serve_static_files(path):
    return send_from_directory("static", path)



if __name__ == "__main__":
    app.run(debug=True)
