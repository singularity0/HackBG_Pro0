# is list1 a sublist of list2

def sublist(list1, list2):
	for item in list1:
		if item not in list2:
			return False
	return True

# print(sublist(["Python"], ["Python", "Django"]))
print(sublist([1,22], [1, 0, 1, 2, 2]))