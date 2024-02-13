from flask import Flask, redirect, url_for, render_template, request
from createFigure import createFigure
import dataAnalysis as da
import os

app = Flask(__name__)
UPLOAD_FOLDER = "tmp"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

learningRate, iterations = 0.00005,100

@app.route("/")
@app.route("/index")
def index():
    #Clean up the tmp folder from last time
    files = os.listdir(UPLOAD_FOLDER)
    for file in files:
        filePath = os.path.join(UPLOAD_FOLDER, file)
        if os.path.isfile(filePath):
            os.remove(filePath)
    return redirect("/upload")      #Just makes life a little easier
    #return "<p>Index</p>"

@app.route("/upload", methods=["GET","POST"])
def uploadFile():
    if request.method == "GET":
        return render_template("uploadFile.html")
    if request.method == "POST":
        if ("upload" not in request.files) or (request.files["upload"].filename == ""):
            return redirect("/fileUploadError")
        else:
            upload = request.files["upload"]
            #Saving to tmp folder because files may be too big for session variables
            upload.save(os.path.join(app.config["UPLOAD_FOLDER"], upload.filename))
            return redirect(url_for("showFileVisualization", filename=upload.filename))
                
@app.route("/fileUploadError")
def displayUploadError():
    return "<p>File Error</p>"

@app.route("/fileUploadSuccess/<filename>", methods=["GET","POST"])
def showFileVisualization(filename):
    if request.method == "GET":
        data = da.parseData(UPLOAD_FOLDER + "/" + filename)
        figure = createFigure(data)
        return render_template("imgDisplay.html", image=figure)
    if request.method == "POST":
        #return "<p>Don't give me an error please</p>"
        return redirect(url_for("performLinearRegression",filename=filename))
    
@app.route("/fileUploadSuccess/linearRegression/<filename>")
def performLinearRegression(filename):
    data = da.parseData(UPLOAD_FOLDER + "/" + filename)     #TODO: Pass parsed data through? Doing this twice feels silly
    theta = da.trainModel(data,learningRate,iterations)     #TODO: User selection for learningRate and iterations
    figure = createFigure(data,theta)                       #TODO: Doing this a second time feels silly, too
    if os.path.exists(UPLOAD_FOLDER + "/" + filename):
        os.remove(UPLOAD_FOLDER + "/" + filename)
    return render_template("imgDisplay.html", image=figure)     #TODO: Spit out image regarding confidence


    #Show the line of best fit
    #Spit out information regarding confidence