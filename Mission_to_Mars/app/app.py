# import Flask, pymongo, and scrape_mars (your python file)
from flask import Flask
import pymongo
from scrape_mars import scrape

# Instantiate a Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Create a base '/' route that will query your mongodb database and render the `index.html` template
@app.route("/")
def query_mongo():

# Create a '/scrape' route that will create the mars collection, run your scrape() function from scrape_mars, and update the mars collection in the database
# The route should redirect back to the base route '/' with a code 302.
@app.route("/scrape")
def mars_collection():


# Run your app