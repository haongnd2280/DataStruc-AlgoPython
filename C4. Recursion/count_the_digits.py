def digits_number(n):
	"""Recursive function to count the the digits of a given number
	using recursion.
	"""
	if n == 0:
		return 0
	else:
		return 1 + digits_number(n // 10)


if __name__ == '__main__':
	result = digits_number(7383749)
	print(result)
