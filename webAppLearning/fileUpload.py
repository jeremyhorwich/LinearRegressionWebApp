import os
from flask import Flask, redirect, url_for, render_template, request, flash
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "/tmp"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
@app.route("/index")
def index():
    return redirect("/upload")
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
            return render_template("fileContent.html",text=file.read())
            # with open(file,"r") as f:
            #     return render_template("fileContent.html",text=f.read())
            # return redirect("/Success")
            # filename = secure_filename(file.filename)
            # file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            # return redirect(url_for("download_file", name=filename))
        
@app.route("/fileuploaderror")
def displayUploadError():
    return "<p>File Error</p>"

# @app.route("/Success")
# def displayFile():
#     if "upload" not in request.files:
#         return redirect("htmlBasicForm.html")
#     file = request.files["upload"]
#     with open(file,"r") as f:
#         return f"<p>{f.read()}</p>"
