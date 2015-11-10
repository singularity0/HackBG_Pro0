numbers = [0, 2, -2, 5, 10]
def count_zero_pairs(numbers):
	counter = 0
	for i in range(0, len(numbers)):
		for j in range(i, len(numbers)):
			if numbers[i] + numbers[j] == 0:
				counter += 1
				print(str(numbers[i]) + 'and' + str(numbers[j]) )
	return counter
print(count_zero_pairs(numbers))
