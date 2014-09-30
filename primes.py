# coding=utf-8

from math import sqrt


possible_prime = 2
i = 2

while True:
	is_prime = True
	i = 2
	while i <= sqrt(possible_prime):
		if possible_prime % i == 0:
			is_prime = False
		i += 1

	if is_prime:
		print(possible_prime, " is a prime.")
	
	possible_prime += 1
