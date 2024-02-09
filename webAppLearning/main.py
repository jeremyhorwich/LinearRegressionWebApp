from flask import Flask, redirect, render_template, request
from createFigure import createFigure

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return redirect("/showImage")      #Just makes life a little easier
    #return "<p>Index</p>"

@app.route("/showImage")
def showImage():
    figure = createFigure()
    return render_template("imgDisplay.html", image=figure)