from flask import Flask, redirect, render_template, request
from createFigure import createFigure
import dataAnalysis as da

app = Flask(__name__)

learningRate, iterations = 0.00005,100

@app.route("/")
@app.route("/index")
def index():
    return redirect("/showImage")      #Just makes life a little easier
    #return "<p>Index</p>"

@app.route("/showImage")
def showImage():
    figure = createFigure()
    return render_template("imgDisplay.html", image=figure)

@app.route("/upload", methods=["GET","POST"])
def uploadFile():
    if request.method == "GET":
        return render_template("uploadFile.html")
    if request.method == "POST":
        #Here I made the choice not to save the file to memory because it streamlines the code logic
        #Not sure if this is correct or if I should be saving the file to a local variable (ie file = request.files["upload"])
        if ("upload" not in request.files) or (request.files["upload"].filename == ""):
            return redirect("/fileUploadError")
        else:
            return redirect("/fileUploadSuccess")
        
@app.route("/fileUploadError")
def displayUploadError():
    return "<p>File Error</p>"

@app.route("/fileUploadSuccess")
def analyzeFile():
    data = da.parseData((request.files["upload"]))
    #Show the initial scatter plot
    theta = da.trainModel(data,learningRate,iterations)             #TODO: User selection for learningRate and iterations
    #Show the line of best fit
    #Spit out information regarding confidence
    return "<p>In progress</p>"