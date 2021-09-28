# import Flask, pymongo, and scrape_mars
from flask import Flask, render_template
from flask_pymongo import pymongo
from scrape_mars import scrape

# Instantiate a Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_db

# Create a base '/' route that will query your mongodb database and render the `index.html` template
@app.route("/")
def mainpage():

# Create a '/scrape' route that will create the mars collection, run your scrape() function from scrape_mars, and update the mars collection in the database
# The route should redirect back to the base route '/' with a code 302.
@app.route("/scrape")
def call_scrape():
    Post = scrape()
    db.marsinfo.insert_one(Post)
    return


# Run the app
if __name__ == "__main__":
    app.run(debug=True)