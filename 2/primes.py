# coding: utf-8

from math import sqrt

def is_prime(possible_prime):
	is_prime = True
	if possible_prime == 2:
		return True
	for i in range(2, int(sqrt(possible_prime))+2):
		if possible_prime % i == 0:
			is_prime = False

	return is_prime


start = 2
for i in range(start, 15):
	print(is_prime(i), i)

