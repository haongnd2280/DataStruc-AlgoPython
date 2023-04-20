def exponen(base, exp):
	"""This function computes the number base^exp."""
	if exp == 0:
		return 1
	else:
		return base * exponen(base, exp - 1)


if __name__ == '__main__':
	result = exponen(3, 14)
	print(result)