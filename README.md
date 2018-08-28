# Shopping List App - Data Centric Development

This site is a shopping list application which is designed to help users to keep track of their shopping list as well as manage their shopping list.

The idea behind this choice of application is based on my personal experiences. I have always struggled to do my shopping properly and sticking to the things that I needed, sometimes forgetfulness and random purchases took control as a result I ended up spending more money and time than I had intended to. Going shopping can be really challenging when you have forgotten your list, by the time you get home only then you realize you forgot to pick up one or two things, therefore if one has a shopping list app, not only can they eliminate unnecessary return trips, they can also save money by eliminating random purchases.

Click on this [link](https://www.shoutem.com/builder/design/smartphone?nid=207360545&signup=true#/homepage/) to access a live version of this site.

# UX

Once the user is logged in, the shopping list application allows the user to create a title category for their shopping, they would then be redirected to list page where they would be prompted to add or create a title. They can then create a title for example; say fruits, and within this category they would be prompted to add items of their choice. The user can add as many items as they wish and the quantity. Only the categories or main titles would be on view until the user clicks on a particular title to access what’s in it. I have made it in such a way that the user could have their shopping list separated by categories which means each group of similar items can be added to a different category. Creating a shopping list within specific categories would ensure that the user can save time later when they want to access their lists, rather than having to go through a list of 50 items in order to edit 1 item, only the category within which the item is saved can be checked while ignoring other categories. It also means that the user can choose what category needs most attention.

The user can add a list whenever they think of an item and can even prioritize their list. The ability to do this helps the user to space out their purchases while ensuring that nothing is ever forgotten. Although one would question why shopping list app  over a paper list – a method which was heavily relied upon long before the technology era, the problem with the paper list is that it gets easily misplaced or forgotten, forgetting to bring the paper list to the store far defeats the purpose of making it in the first place. This scenario is all too common. Unlike paper, people always have their phones with them.

# Features

In order to use this site, users must first register and if they are already registered they may go ahead and log in. There is a confirmation message that pops ut to let the user that their profile had been created successfully.

1.Add list title – user creates a title for the list to be stored

2.Add item – this is where the user is prompted to create a shopping list of actual items

3.Mark item as priority – all items marked as priority are saved on a separate page and under priority items

4.Delete item – this feature deletes every other thing the user want to have deleted

5.Success messages - Each time the user add a title, delete item or update their list, there is a pop up message that follows to let them know that their action was a success.

See a brief overview of how the site looks in different screens

* Below is an overview of how the site looks on different screen sizes.

<!--![alt text](https://github.com/DollyGt/my_shopping_list_app/blob/master/static/image/bags.jpg)-->

<!--![alt text](https://github.com/DollyGt/my_shopping_list_app/blob/master/static/image/bags.jpg)-->


# Features Left to Implement

I would like to add a built-in recipe books where users would be able to add recipes and have each item needed for a meal gets automatically added to their shopping list. This feature would allow users to create a collection of their favourite recipes. Once a recipe gets selected, all the ingredients for that particular recipe would be added to the  shopping list automatically.

I would also like to add a delayed list feature – this feature would allow the user to add from their list the items that are needed only very late in a month or so, this is followed by a reminder nearing the date in which the initial purchase is intended.

# Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

The technologies used for this website are as follows:

* HTML5

* CSS3

* Bootstrap

* JavaScript/ jQuery

* Flask Microframework (Python)

* MongoDB (NoSQL Database)

# Testing

The website is user friendly, recognises  desktop browsers and it is also mobile compatible. Using webview/ chrome view and safari same website can be used as an Android App with zero changes. 

All forms were tested

Users would have to either log in or register otherwise the form will pass in error

If a user is not registered and they try to log in , the error message will return to let them know that there is no user of that particular name

An empty form will return a field required message if the user fails to type in their list title

* Below is an overview of how the site looks with different screen sizes.

# Deployment

GitHub pages are used for hosting while the master branch is deployed to Heroku. Please click here to see a live demo on Heroku.

For deployment, you would have to:

1.Fist create a workspace in visual studio {% codeblock title lang:language URL link_text %}

{% endcodeblock %}

2.Link the work space to Github repository

pip install the following:

** sudo pip3 freeze --local >requirements.txt
** sudo pip3 install gunicorn

gunicorn should now be in the requirements.txt

3.Go to heroku and link the Github repository by deploying it manually. Once this step is done, each time you push to Github the Github master branch would be automatically update


# To install and have it running

To clone this repository follow the following command:

* git clone followed by this repository [link](https://github.com/DollyGt/my_shopping_list_app).


# Media

The photos used in this site were obtained from pexels website. Click on this [link](https://www.pexels.com/) to access thier website.

# Acknowledgements

I received inspiration for this project from X
