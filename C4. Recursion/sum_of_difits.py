def digits_sum(n):
	"""Recursive algorithm to find the sum of digits of a number."""
	if n == 0:
		return 0
	else:
		return n % 10 + digits_sum(n // 10)


if __name__ == '__main__':
	result = digits_sum(3843274)
	print(result)