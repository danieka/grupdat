binomials = {}

def binomial(n, k):
	if (n,k) in binomials.keys():
		result = binomials[(n, k)]
	else:
		if k == 0:
			result = 1
		elif n == 0:
			result = 0
		elif k == 1:
			result = n
		else:
			result = binomial(n-1, k-1) + binomial(n-1, k)
			binomials[(n, k)] = result

	return result

def triangel_bas_ner(dist, bredd):
	if bredd <= 0:
		return ""
	s = triangel_bas_ner(dist+1, bredd -1)
	s += ' '*dist
	for i in range(bredd):
		s += str(binomial(bredd-1, i))
		s += " "
	return s + "\n"

print(triangel_bas_ner(5,250))
