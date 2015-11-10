list_of_words = ["words", "are", "meaningful", "words", "words", "are"]

def count_words(words):
	result_dict = {}
	for i in words:
		if i in result_dict:
			result_dict[i] += 1
		else:
			result_dict[i] = 1
	return result_dict
print(count_words(list_of_words))