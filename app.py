import urllib.request as urllib
import re
import sys

if len(sys.argv) != 2:
	print("Usage: ./app.py [QUERY_STRING]")
	exit()

add_url = sys.argv[1] + "%20vs%20"
base_url = "http://suggestqueries.google.com/complete/search?&output=toolbar&gl=us&hl=en&q="
url = base_url + add_url

response = str(urllib.urlopen(url).read())
x = re.findall("\<suggestion data=\"(.+?)\"", response)
print(x)