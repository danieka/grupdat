# coding: utf8

def fakultet(a):
	k = 1
	if a < 0 or type(a) != int:
		return "Fel"
	for i in range(2, a+1):
		k *= i
	return k

inp = float(input("Skriv in ett tal: "))
result = fakultet(inp)
print(result)













