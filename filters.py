def	filter_key(dict):
	ref = list(dict.keys())[0]
	lst = dict[ref]
	for x in lst:
		if x.find(ref) != -1:
			lst.remove(x)

def	filter_duplicates(dict):
	key = list(dict.keys())[0]
	lst = dict[key]
	new_lst = []
	flag = 0
	for x in lst:
		if new_lst:
			for y in new_lst:
				if (x.find(y) != -1 or y.find(x) != -1):
					flag = 1
					break
		if flag == 1:
			flag = 0
			continue
		else:
			new_lst.append(x)
	dict[key] = new_lst