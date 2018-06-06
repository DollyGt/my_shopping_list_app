import os
from flask import Flask, request, render_template, redirect
from pymongo import MongoClient

MONGODB_URI = os.environ.get("MONGODB_URI")
MONGODB_NAME = os.environ.get("MONGODB_NAME")

app = Flask(__name__)

@app.route('/')
def get_index():
    return render_template('index.html')
    
@app.route("/login", methods=['POST'])
def do_login():
    username = request.form['username']
    return redirect(username)

@app.route("/<username>") 
def get_userpage(username):
    return render_template("lists.html", username=username)

 
@app.route("/<username>/new_list", methods=["POST"]) 
def add_message(username):
    list_name= request.form['list_name']
    return redirect(username)
    
    
def save_lists_to_mongo():
    pass
    
def load_list_names_from_mongo():
    pass



if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)