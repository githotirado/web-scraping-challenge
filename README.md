# web-scraping-challenge
Web application that scrapes various websites for data related to the Mission to mars

# Setup
install flask_pymongo (pip install Flask-PyMongo)
have your local mongodb running on port 27017

# Initialization
Run the main Flask file app.py in the background.
For the URL presented when running Flask, append the "/scrape" path to it for the first hit, (ex: http://127.0.0.1:5000/scrape).  This will make a first scrape pass at the Mars web sites and populate the back end MongoDB with at least one dictionary that can be used to draw the main page at http://127.0.0.1:5000/. 

# Notes
splinter and web crawling using headless=True, so you won't see the Chrome browser popping in and out when program is run
