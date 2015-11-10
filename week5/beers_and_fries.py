
beers = [1000, 1010, 1020, 1030, 1040]
fries = [834, 500, -1, 0, 60]

def max_score(beers, fries):
	max_score = 0
	beers = sorted(beers)
	fries = sorted(fries)
	for i in range(0, len(beers)):
		max_score += beers[i] * fries[	i]
		# max_score += beers[len(beers)-1-i] * fries[len(fries)-1-i]

	return max_score

print(max_score(beers, fries))
