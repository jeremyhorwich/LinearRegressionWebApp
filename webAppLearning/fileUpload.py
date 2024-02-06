from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return "<p>Index</p>"