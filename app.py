# MongoDB and Flask Application
#################################################

# Dependencies and Setup
from flask import Flask, render_template
from flask_pymongo import PyMongo
import nasa_scraper
import datetime as dt
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import os
import requests
from webdriver_manager.chrome import ChromeDriverManager


# Flask Setup

app = Flask(__name__)

#End Flask Set up

# PyMongo Connection Setup

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# End PyMongo Connection Setup


# Flask Routes

# Root Route to Query MongoDB & Pass Mars Data Into HTML Template: index.html to Display Data
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("./index.html", mars=mars)

# Scrape Route to Import `nasa_scraper.py` Script & Call `scrape` Function
@app.route("/scrape")
def scrapper():
    mars = mongo.db.mars
    mars_data = nasa_scraper.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return "Scraping Successful"

# Define Main Behavior
if __name__ == "__main__":
    app.run()