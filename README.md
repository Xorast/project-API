# SINGLE PAGE APPLICATION & API

SPA using API to get news from online newspapers on user chosen topic and a custom micro-API to get tweets on given topics (Cyber Security, Full Stack, Internet of Things).

[http://api.xavierastor.com](http://api.xavierastor.com)

## OVERVIEW - WHAT IS THIS APPLICATION FOR ?

This application is a personnal training to understand SPA structure and work with API. 

The application got a single page that has two menus:
* The first menu enables the user to look for articles from online newspapers.
* The second menu enables the user to look for tweets on a set topic.

## HOW TO USE IT ?

Once on the [website](http://api.xavierastor.com) landing page, the user has two menus and can choose to look for articles or to look for tweets.
The use of the application is pretty straightforward (classic UI).

## HOW DOES IT WORK ?

Once the page loaded, the application runs on the client side only (spa.js).

The "Articles" feature is taking the user input and send a request to the [http://newsapi.org](newsapi.org) API to get articles.
The user can chose the language and the sorting method with radio buttons. Those parameters are sent with the GET request to the API.
The response is processed with a local JS script that create a new row for each articles and write the article data into it.

The "Tweets" feature is taking the user topic choice among a set of topics and send a request to a custom API to get tweets.
This API is built with an application that grabs tweets (using tweepy) and store them online in a Mongo Data Base (Mlab).
The online database is then used as an API. The "tweet grabber" application is run hourly by the hosting server to update the database.
Once the response from the GET request ready, a local JS script  create a new row for each tweet and write the tweet data into it.

## ARCHITECTURE

The application is started on the backend with the application.py file (Flask app).
The landing page is sent with the code to run the application on the client side : spa.js (and jquery.js).
The ux.js, shipped as well with the landing page, contains script to enhance user experience.

The "tweet_..." files are for the creation and update of the Mongo Database. They run independently from the application.
They are runned hourly by the host server add-on "Heroku Scheduler" to update the database.

The files "get_data.py" and "mpa.html" are coming from the first version of this application (running on the server side) and are no longer required. They are kept for personal "archive".
    
## AUTHOR(S)

* Xorast

## BUILT WITH
### LANGUAGES

The application is written in:
* JavaScript
* [Python 3](https://www.python.org/) (3.4.3)
* HTML5 
* CSS3

### FRAMEWORK & LIBRAIRIES

The following frameworks and librairies have been used:
* [Tweepy](http://www.tweepy.org/)
* [PyMongo](https://api.mongodb.com/python/current/)
* [Flask](http://flask.pocoo.org/)
* [Bootstrap](http://getbootstrap.com/) version 4.1.3
* [jQuery](https://jquery.com/)

### SERVICES
* Online NoSQL Database : [MongoDB - mLab](https://mlab.com/)
* Host : [Heroku](https://heroku.com)
* Scheduler : [Heroku Scheduler](https://devcenter.heroku.com/articles/scheduler)

## CREDITS
* News API : [http://newsapi.org](https://newsapi.org)
* Tweets: [Twitter.com](https://twitter.com)
* Theme: [Bootswatch](https://bootswatch.com/) - Used theme [here](https://bootswatch.com/lux/)