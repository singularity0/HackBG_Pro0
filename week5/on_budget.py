books = [0, 10, 100, 5, 3, 8, 25]
budget = 35

result = {"books_on_budget": 0, 'loan': 0}
def on_budget(books, budget):
	books = sorted(books)

	while budget > books[0]:
		result['books_on_budget'] += 1
		budget -= books.pop(0)

	result['loan'] -= budget

	for books_left_prices in books:
		result['loan'] += books_left_prices

	return result
	
print(on_budget(books, budget))
