from flask import Flask, redirect, url_for, render_template, request
from createFigure import createFigure
import dataAnalysis as da
import os

app = Flask(__name__)
UPLOAD_FOLDER = "tmp"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

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
            return redirect(url_for("showFileVisualization", filename=upload.filename, errorReceived=False))
                
@app.route("/fileUploadError")
def displayUploadError():
    return "<p>File Error</p>"

@app.route("/fileUploadSuccess/", methods=["GET","POST"])
def showFileVisualization():
    if request.method == "GET":
        query = request.args.to_dict()
        filename=query["filename"]
        errorReceived=query["errorReceived"]

        data = da.parseData(UPLOAD_FOLDER + "/" + filename)
        figure = createFigure(data)
        if errorReceived == "True":         #Must check against string since we are getting errorReceived as a query parameter
            return render_template("scatterPlotWithError.html", image=figure)
        return render_template("scatterPlotDisplay.html", image=figure)

    if request.method == "POST":
        query = request.args.to_dict()
        filename=query["filename"]
        
        learningRate = request.form.get("learningRate",type=float)
        iterations = request.form.get("iterations",type=int)

        if (learningRate is None) or (iterations is None):
            return redirect(url_for("showFileVisualization", filename=filename, errorReceived=True))
        if (learningRate < 0.00001) or (learningRate > 0.0001):
            return redirect(url_for("showFileVisualization", filename=filename, errorReceived=True))
        if (iterations < 50) or (iterations > 500):
            return redirect(url_for("showFileVisualization", filename=filename, errorReceived=True))
        
        return redirect(url_for("performLinearRegression",filename=filename,learningRate=learningRate,iterations=iterations))
    
@app.route("/fileUploadSuccess/linearRegression/", methods=["GET","POST"])
def performLinearRegression():
    if request.method == "GET":
        query=request.args.to_dict()
        filename=query["filename"]
        learningRate = float(query["learningRate"])
        iterations = int(query["iterations"])

        data = da.parseData(UPLOAD_FOLDER + "/" + filename)     #TODO: Pass parsed data through? Doing this twice feels silly
        theta, cost = da.trainModel(data,learningRate,iterations)
        figure = createFigure(data,theta)                       #TODO: Doing this a second time feels silly, too
        #Clean up the tmp folder
        if os.path.exists(UPLOAD_FOLDER + "/" + filename):
            os.remove(UPLOAD_FOLDER + "/" + filename)
        return render_template("completedRegressionDisplay.html", image=figure, cost=cost)
    if request.method == "POST":
        return redirect("/")