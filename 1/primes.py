# coding=utf-8
# The coding above is only necessary with Python 2

possible_prime = 2

while True:
	#This first loop loops over possible primes
	divisor = 2
	is_prime = True #For keeping track of whether possible_prime actually is a prime
	while divisor < possible_prime:
		#This second loop loops over possible divisors
		if possible_prime % divisor == 0:
			# Possible prime is not a prime and we keep track of that with is_prime and break the loop
			is_prime = False
			break
		else:
			#Go to the next divisor
			divisor = divisor + 1

	if is_prime:
		#If possible prime was a prime we should print it
		print(possible_prime)

	#Go to the next possible prime
	possible_prime = possible_prime + 1
