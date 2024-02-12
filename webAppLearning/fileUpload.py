from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
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
            return request.files["upload"].read()
        
@app.route("/fileUploadError")
def displayUploadError():
    return "<p>File Error</p>"

