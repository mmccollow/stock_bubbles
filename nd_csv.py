import csv
import urllib2
import StringIO
import json

URL = "http://www.nasdaq.com/quotes/nasdaq-100-stocks.aspx?render=download"

# try to simulate Chrome
HEADERS= {
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
	"Accept-Encoding": "gzip,deflate,sdch",
	"Accept-Language": "en-US,en;q=0.8",
	"Cookie": "clientPrefs=||||lightg; \
	__atuvc=1%7C24%2C1%7C25; \
	s_sess=%20s_cc%3Dtrue%3B%20s_sq%3Dnasdaqprod%253D%252526pid%25253DFlashQuotes%25252520-%25252520Nasdaq%25252520100%252526pidt%25253D1%252526oid%25253Dhttp%2525253A//www.nasdaq.com/quotes/nasdaq-100-stocks.aspx%2525253Frender%2525253Ddownload%252526ot%25253DA%3B; \
	s_pers=%20bc%3D1%7C1403018677068%3B%20s_nr%3D1403105222488-Repeat%7C1410881222488%3B; \
	NSC_W.TJUFEFGFOEFS.OBTEBR.80=ffffffffc3a08e3745525d5f4f58455e445a4a423660"
}

def get_stocks_data():
	req = urllib2.Request(URL, headers=HEADERS)
	page = urllib2.urlopen(req)

	csvfile = StringIO.StringIO(page.read())
	csvdict = csv.DictReader(csvfile)

	output = {'children': []}
	for item in csvdict:
		output['children'].append({
			'symbol': item['Symbol'].strip(),
			'name': item[' Name'].strip(),
			'price': item[' lastsale'].strip(),
			'change_d': item[' netchange'].strip(),
			'change_p': item['pctchange'].strip(),
			'volume': item[' share_volume'].strip(),
			'value': item[' Nasdaq100_points'].strip()
		})
	return json.dumps(output)

