def krock(l1, l2):
	for el1 in l1:
		if el1 in l2:
			return True
	return False


print(krock([1, 2, 3, "hej"], [4, 5, 6, "hej"]))