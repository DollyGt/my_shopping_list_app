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
    user_lists = load_list_names_from_mongo(username)
    return render_template("user_home.html", username=username, user_lists=user_lists)

 
@app.route("/<username>/create_new_list", methods=["POST"]) 
def add_list_name(username):
    list_name= request.form['list_name']
    save_list_names_to_mongo(username,list_name)
    return redirect(username)
    
@app.route("/<username>/<list_name>", methods=["GET","POST"]) 
def view_specific_list_by_user(username, list_name):
    list_items = load_list_items_from_mongo(username, list_name)
    return render_template("user_lists.html", username=username, list_name=list_name, list_items=list_items)
    
@app.route("/<username>/<list_name>/add_item", methods=["POST"]) 
def add_item_to_list(username, list_name):
    list_item= request.form['list_item']
    save_list_items_to_mongo(username, list_name, list_item)
    return redirect(username + "/" + list_name)
    
def save_list_names_to_mongo(username, list_name):
    with MongoClient(MONGODB_URI) as conn:
        db = conn[MONGODB_NAME]
        collection = db[username]
        collection.insert({'name': list_name, 'list_items': [] })
        
def load_list_names_from_mongo(username):
    with MongoClient(MONGODB_URI) as conn:
        db = conn[MONGODB_NAME]
        collection = db[username]
        users = db.collection_names()
        if username in users:
            user_lists = collection.find()
            return user_lists
        
def save_list_items_to_mongo(username, list_name, new_list_item):
    with MongoClient(MONGODB_URI) as conn:
        db = conn[MONGODB_NAME]
        collection = db[username]
        selected_list = collection.find({'name':list_name})
        new_list_of_items = []
        for i in selected_list:
            if i["list_items"]:
                for item in i["list_items"]:
                    new_list_of_items.append(item)
            
        new_list_of_items.append(new_list_item)
        collection.find_one_and_update({"name": list_name}, {"$set": {"list_items": new_list_of_items}})

def load_list_items_from_mongo(username, list_name):
    with MongoClient(MONGODB_URI) as conn:
        db = conn[MONGODB_NAME]
        collection = db[username]
        users = db.collection_names()
        if username in users:
            list_items = collection.find({'name':list_name})
            return list_items
        




if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)