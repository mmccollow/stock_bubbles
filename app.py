#!/usr/bin/env python

from flask import Flask
from scrape import load_data

app = Flask(__name__)

@app.route("/data.json")
def data_json():
	return str(load_data())

@app.route("/")
def index():
	return render_template("index.html")

if __name__ == "__main__":
	app.run()