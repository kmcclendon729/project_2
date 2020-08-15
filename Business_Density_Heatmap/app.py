import pandas as pd
import json
import os
from flask import Flask, jsonify, render_template, redirect, Blueprint
from flask_pymongo import PyMongo

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

mongo = PyMongo(app, uri='mongodb://localhost:27017/yelpBusiness')

# add a CORS header to each response
@app.after_request
def after_request(response):
        header = response.headers
        header['Access-Control-Allow-Origin'] = '*'
        return response

#################################################
# Flask Routes
#################################################

# default route to render index.html
@app.route("/")
def index():    
    
    collection = mongo.db.openVegas.find_one()
    return render_template('index.html', vacation=collection)

# route to bring in our data from mongo DB
@app.route("/api")
def businessData():
    vegasBusinesses = mongo.db.openVegas.find({}, {'_id': False})
    # we need to use a list comprehension in order to loop through results so we can jsonify them
    businesses = [business for business in vegasBusinesses]
    data = {
        "businesses": businesses
    }
    
    return jsonify(data)

@app.route("/api/restaurants")
def restaurantData():
    vegasBusinesses = mongo.db.openVegas.find({"categories":{"$regex": "Restaurants"}}, {'_id': False})
    # vegasBusinesses = mongo.db.openVegas.find({"categories":{"$regex": "(.*Restaurant.*Pizza.*)|(.*Pizza.*Restaurant.*)"}}, {'_id': False})
    # we need to use a list comprehension in order to loop through results so we can jsonify them
    businesses = [business for business in vegasBusinesses]
    data = {
        "businesses": businesses
    }
    
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True)
