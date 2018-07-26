# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 17:41:39 2018

@author: Michael Diaz
"""
import Flask
import PyMongo
import scrape_mars

from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

mongo = PyMongo(app)

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route('/scrape')
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars.update(
        {},
        mars_data,
        upsert=True
    )
    return 'Scraping Successful!'


if __name__ == "__main__":
    app.run(debug=True)