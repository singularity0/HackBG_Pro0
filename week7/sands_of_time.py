def sands_of_time(n):
	for i in range(0, n):
		if i % 2 == 0:
			print('.' * ((n-(n-i))//2) , end = '')
			print('*' * (n-i), end ='')
			print('.' * ((n-(n-i))//2) , end = '')
			print()
	for i in range(0, n-1):
		if i % 2 != 0:
			print('.' * ((n - (i+2))//2), end = '')
			print('*' * (i + 2), end = '')
			print('.' * ((n - (i+2))//2), end = '')
			print()
sands_of_time(5)

