seasons = ["winter", "summer", "summer", "summer", "spring", "srping"]
def winter_is_coming(seasons):
	counter = 0
	for i in seasons:
		if i != 'winter':
			counter += 1
		else:
			counter = 0
	return counter >= 5
print(winter_is_coming(seasons))