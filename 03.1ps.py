#!/usr/bin/env python -tt

def countSubStringMatch(target, key):
	
	idx = target.find(key, 0)
	count = 0

	while idx != -1:
		idx = target.find(key, idx + len(key))
		count += 1

	return count



def countSubStringMatchRecursive(target, key):

	idx = target.find(key)
	count = 0

	if idx != -1:
		count += 1
		if (idx + len(key)) < len(target):
			substr = target[idx + len(key):]
			count += countSubStringMatchRecursive(substr, key)

	return count


def subStringMatchExact(target, key):
	
	idx = target.find(key, 0)
	match_tuple = ()

	while idx != -1:
		match_tuple = match_tuple + (idx,)
		idx = target.find(key, idx + len(key))

	return match_tuple


def main():
  # print countSubStringMatch('def', 'abc')
  # print countSubStringMatchRecursive('abcdeabcfabc', 'abc')
  print subStringMatchExact("atgacatgcacaagtatgcat","atgc") 


if __name__ == "__main__":
	main()