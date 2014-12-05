def depth(l):
	if type(l) != list:
		return 0

	result = []
	for el in l:
		if type(el) == list:
			result.append(1 + depth(el))

	if len(result) == 0:
		return 1
	else:
		return max(result)

print(depth([1,2,3,[]]))