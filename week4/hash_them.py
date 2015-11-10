keys = ['Ivan', 'Maria', 'pesho']
values = [1,2,4,5]
dic = {}
def hash_them(keys, values):
	if len(values) < len(keys):
		while len(values) < len(keys):
			values.append(None)
	if len(keys) < len(values):
		while len(keys) < len(values):
			keys.append(None)
	for i in range(0,len(keys)):	
		dic[keys[i]] = values[i]
	return dic
print(hash_them(keys,values))
