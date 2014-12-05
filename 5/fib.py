import time

fib_numbers = {0: 0, 1: 1}

def fib(n):
	if n in fib_numbers.keys():
		return fib_numbers[n]
	else:
		fib_n = fib(n-1) + fib(n-2)
		fib_numbers[n] = fib_n
		return fib_n

while True:
	n = int(input("Input a number: "))
	start = time.time()
	print(fib(n))
	end = time.time()
	print(end-start)