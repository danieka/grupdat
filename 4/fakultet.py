def fakultet(i):
	if i == 1:
		return 1
	return i * fakultet(i-1)

print(fakultet(40))