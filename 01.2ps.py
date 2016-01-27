#!/usr/bin/env python -tt
import math
import sys

sys.path.append('./modules')

from module_is_prime import *

def sum_of_logs(n):

	log_sum = math.log(2)
	prime_count = 1
	i = 3

	while prime_count < n:
		if is_prime(i):
			prime_count += 1
			log_sum += math.log(i)
		i += 2

	print 'n: ' + str(n)
	print 'nth prime: ' + str(i)
	print 'log sum: ' + str(log_sum)
	print 'ratio: ' + str(log_sum / i)


def main():
	sum_of_logs(25000)

if __name__ == "__main__":
	main()