# import Flask, pymongo, and scrape_mars
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrape_mars import scrape

# Instantiate a Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/marsDB"
mongo = PyMongo(app)
# db = mongo.db

# Create a base '/' route that will query your mongodb database and render the `index.html` template
@app.route("/")
def mainpage():

# Create a '/scrape' route that will create the mars collection, run your scrape() function from scrape_mars, and update the mars collection in the database
# The route should redirect back to the base route '/' with a code 302.
@app.route("/scrape")
def call_scrape():
    # Call scrape_mars.scrape and save dictionary
    mars_dict = scrape()
    # Store response as a dictionary in MongoDB
    # mongo.db.collection.update({}, mars_dict, upsert=True)
    mongo.db.collection.insert_one(mars_dict)
    return redirect("/", 302)


# Run the app
if __name__ == "__main__":
    app.run(debug=True)