def fib(i):
	if i == 0:
		return 0
	if i == 1:
		return 1
	else:
		return fib(i-2) + fib(i-1)

print(fib(30))

