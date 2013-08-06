#!/usr/bin/env python

from flask import Flask
from flask import render_template, url_for
from scrape import load_data, format_json

app = Flask(__name__)

@app.route("/data.json")
def data_json():
	return format_json(load_data())

@app.route("/")
def index():
	d3 = url_for('static', filename='js/d3.v3.min.js')
	bootstrapjs = url_for('static', filename='js/bootstrap.min.js')
	bootstrapcss = url_for('static', filename='css/bootstrap.min.css')
	qr = url_for('static', filename='img/qrcode.png')
	return render_template("index.html", d3=d3, bootstrapjs=bootstrapjs, bootstrapcss=bootstrapcss, qr=qr)

if __name__ == "__main__":
	app.run(debug=True)