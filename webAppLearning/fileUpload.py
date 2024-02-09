import os
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
        return render_template("uploadFileForm.html")
    if request.method == "POST":
        if "upload" not in request.files:
            return redirect("htmlBasicForm.html")
        file = request.files["upload"]
        if file.filename == "":
            return redirect("/fileuploaderror")
        else:
            return file.read()
        
@app.route("/fileuploaderror")
def displayUploadError():
    return "<p>File Error</p>"

