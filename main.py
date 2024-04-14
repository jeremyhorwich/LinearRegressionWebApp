from flask import Flask, redirect, url_for, render_template, request
from figure import create_figure
import analysis as da
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
        file_path = os.path.join(UPLOAD_FOLDER, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
    return redirect("/upload")


@app.route("/upload", methods=["GET","POST"])
def upload_file():
    if request.method == "GET":
        return render_template("uploadFile.html")
    if request.method == "POST":
        upload_not_found = "upload" not in request.files
        upload_name_blank = request.files["upload"].filename == ""
        if upload_not_found or upload_name_blank:
            return redirect("/fileUploadError")
        else:
            upload = request.files["upload"]
            #Saving to tmp - files may be too big for session variables
            dest = os.path.join(app.config["UPLOAD_FOLDER"], upload.filename)
            upload.save(dest)
            return redirect(url_for("show_file_visualization", 
                                    filename=upload.filename, 
                                    error_received=False))
                
                
@app.route("/fileUploadError")
def display_upload_error():
    return "<p>File Error</p>"


@app.route("/fileUploadSuccess/", methods=["GET","POST"])
def show_file_visualization():
    if request.method == "GET":
        query = request.args.to_dict()
        filename = query["filename"]
        error_received = query["error_received"]

        data = da.parse_data(UPLOAD_FOLDER + "/" + filename)
        figure = create_figure(data)

        #error_received is a query parameter, so we check against string
        if error_received == "True":
            return render_template("scatterPlotWithError.html", image=figure)
        return render_template("scatterPlotDisplay.html", image=figure)

    if request.method == "POST":
        query = request.args.to_dict()
        filename = query["filename"]
        
        learning_rate = request.form.get("learningRate",type=float)
        iterations = request.form.get("iterations",type=int)

        if (learning_rate is None) or (iterations is None):
            return redirect(url_for("show_file_visulaization", 
                                    filename=filename, 
                                    error_received=True))
        
        if (learning_rate < 0.00001) or (learning_rate > 0.0001):
            return redirect(url_for("show_file_visualization", 
                                    filename=filename, 
                                    error_received=True))
        
        if (iterations < 50) or (iterations > 500):
            return redirect(url_for("show_file_visualization", 
                                    filename=filename, 
                                    errorReceived=True))
        
        return redirect(url_for("perform_linear_regression",
                                filename=filename,
                                learning_rate=learning_rate,
                                iterations=iterations))
    

@app.route("/fileUploadSuccess/linearRegression/", methods=["GET","POST"])
def perform_linear_regression():
    if request.method == "GET":
        query = request.args.to_dict()
        filename = query["filename"]
        learning_rate = float(query["learning_rate"])
        iterations = int(query["iterations"])

        data = da.parse_data(UPLOAD_FOLDER + "/" + filename)            #TODO: Pass parsed data through? Doing this twice feels silly
        theta, cost = da.train_model(data,learning_rate,iterations)
        figure = create_figure(data,theta)                              #TODO: Doing this a second time feels silly, too
        
        #Clean up the tmp folder
        if os.path.exists(UPLOAD_FOLDER + "/" + filename):
            os.remove(UPLOAD_FOLDER + "/" + filename)
        return render_template("completedRegressionDisplay.html", 
                               image=figure, 
                               cost=cost)
    
    if request.method == "POST":
        return redirect("/")