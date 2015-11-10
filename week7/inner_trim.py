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

def inner_trim(string):
	return ' '.join(string.split())
print(inner_trim("  Python    Django     "))