numbers = [1, 2, 3, 4, 5]
def prime_pair(numbers):
	for i in range(0, len(numbers)):
		for j in range(0, len(numbers)):
			if (numbers[i] + numbers[j]) % 2 != 0:
				print (numbers[i], numbers[j])
				return True
	return False 
print(prime_pair(numbers))
