def base_two_logarithm(n):
	"""Recursive algorithm to compute the integer part of the base-two
	logarithm of n using only addition and integer division.
	"""
	if n < 2:
		return 0
	else:
		return 1 + base_two_logarithm(n / 2)


def logarithm(x, n):
	"""Recursive algorithm to compute the integer part of the base-x
	logarithm of n using only addition and integer division.
	"""
	if n < x:
		return 0
	else:
		return 1 + logarithm(x, n / x)


if __name__ == '__main__':
	result = base_two_logarithm(1000)
	print(result)
	result2 = logarithm(5, 12905)
	print(result2)