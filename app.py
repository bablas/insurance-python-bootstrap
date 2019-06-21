from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
import time
import json
import os
import requests
from bson import json_util
import pandas as pd

app = Flask(__name__)
CORS(app)

mongo = PyMongo(app, uri="mongodb://localhost:27017/underwriting_data")

@app.route("/")
def home():
	return render_template("index.html")

# one time function to convert csv to json
@app.route("/csvtojson3k")
def csvToJson3k():
	csv_file = pd.DataFrame(pd.read_csv("static/data/0_to_3k.csv", sep = ",", header = 0, index_col = False))
	csv_file.to_json("static/data/data_0_to_3k.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)
	return "The 0 to 3k csv file is converted"
# one time function to convert csv to json
@app.route("/csvtojson3ktoall")
def csvtojson3ktoall():
	csv_file = pd.DataFrame(pd.read_csv("static/data/3k_to_all.csv", sep = ",", header = 0, index_col = False))
	csv_file.to_json("static/data/data_3k_to_all.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)
	return "The 3k to all csv file is converted"

@app.route("/data3k")
def showData3k():
	data3k = open(os.path.join("static", "data", "data_0_to_3k.json"))
	return json.dumps(list(data3k))

@app.route("/data3ktoall")
def showData3ktoall():
	data3ktoall = open(os.path.join("static", "data", "data_3k_to_all.json"))
	return json.dumps(list(data3ktoall))

if __name__ == '__main__':
	app.run(debug=True)