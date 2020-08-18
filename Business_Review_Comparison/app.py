from flask import Flask, render_template, redirect, Blueprint, jsonify, request
from flask_pymongo import PyMongo
import os
import pandas as pd
import json



app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/yelpBusiness")

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response 

# Route to render index.html template using data from mongo
@app.route("/")
def home():

    collection = mongo.db.openVegas.find_one()
    return render_template('index.html', vacation=collection)
    
# Route to get data
@app.route("/api")
def api():
    
    collections = mongo.db.openVegas.find({}, {'_id': False})
    data = [collection for collection in collections]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)