def permutations(l):
	if len(l) == 1:
		return [l]
	r = []
	for i, el in enumerate(l):
		for res in permutations(l[0:i] + l[i+1:]):
			r.append([el] + res)
	return r


print(len(permutations([1,2,3,4,5,6,7,8,9,10])))