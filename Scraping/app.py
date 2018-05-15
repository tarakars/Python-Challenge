# import necessary libraries
from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_BS

# create instance of Flask app
app = Flask(__name__)


mongo = PyMongo(app)

#  create route that renders index.html template
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_BS.scrape()
    mars.update(
        {},
        mars_data,
        upsert=True
    )
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)