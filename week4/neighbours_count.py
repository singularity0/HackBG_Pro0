numbers = [1, 2, -2, 0, 0, 5, -5]
def count_zero_neighbours(numbers):
	count = 0
	for i in range(0,len(numbers)-1):
		if numbers[i] + numbers[i + 1] == 0:
			count += 1
			print('numbers ' + str(numbers[i]) + 'and' + str(numbers[i+1]))
	return count
print(count_zero_neighbours(numbers))

