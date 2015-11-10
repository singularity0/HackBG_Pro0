def str_reverse(st):
	result =''
	for i in range(0, len(st)):
		result += st[len(st)-1-i]
	# result = st[::-1]
	return result
# print(str_reverse('kudos'))

def join(delimiter, items):
	string = ''
	for c in range(0, len(items)):
		string += str(items[c])
		if c < len(items)-1:
			string += delimiter
	return string
# print(join("|", [1, "there"]))
# print(join("@@@", [1, 2, 3]))

def startswith(search, string):
	for i in range(0, len(search)):
		if string[i] != search[i]:
			return False
	return True
# print(startswith("Py", "Python"))

def endswith(search, string):
	return startswith(search, str_reverse(string))
# print(endswith("kapak", "babakapak"))

def trim(string):
	li = []
	st =''
	for item in string:
		li.append(item)
	while li[0] == ' ':
		li.pop(0)
	while li[len(li)-1] == ' ':
		li.pop()
	for i in li:
		st += i
	return st
# print(trim("   asda   "))

def trim_left(string):
	li = []
	st =''
	for item in string:
		li.append(item)
	while li[0] == ' ':
		li.pop(0)
	for i in li:
		st += i
	return st
# print(trim_left("   asda   "))

def trim_right(string):
	result =  str_reverse(trim_left(reversed(string)))
	return result

# def trim(string):
# 	return trim_left(trim_right(string))
# print(trim("   asdaw   "))

