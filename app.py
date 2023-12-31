from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from os import path

app = Flask(__name__)
app.config["SECRET_KEY"] = "sangdangdns"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =False
app.permanent_session_lifetime = timedelta(minutes=1)

db = SQLAlchemy(app)

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self,name,email):
        self.name = name
        self.email = email


@app.route("/login", methods=["POST","GET"])
def hello_world():
    if request.method == "POST":
        user_name = request.form["name"]
        # session.permanent = True
        if user_name:
            session["user"] = user_name
            return redirect(url_for("hello_user", name = user_name))
    if "user" in session:
        name = session["user"]
        return f"<h1>Hello {name}</h1>"

    return render_template("login.html")

@app.route("/admin")
def hello_admin():
    return f"Hello bạn admin !!!"

@app.route("/user")
def hello_user():
    if "user" in session:
        name = session["user"]
    else:
        return redirect(url_for("hello_world"))
    if name == 'Sang':
        return redirect(url_for("hello_admin"))
    return f"Hello bạn {name} !!!"

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("hello_world"))


@app.route("/blog/<int:blog_id>")
def blog(blog_id):
    return f"Blog {blog_id} !!!"

if __name__ == "__main__":
    if not path.exists("user.db"):
        with app.app_context():
            db.create_all()
            print("Created DB")
    app.run(debug=True)