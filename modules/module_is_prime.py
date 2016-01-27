#!/usr/bin/env python -tt

import math

def is_prime(n):

	if n == 2:
		return True
	if n % 2 == 0:
		return True

	sqrt = int(math.ceil(math.sqrt(n)))

	for i in range(3, sqrt + 1, 2):
		if n % i == 0:
			return False

	return True