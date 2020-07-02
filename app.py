import urllib.request as urllib
import re
import sys
import json

def	response_to_json(array):
	new_dict = {}
	targets = []
	source = array[0].split(' vs ')[0]
	for x in array:
		targets.append(x.split(' vs ')[1])
	new_dict.update({source : targets})
	print(new_dict)


def main():
	if len(sys.argv) != 2:
		print("Usage: ./app.py [QUERY_STRING]")
		exit()

	add_url = sys.argv[1] + "%20vs%20"
	base_url = "http://suggestqueries.google.com/complete/search?&output=toolbar&gl=fi&hl=en&q="
	url = base_url + add_url

	response = str(urllib.urlopen(url).read())
	array = re.findall("\<suggestion data=\"(.+?)\"", response)
	print(array)
	response_to_json(array)

if __name__ == "__main__":
	main()