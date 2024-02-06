from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        return redirect(url_for("user",usr=user))
    else:
        return render_template("htmlBasicForm.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"