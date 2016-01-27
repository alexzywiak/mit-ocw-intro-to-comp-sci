#!/usr/bin/env python -tt
import math
import sys

sys.path.append('./modules')

from module_is_prime import *

def find_nth_prime(n):

	primes = [2]
	i = 3

	while len(primes) < n:
		if is_prime(i):
			primes.append(i)
		i += 2

	print len(primes)
	return primes[-1]

def main():
	print find_nth_prime(1000)

if __name__ == "__main__":
	main()