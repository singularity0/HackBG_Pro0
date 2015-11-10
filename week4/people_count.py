import test_data
x = test_data.generate_test(3)
print(x)
def get_people_count(x):
	activity = []
	for i in x:
		if i not in activity:
			activity.append(i)
	print(len(activity))
	return len(activity)
get_people_count(x)

# def get_people_count2(x):
# 	sett = set()
# 	for i in x:
# 		sett.add(i)
# 	print(sett)
# 	return sett
# get_people_count2(x)

# #recreate test_generation:
# from random import randint
# def generte_test(counter):
# 	names = ["Ivo", "Maria", "Anetta", "Philip", "Rado", "Gergana"]
# 	result = []
# 	for i in names:
# 		for j in range(1, randint(1, 3)):
# 			result.append(i)
# 	print (result)
# 	return result
# generte_test(3)