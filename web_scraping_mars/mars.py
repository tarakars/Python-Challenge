from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_BS
import os
from pymongo import MongoClient

app = Flask(__name__)


mongo = PyMongo(app)

@app.route('/')
def index():
    mars = mongo.db.mars.find_one()
    return render_template('index.html', mars = mars)


@app.route('/scrape')
def scrape():
    mars_data = mongo.db.mars
    data = scrape_BS.scrape()


    #mars_data.insert_one(data)

    data.pop('_id', None)

    mars_data.update(
        {},
        data,
        upsert=True
    )

    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)


