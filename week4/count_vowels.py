word  = 'aaaAcccD'
vowels = 'aeiouyAEIOUY'
conson = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
d = {'vowels': 0, 'consonants': 0}
def count_vowels_consonants(word):
	for i in word:
		if i in vowels:
			d['vowels'] += 1
		elif i in conson:
			d['consonants'] += 1
		else:
			print('There is a non letter symbol')
			break
	return d
print(count_vowels_consonants(word)) 
