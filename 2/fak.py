# coding=utf-8
# The coding above is only necessary with Python 2

#Två olika varianter på fakultet
def fak_while(n):
	summa = 1
	i = 1
	while i <= n:
		summa *= i
		i += 1
	return summa

def fak_for(n):
	summa = 1
	for i in range(1, n+1):
		summa *= i
	return summa

print(fak_while(5))
a = fak_for(5)
print(a)
