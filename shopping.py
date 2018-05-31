from flask import Flask, request, render_template, redirect
import os
import json

app = Flask(__name__)

# @app.route("/")
# def get_index():
#     loaded_lists=load_file()
    
#     return render_template("shopping.html",shopping_front=loaded_lists)


# @app.route("/shopshop", methods=["POST"])
# def menu_list():
    
#     shoe_type= request.form.get("shoe_type")
#     shoe_price= request.form.get("price")
#     shoe_colour= request.form.get("colour")
#     shoe_size= request.form.get("size")
#     shoe_brand= request.form.get("brand")
   
#     shopping_item={
#         "shoe": shoe_type,
#         "colour": shoe_colour,
#         "size": shoe_size,
#         "brand": shoe_brand,
#         "price": shoe_price
#     }
    
#     shopping_list=load_file() 
#     shopping_list.append(shopping_item)
#     save_file(shopping_list)
#     return redirect("/")

# def save_file(shopping_list):
#     with open("shopping_list.txt", "w") as outfile:
#         json.dump(shopping_list, outfile)
        
# def load_file():
#     if os.path.isfile("shopping_list.txt"):
#         with open("shopping_list.txt") as json_file:
#             return json.load(json_file)
#     else:
#         return []
 
# # @app.route("/menu_list")  
# # def menu_item():
# #     menu_item = menu_list.get_menu()
# #     for item in menu_list:
# #         menu_list["add_to_cart"].append(id)
# #     else:
# #         session["add_to_cart"]=[id]
# #     if ["add_to_cart"] not in menu_list:
# #         menu_list["add_to_cart"]=[]
# #         menu_list["add_to_cart"],append(id)
# #         show("1 item added to cart")
# #         return redirect ("/add_to_cart")

# # @app.route("/checkout")
# # def checkout():
# #     return



# if __name__ == '__main__':
#     app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)),debug=True)
     
