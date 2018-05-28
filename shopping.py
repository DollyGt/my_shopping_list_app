from flask import Flask, request, render_template, redirect
import os

app = Flask(__name__)

@app.route("/")
def get_shoppinghello():
    return render_template("shopping.html")

    