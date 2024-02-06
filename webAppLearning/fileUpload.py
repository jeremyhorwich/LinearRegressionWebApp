import os
from flask import Flask, redirect, url_for, render_template, request, flash
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "/tmp"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
@app.route("/index")
def index():
    return "<p>Index</p>"

@app.route("/upload", methods=["GET","POST"])
def uploadFile():
    if request.method == "GET":
        return render_template("uploadFileForm.html")