def string_matrix(matrix_width, li):
	result = []
	li_aligned = ''
	for i in li:
		if len(i) == matrix_width:
			result.append(i)
		elif len(i) < matrix_width:
			result.append(i + 'X' * (matrix_width - len(i)))
		else:
			result.append(i[0:matrix_width])
	
	for element in result:
		for ch in element:
			li_aligned += " | "
			li_aligned += ch
		li_aligned += ' | '
		li_aligned += '\n'
	return li_aligned


print(string_matrix(6,["python","gogo","perl","java","haskell","ruby0nRails"]))