from __future__ import print_function
import sys
import os
from flask import Flask, request, render_template, redirect, flash, session, abort
from pymongo import MongoClient
from bson.objectid import ObjectId
import logging
logging.basicConfig(level=logging.DEBUG)

MONGODB_URI = os.environ.get("MONGODB_URI")
MONGODB_NAME = os.environ.get("MONGODB_NAME")

app = Flask(__name__)
app.secret_key = "secretKeyHere"

@app.route('/')
def get_index():
    if 'user_name' in session:
        user_name=session['user_name']
    else:
        user_name='nouserinsession'
    return render_template('index.html', user_name=user_name)
    
@app.route("/login", methods=['POST'])
def do_login():
    with MongoClient(MONGODB_URI) as conn:
        db = conn[MONGODB_NAME]
        user_name = request.form['user_name'].strip()
        password = request.form['password'].strip()
        mode = request.form['mode']
        user = get_user(user_name)
        eprint(user)
        if mode == 'login':
            if not user:
                msgString = 'There is no user "%s"'%(user_name)
                flash(msgString)
                return render_template('index.html')
            else:
                if not user['password'] == password:
                    msgString = 'Wrong password !!'
                    flash(msgString)
                    return render_template('index.html')
                
                else:
                    session['logged_in'] = True
                    session['user_name'] = user_name
                    msgString = 'Password is fine move forward'
                    #flash(msgString)
                    return render_template('index.html', user_name=user_name)
        
        else:
            user = db['users'].find_one({'user_name':user_name})
            if not user:
                db['users'].insert({'user_name': user_name, 'password':password, 'lists':[]})
                session['logged_in'] = True
                session['user_name'] = user_name
                return render_template('index.html',user_name=user_name)
            else:
                msgString = 'User with the same name already exist'
                flash(msgString)
                return render_template('index.html')


@app.route("/logout")
def logout():
    session['logged_in'] = False
    session['user_name'] = False
    msgString = 'Successfully logged out'
    flash(msgString)
    return render_template('index.html')
    
@app.route("/<user_name>/") 
def get_userpage(user_name):
    user = get_user(user_name)
    
    lists= []
    if not user:
        lists = []
    else:
        for list in user['lists']:
            lists.append(list)
            
    priorities = load_priority_items(lists)
    return render_template("user_home.html", user_name=user_name, lists=lists, priorities=priorities)

@app.route("/<user_name>/create_new_list", methods=["POST"]) 
def create_list(user_name):
    list_name= request.form['list_name']
    create_list_for_user(user_name,list_name)
    msgString = 'Your list "%s" is created '%(list_name)
    flash(msgString)
    return redirect(user_name)
    
@app.route("/<user_name>/<list_name>/add_item", methods=["POST"]) 
def add_item_to_list(user_name, list_name):
    user = get_user(user_name)
    priority = request.form.getlist('item_priority')
    item_name = request.form['item_name']
    quantity = int(request.form['item_quantity'])
    
    for counter, list in enumerate(user['lists']):
        if list['list_name'] == list_name:
            list_index = counter 
            break
        
    if(len(priority) > 0):
        priority = 1
    else:
        priority = 0

    list_item= {'item_name': item_name, 'item_priority': priority, 'item_quantity': quantity}
    user['lists'][list_index]['list_items'].append(list_item)
    save_user_lists(user)
    msgString = 'Item "%s", added to "%s" list !'%(item_name,list_name)
    flash(msgString)
    return redirect(user_name)
    
@app.route('/<user_name>/<list_name>/<item_name>/delete_item',methods=['POST'])
def delete_item(user_name, list_name, item_name):
    user = get_user(user_name)
    for counter, list in enumerate(user['lists']):
        if list['list_name'] == list_name:
            list_index = counter 
            break
    user['lists'][list_index]['list_items'] = removeObjFromList(user['lists'][list_index]['list_items'], item_name)
    save_user_lists(user)
    msgString = 'Item "%s", removed from "%s" list !'%(item_name, list_name)
    flash(msgString)
    return redirect(user_name)
    
    
@app.route('/<user_name>/<list_name>/delete_list',methods=['POST'])        
def delete_list(user_name, list_name):
    user = get_user(user_name)
    new_lists = []
    for counter, list in enumerate(user['lists']):
        if list['list_name'] == list_name:
            del(user['lists'][counter])
            deleted = True
            break

    if deleted:
        save_user_lists(user)
        msgString = 'Your list "%s" is deleted '%(list_name)
    else:
        msgString = 'Something went wrong'

    flash(msgString)
    return redirect(user_name)

def load_priority_items(user_lists):
    lists_with_priority = []
    for list in user_lists:
        for item in list['list_items']:
            if item['item_priority'] > 0:
                list_name = list['list_name']
                item_name = item['item_name']
                lists_with_priority.append({'list_name':list_name, 'item_name': item_name})
        
    return lists_with_priority

def get_user(user_name):
    user = {}
    client = MongoClient(MONGODB_URI)
    db = client[MONGODB_NAME]
    users = db['users']
    res = users.find({'user_name':user_name})
    for u in res:
        user = u
        
    # eprint(user)
    client.close()
    return user


def removeObjFromList(list, item_name):
    for counter, item in enumerate(list):
        if item['item_name'] == item_name:
            del(list[counter]) 
            break
        
    return list

def create_list_for_user(user_name, list_name):
    user = get_user(user_name)
    user['lists'].append({'list_name':list_name, 'list_items':[]})
    save_user_lists(user)
    return

def save_user_lists(user):
    with MongoClient(MONGODB_URI) as conn:
        db = conn[MONGODB_NAME]
        db['users'].find_one_and_update({"_id": user['_id']}, 
                                 {"$set": {"lists": user['lists']}})
    return

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

        
if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)
    