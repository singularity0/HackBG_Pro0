students = [{
              "name": "RadoRado",
              "status": "not_finalized"
            }, {
              "name": "Ivo",
              "status": "finalized"
            }, {
              "name": "Genadi",
              "status": "finalized"
            }]

result =	{}      

def status_count(students):
	list_fnzd =[]
	for everybody in students:
		if everybody['status'] == 'finalized':
			list_fnzd.append(everybody['name'])
			result['finalized'] = list_fnzd
		else:
			result['not_finalized'] = [everybody['name']]
	return result
print(status_count(students))