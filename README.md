**Important message!**

*Due to having my app crushing on heroku, i had to figure out why it was not working. I ended up tracing my code from when the app was last working on heroku, as a result, i copied all my code to a different working environment to work from there as an attempt to find out where the problem was. I then pasted all the code from since when the app was working to the original work space from which i had deleted the code that was failing in heroku and this did work. I figured out that once i changed my MongoDB details in MLab i never updated my config vars details. After that, i went back to the code that i had deletd and i pasted it back. These changes affected my commits update and timeline. Please refer to my commits to see history of all original commits of this repository from the very beginning.*

# Shopping List App - Data Centric Development

This site is a shopping list application which is designed to help users to keep track of their shopping list as well as manage their shopping list.

The idea behind this choice of application is based on my personal experiences. I have always struggled to do my shopping properly and sticking to the things that I needed, sometimes forgetfulness and random purchases took control as a result I ended up spending more money and time than I had intended to. Going shopping can be really challenging when you have forgotten your list, by the time you get home only then you realize you forgot to pick up one or two things, therefore if one has a shopping list app, not only can they eliminate unnecessary return trips, they can also save money by eliminating random purchases. Users would be able to save all their list with a user friendly app.

Click on this [link](https://dollys-shopping-list.herokuapp.com/) to access a live version of this site.

# UX

Once the user is logged in, the shopping list application allows the user to create a title category for their shopping, they would then be redirected to list page where they would be prompted to add or create a title. They can then create a title for example; say fruits, and within this category they would be prompted to add items of their choice. The user can add as many items as they wish and the quantity. Only the categories or main titles would be on view until the user clicks on a particular title to access what’s in it. I have made it in such a way that the user could have their shopping list separated by categories which means each group of similar items can be added to a different category. Creating a shopping list within specific categories would ensure that the user can save time later when they want to access their lists, rather than having to go through a list of 50 items in order to edit 1 item, only the category within which the item is saved can be checked while ignoring other categories. It also means that the user can choose what category needs most attention.

The user can add a list whenever they think of an item and can even prioritize their list. The ability to do this helps the user to space out their purchases while ensuring that nothing is ever forgotten. Although one would question why shopping list app  over a paper list – a method which was heavily relied upon long before the technology era, the problem with the paper list is that it gets easily misplaced or forgotten, forgetting to bring the paper list to the store far defeats the purpose of making it in the first place. This scenario is all too common. Unlike paper, people always have their phones with them.

# Features

In order to use this site, users must first register and if they are already registered they may go ahead and log in. There is a confirmation message that pops up to let the user know that their profile had been created successfully.

1.Add list title – user creates a title for the list to be stored

2.Add item – this is where the user is prompted to create a shopping list of actual items

3.Mark item as priority – all items marked as priority are saved on a separate page and under priority items

4.Delete item – this feature deletes every other thing the user want to have deleted

5.Success messages - Each time the user add a title, delete item or update their list, there is a pop up message that follows to let them know that their action was a success.


* Screenshots.

![alt text](https://github.com/DollyGt/my_shopping_list_app/blob/master/static/image/screenshot1.png)

![alt text](https://github.com/DollyGt/my_shopping_list_app/blob/master/static/image/screenshot2.png)


# Features Left to Implement

I would like to add a built-in recipe books where users would be able to add recipes and have each item needed for a meal gets automatically added to their shopping list. This feature would allow users to create a collection of their favourite recipes. Once a recipe gets selected, all the ingredients for that particular recipe would be added to the  shopping list automatically.

I would also like to add a delayed list feature – this feature would allow the user to add from their list the items that are needed only very late in a month or so, this would be followed by a reminder nearing the date in which the initial purchase is intended.

# Technologies Used

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

Users would have to either log in or register otherwise the form will pass in error if they attempt logging in without first registering. Once a user is registered, to log they would be required to enter their registed login details. If the user enters different login details, there would be alerted that the login details are wrong therefore the form would never submit. I tested to see that the forms all work as intended and this was a success.

If a user is not registered and they try to log in , the error message will return to let them know that there is no user of that particular name

An empty form will return a field required message if the user fails to type in their list title. No form can submit if the user have not created a list title for their shopping list.

# Deployment

GitHub pages are used for hosting while the master branch is deployed to Heroku. 

For deployment, you would have to:

`First create a workspace in visual studio`

`Link the work space to Github repository`

`pip install the following:`

`$ sudo pip3 freeze --local >requirements.txt`

`$ sudo pip3 install gunicorn`

`gunicorn should now be in the requirements.txt`

`Go to heroku and link the Github repository by deploying it manually. Once this step is done, each time you push to Github the Github master branch would automatically update.`


# To install and have it running

Go to this repository lin below:

* git clone followed by this repository [link](https://github.com/DollyGt/my_shopping_list_app).

Once there, git clone the repository and then from your terminal run the following command:

`$ sudo pip3 -r install requirements.txt`

# Media

The photos used in this site were obtained from pexels website. Click on this [link](https://www.pexels.com/) to access thier website.


