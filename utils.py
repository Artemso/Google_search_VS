def	replace_spaces(str1):
	new_str = ""
	for x in str1:
		if x == " ":
			new_str += "%20"
		else:
			new_str += x
	return new_str

def	err_exit(msg):
	print(msg)
	exit(0)