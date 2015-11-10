def head(lis):
	return lis[0]
# print(head([100,2,3]))
# print(head(["Python"]))


def last(lis):
	return lis[len(lis)-1]
# print(last([100,2,3]))

def tail(lis):
	# lis.pop(0)
	lis.remove(lis[0])
	return lis
# print(tail([100,2,3]))

def equal_lists(list1, list2):
	if len(list1) != len(list2):
		return False
	for i in range(0, len(list1)):
		if list1[i] != list2[i]:
			return False
	return True
# print(equal_lists([1, 2], [1, 2, 1]))

def count_item(el, li):
	counter = 0
	for item in li:
		if item == el:
			counter += 1
	return counter 
# print(count_item("winter", ["winter", "winter"]))

def take(el, li):
	new_list = []
	for i in range(0, el):
		new_list.append(li[i])
	return new_list
# print(take(3, [3, 4, 5, 6, 7, 8]))

def drop(el, li): 
	new_list = []
	for i in range(el, len(li)):
		new_list.append(li[i])
		# print(new_list)
	return new_list
# print(drop(1, [1, 2, 3]))

def reverse(li):
	new_list = []
	for i in range(0, len(li)):
		new_list.append(li[len(li)-1-i])
	# new_list = li[::-1]
	return new_list
print(reverse(["Speak", "in", "reverse", "you", "must!"]))
