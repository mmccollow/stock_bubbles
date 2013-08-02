#!/usr/bin/env python

from bs4 import BeautifulSoup
import urllib2
import json

URL = "http://www.nasdaq.com/quotes/nasdaq-100-stocks.aspx"

def load_data():
	# get the page content
	page = urllib2.urlopen(URL)
	soup = BeautifulSoup(page.read(), 'lxml')

	# extract the JSON data
	scripts = soup.find_all('script')
	target = scripts[14]
	json_string = target.text.split('=')[1][:-9]
	json_data = json.loads(json_string)

	"""
	json_data[x][0] = stock symbol
	json_data[x][1] = company name
	json_data[x][2] = stock price in $
	json_data[x][3] = change in stock price in $
	json_data[x][4] = change in stock price in %
	json_data[x][5] = share volume
	json_data[x][6] = "NASDAQ-100 Points"
	"""
	return json_data