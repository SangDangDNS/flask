from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "sangdangdns"
@app.route("/login", methods=["POST","GET"])
def hello_world():
    if request.method == "POST":
        user_name = request.form["name"]
        if user_name:
            session["user"] = user_name
            return redirect(url_for("hello_user", name = user_name))
    return render_template("login.html")

@app.route("/admin")
def hello_admin():
    return f"Hello bạn admin !!!"

@app.route("/user")
def hello_user(name):
    if "user" in session:
        name = session["user"]
    else:
        return redirect(url_for("login"))
    if name == 'Sang':
        return redirect(url_for("hello_admin"))
    return f"Hello bạn {name} !!!"




@app.route("/blog/<int:blog_id>")
def blog(blog_id):
    return f"Blog {blog_id} !!!"

if __name__ =="__main__":
    app.run(debug=True)