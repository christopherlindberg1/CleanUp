from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", title="Start", author="Christopher")


@app.route("/to_do_list.html/")
def to_do_list():
    return render_template("to_do_list.html", title="To Do", author="Christopher")


@app.route("/calendar.html/")
def calendar():
    return render_template("calendar.html", title="Kalender")


@app.route("/cleaning_tips.html/")
def cleaning_tips():
    return render_template("cleaning_tips.html", title="Städtips")


@app.route("/login.html/")
def login():
    return render_template("login.html", title="Logga in")


@app.route("/my_account.html/")
def account():
    return render_template("my_account.html", title="Mitt konto")


@app.route("/my_home.html/")
def my_home():
    return render_template("my_home.html", title="Min bostad")


@app.route("/static/<path:path>")
def serve_static_files(path):
    return send_from_directory("static", path)




if __name__ == "__main__":
    app.run(debug=True)