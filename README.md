# **Task Tracker** - By Cameron Maxwell
#### Video Demo: https://www.youtube.com/watch?v=dENf1VW_dk4
#### Description:
        For my final project, I decided to create a Task Tracker, a website where you can add tasks to your list whether it be things you need to get done, ideas you want to note down to re-visit later, or events you need to write down to remember. Task Tracker allows you to create an account so only you see your list, adds a date to each task so you know when you created that task, and allows you to delete a single task or all tasks if need be.

        The reason I created Task Tracker, was because I would randomly think of ideas or have things I need or want to remember so I wanted a place that looked nice and is easy to use to keep track of anything and everything.

#### Models.py:
        In the models.py file, I used Djangos AbstractUser to create the user model so you can create an account to store each users list privately.

        The List class in models.py is the core model where it structures each list item. Each item is built with user to keep track of who the item belongs to, list_content which contains the actual content of the item, and the date_created which contains the data the item was created.  
        
#### Admin.py:
        In the admin.py file, I registered the User model and List model.

#### Urls.py:
        In the urls.py file, I created all the paths needed for the URLs and functions. Index path to load the home page, register path to load the register account page, login path to load the login page, logout path which logs out user but just loads back the home page, create_list path to add tasks to the database, my_list path to load the users list page, delete_list path to delete a list with given list id from the database and loads to the users list page, delete_all path that deletes all the users tasks from the database and loads the users list page, edit_task path to edit the task the user selects.

#### Views.py:
        In the views.py file, I created the function to render the index.html page,
        function for registering, logging in, and logging out, as well as the create_list function for the user to create a task and for it to save to the database, my_list function to retrieve all the current user's tasks and render their list page so they only see their tasks, delete_list function to retrieve the id of the task the user would like to delete and delete that specific task, delete_all function that retrieves all the current users tasks and deletes them all, edit_task fucntion is used to retrieve the id of the task the user selects and edit the content and save it to the database.

## Templates folder:
#### Base.html:
        In the base.html file, I created the layout for my website i.e. the header, and the footer for all HTML pages and linked bootstrap as well as my style sheet and javascript.

#### Index.html:
        In the index.html file, I created the home page for Task Tracker, where you can path to registering an account, logging in, and adding tasks to your list.

#### Login.html:
        In the login.html file, I created the login page for a user to log in with an account they already created.

#### Register.html:
        In the register.html file, I created the register page for a user to create an account for Task Tracker, or they can be redirected to the login page if they already have an account.

#### My_list.html:
        In the my_list.html file, I created the my_list page where the user can go to see their tasks they have created, add new tasks, or delete tasks they have finished or no longer need.

## Static folder:
#### css/styles.css:
        In the styles.css file, I created all my css that I wanted to add to my webpage.

#### img folder:
        In the img folder, I have the svg for the websites logo, and the png for the main image on the index page.

#### js/script.js:
        In the script.js file, I created addTask to alter the HTML when the add button on my_list page is pressed adding a textarea and submit button for the user to create the task, deleteTask to alert the user when they have deleted a single task, and deleteAllPrompt is used to alert the user when they press delete all button and ask to confirm if they user confirms deleteAllPrompt then triggers deleteAll which is used to alert the user they have deleted all tasks, editTask is used to edit a specific task.