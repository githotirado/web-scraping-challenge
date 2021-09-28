# web-scraping-challenge
Web application that scrapes various websites for data related to the Mission to mars.

# Setup
* Install flask_pymongo (pip install Flask-PyMongo).
* Have your local mongodb running on port 27017 as defined in app.py.

# Initialization
* Run the main Flask file app.py in the background.
* The MongoDB database will need at least one run of the scraping to display a good page the first time.  For the URL that is presented after running Flask, invoke the "/scrape" route for the first run (ex: http://127.0.0.1:5000/scrape).  This will make a first scrape pass at the Mars web sites and populate the back end MongoDB with at least one dictionary that can be used to draw the main page at http://127.0.0.1:5000/ for the first and subsequent visits. 

# Notes, debugging testing issues
* (Note) Allow 15-20 seconds after clicking the 'scrape' button because there are 5-second sleep delays put in after each scrape in order to allow any browser activity to catch up.
* (Note) splinter and web browser initiation is using 'headless=True', so you won't see the Chrome browser popping in and out when the scraping is occurring.
* (Note) there was no Mars current weather portion in this exercise.  Nothing to display.
* (Debugging) The scraping file scrape_mars.py can be run independently in a terminal to confirm its success.