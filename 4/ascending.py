def is_ascending(l):
	if len(l) <= 1:
		return True
	return l[0] <= l[1] and is_ascending(l[1:])

print(is_ascending([1,2,3,9]))
print(is_ascending([1,3,2,5]))