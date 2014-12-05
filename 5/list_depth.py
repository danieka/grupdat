def list_depth(l):
	if type(l) != list:
		return 0

	depth = []
	for el in l:
		if type(el) == list:
			depth.append(1 + list_depth(el))

	if depth == []:
		return 1
	else:
		return max(depth)


print(list_depth([[[1]], 2 ,[3, 4]]))

