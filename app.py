import urllib.request as urllib
import re
import sys
import json
from filters import filter_duplicates, filter_key
from utils import replace_spaces, err_exit
from visualise import Visualise

def	response_to_json(array):
	new_dict = {}
	targets = []
	source = array[0].split(' vs ')[0]
	for x in array:
		if (len(targets) < 5):
			try:
				targets.append(x.split(' vs ')[1])
			except:
				continue
	new_dict.update({source : targets})
	filter_key(new_dict)
	filter_duplicates(new_dict)
	return (new_dict)

def	make_search(string):
	new_str = replace_spaces(string)
	add_url = new_str + "%20vs%20"
	base_url = "http://suggestqueries.google.com/complete/search?&output=toolbar&gl=fi&hl=en&q="
	url = base_url + add_url

	response = str(urllib.urlopen(url).read())
	array = re.findall("\<suggestion data=\"(.+?)\"", response)
	if array:
		new_dict = response_to_json(array)
	else:
		print("No suggestions found! for " + string)
	return new_dict

def	make_iteration(dictionary):
	new_dict = {}
	for key, lst in dictionary.items():
		for x in lst:
			new_dict.update(make_search(x))
	return new_dict


def main():
	if len(sys.argv) != 2:
		err_exit("Usage: ./app.py [QUERY_STRING]")

	total = {}
	duct = make_search(sys.argv[1])
	total.update(duct)
	for x in range(1):
		total = make_iteration(total)
	print(total)
	visu = Visualise()
	visu.visualise_graph(total)

if __name__ == "__main__":
	main()