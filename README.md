# Fitness Madness

Welcome to the readme file of my project.

## Introduction

This programme is designed 

You can find a link to my website [here]().

# Table of Contents
[1.User Experience(UX)](#1-user-experience)
- 1.1 User Goals
- 1.2 User Expectations
- 1.3 User Stories
- 1.4 Wireframe
- 1.5 Strategy Tables

[2.Features](#2-features)

[3.Technology](#3-technology)

[4.Testing](#4-testing)

[5.Bugs](#5-bugs)

[6.Deployment](#6-deployment)

[7.Project Completion](#7-project-completion)

[8.Improvements](#8-improvements)

[9.Acknowledgements](#9-acknowledgements)

# 1. User Experience

## 1.1 User Goals

[Return to the Table of Contents](#table-of-contents)


## 1.2 User Expectations

[Return to the Table of Contents](#table-of-contents)

The following are expected of the website:

* Should be easily accessible.
* The language should be in simple English.
* The user should be able to login and out easily.
* 
* 
* The user can sign up to the website if they haven't an account. 
* 
* The user should be able to access the website on different devices, not just through the computer.

## 1.3 User Stories

[Return to the Table of Contents](#table-of-contents)

Throughout the project, I used github user stories to record and keep track of my tasks. At the beginning, I listed all the things I needed to do, moved them to the second column when I am working on them and finally to the last column when I am done with that task.
![user_story_board](documents/images/user_stories.png)

## 1.4 Wireframes

[Return to the Table of Contents](#table-of-contents)

### Mobile Wireframe

This was what I had in mind when I was coming up with the skeleton of the project.
![user_story_board](documents/images/webframe-mobile.png)

### Website Wireframe

![user_story_board](documents/images/webframe-website.png)

## 1.5 Strategy Table

Opportunity/Problem/Feature| Importance| Viability/Feasibility
------------ | -------------------------|---------


# 2. Features

[Return to the Table of Contents](#table-of-contents)

## 2.1 Navigation Bar

The navigation bar is placed at the top of all pages. The navigation bar is dynamic in that meaning depending on if the user is logged in or not the options will change.
- 

On a tablet or a phone, the navbar would look like this.

![navbar_mob](documents/images/mobile-1.png)

## 2.2 Login, Signup and Logout

The login function would allow the user to signin if the user already has an account.

![login](documents/images/webpage-signin.png)

If the user doesn't have an account, then s/he can sign up for one.

![signup](documents/images/webpage-signup.png)

And when a user wants to logout of their account, they can use the logout function.

![logout](documents/images/webpage-signout.png)

If the email or password is incorrect when signing in, the following would appear.

![error_login](documents/images/failed-webpage-password.png)

## 2.3 About, Contacts and Homepage


## 2.4 

## 2.5

## 2.6

# 3. Technology

[Return to the Table of Contents](#table-of-contents)

* [MD](https://en.wikipedia.org/wiki/Markdown) (Markdown) was used to create this readme file.

* [Gitpod](https://www.gitpod.io/) was used for the code input and edit for this project.

* [Github](https://github.com/) was used to store my repository and code when it is not in use.

* [Slack](https://slack.com/intl/en-ie/) was used for communications when I was having trouble creating code.

* [Pep8 Validator](http://pep8online.com/) was used to check for bugs in my code.

* [Heroku](https://id.heroku.com/login) was used to deploy my project.

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) was used to create the website.

* [JS](https://en.wikipedia.org/wiki/JavaScript)(JavaScript) was used to make the website.

* [HTML5](https://en.wikipedia.org/wiki/HTML5) (Hypertext Markup Language 5) was used to create the webpages.

* [CSS](https://en.wikipedia.org/wiki/CSS) (Cascading Style Sheets) was used to style the webpages.

* [PostgreSQL](https://www.postgresql.org/) was used as a database.

* [Pixabay](https://pixabay.com/) was used to download images. These images were then uploaded onto Cloudinary.

* [Cloudinary](https://cloudinary.com/) was used as a database to store images.

* [Google Fonts](https://fonts.google.com/) was used to import the font style for my project.

* [W3C Markup](https://validator.w3.org/),[Jigsaw validation](https://jigsaw.w3.org/) and [JSHint](https://jshint.com/) tools were used to check for bugs in my code.

* [Auto Draw](https://www.autodraw.com/) was used to create my webframes.

# 4. Testing

[Return to the Table of Contents](#table-of-contents)

The contents of the testing section can be find [here](testing.md).

# 5. Bugs

# 6. Deployment

[Return to the Table of Contents](#table-of-contents)

The site was deployed to Heroku using the following steps:

- Install Django and the supporting libraries
    - Install Django and Gunicorn. Gunicorn is the server that is used to run Django on Heroku.
    - Install support libraries including psycopg2, this was used to connect the PostgreSQL database.
    - Install Cloudinary libraries, this is a host provider service that stores images.
    - The requirements.txt file was created to include the project's dependencies which allowed us to run the project in Heroku.

- Create a new, blank Django Project
    - Create a new project
    - Create the app
    - Add reservations to the installed apps in settings.py
    - Migrate all new changes to the database
    - Run the server to test

- Setup project to use Cloudinary and PostgreSQL
    - Create new Heroku app
        - Sign into Heroku
        - Select New
        - Select create new app
        - Enter a relevant app name
        - Select appropriate region
        - Select the create app button

    - Attach PostgreSQL database
        - In Heroku go to resources
        - Search for Postgres in the add-ons box
        - Select Heroku Postgres
        - Submit order form

    - Prepare the environment and settings.py file
        - Create env.py file
        - Add DATABASE_URL with the Postgres URL from Heroku
        - Add SECRET_KEY with a randomly generated key
        - Add SECRET_KEY and generated key to the config vars in Heroku
        - Add if statement to settings.py to prevent the production server from erroring
        - Replace insecure key with the environment variable for the SECRET_KEY
        - Add Heroku database as the back end
        - Migrate changes to new database

    - Get static media files stored on Cloudinary
        - Create a Cloudinary account
        - From the dashboard, copy the API Environment variable
        - In the settings.py file create a new environment variable for CLOUDINARY_URL
        - Add the CLOUDINARY_URL variable to Heroku
        - Add a temporary config var for DISABLE_COLLECTSTATIC
        - In settings.py add Cloudinary as an installed app
        - Add static and media file variables
        - Add templates directory
        - Change DIR's key to point to TEMPALTES_DIR
        - Add Heroku hostname to allowed hosts
        - Create directories for media, static and templates in the project workspace
        - Create a Procfile

- Deploy new empty project to Heroku

- Set debug = False in the settings.py file of the repository
- Commit and push all files to GitHub.
- In Heroku, remove the DISABLE_COLLECTSTATIC config var.
- In the deploy tab, go to the manual deploy sections and click deploy branch.

# 7. Project Completion

[Return to the Table of Contents](#table-of-contents)

## Desktop Version

## Mobile Version


# 8. Improvements

[Return to the Table of Contents](#table-of-contents)
This is a resubmission attempt since the last one didn't meet the project's criteria. 

# 9. Acknowledgements

[Return to the Table of Contents](#table-of-contents)

* Credits is given to  for given me some code to be used in the programme. This is the code that was implemented into my programme in which I modified.
```

``` 
* Credits is given to the Codestar walkthrough tutorial for how to create the website from scratch and its code. Some of the codes in this project were incorporated into awesome dishes.
```

```
* For the Readme file, I took the structure from my previous Readme file and used it here. Reference is given to https://github.com/dhakal79/Portfolio-project-MS1 which is the readme file I took into consideration when I was doing my first one.

* The ideas and code I implemented into this project were taught to me by Code Institute.
* My mentor Marcel Mulders supported me throughout the whole project. I couldn't have done it without his help.