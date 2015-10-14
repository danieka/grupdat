def allapos(l):
	for i in range(len(l)):
		if l[i] < 0:
			return False
	return True

print(allapos([1,2,3,5,9]))