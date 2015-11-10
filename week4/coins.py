sum = 8.94
sum *= 100
l = [100, 50, 20, 10, 5, 2, 1]
dic = {1: 0, 2 : 0, 5 : 0, 10 : 0, 20 : 0, 50 : 0, 100 : 0 }
def calculate_coins(sum):
	for i in l:
		if sum > i:
			dic[i] = sum // i
			sum -= dic[i] * i
	return dic
print(calculate_coins(sum))


# 	# if sum > 100:
# 	# 	dic[100] = sum // 100
# 	# 	sum -= dic[100] * 100
# 	# if sum > 50:
# 	# 	dic[50 ] = sum // 50
# 	# 	sum -= dic[50 ] * 50
# 	# 	# print(sum)
# 	# if sum > 20:
# 	# 	dic[20] = sum // 20
# 	# 	sum -= dic[20] * 20
# 	# if sum > 10:
# 	# 	dic[10] = sum // 10
# 	# 	sum -= dic[10] * 10
# 	# if sum > 5:
# 	# 	dic[5] = sum // 5
# 	# 	sum -= dic[5] * 5
# 	# if sum > 2:			
# 	# 	dic[2] = sum // 2
# 	# 	sum -= dic[2] * 2
# 	# 	# print(sum)
# 	# if sum >= 1:
# 	# 	dic[1] = sum // 1
# 	# 	sum -= dic[1] * 1
# 	return dic
# print(calculate_coins(sum))
