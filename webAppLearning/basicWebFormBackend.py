from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return "<p>Index</p>"

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        return redirect(url_for("user",usr=user))
    else:
        return render_template("htmlBasicForm.html")

@app.route("/login/<usr>")
def user(usr):
    display=loginLogic(usr)
    return display

def loginLogic(user):
    if user=="Jeremy Horwich":
        return "<h1>Welcome, Jeremy</h1>"
    return f"<h1>{user}</h1>"