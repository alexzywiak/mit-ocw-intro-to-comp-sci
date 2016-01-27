#!/usr/bin/env python -tt

(sm, md, lg) = (6, 9, 20)

def has_solution(n):
	a_limit = n / sm + 1
	b_limit = n / md + 1
	c_limit = n / lg + 1

	for c in range(0, c_limit):

		for b in range(0, b_limit):

			for a in range(0, a_limit):

				if a * sm + b * md + c * lg == n:
					return True

	return False

def max_dio():

	count = 0
	i = 1
	last = 1

	while count < 6:
		if has_solution(i):
			count += 1
		else:
			last = i
			count = 0
		i += 1
	return last

def main():
	print max_dio()

if __name__ == "__main__":
	main()