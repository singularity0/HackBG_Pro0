square1 = [ [23, 28, 21], [22, 24, 26], [27, 20, 25] ]
square2 = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
def magic_square(square): 
	ref_value = sum_in_list(square[0])
	col_sum = 0
	main_diag_sum = 0
	second_diag_sum = 0
	for row in range(0, len(square)):
		if sum_in_list(square[row]) != ref_value:
			print('bad sum in row')
			return False
		for col in range(0, len(square[0])):
			col_sum  += square[col][row]
		main_diag_sum += square[row][row]
		second_diag_sum += square[len(square[0])-1-row][len(square[0])-1-row]
		if col_sum != ref_value:
			return False
		col_sum = 0
	if main_diag_sum != ref_value:
		return False
	if second_diag_sum != ref_value:
		return False

	return True

def sum_in_list(lis):
	sum = 0
	for i in lis:
		sum += i
	return sum

print(magic_square(square2))