def recursive_product(m, n):
	"""This function compute the product of two positive integers, using only
	addition and subtraction.
	"""
	if n == 0:
		return 0
	else:
		return m + recursive_product(m, n - 1)

# Idea: Use m to add, n to count. Add m with itself up to n times, after each addition, we
#       decrement n. If n == 0 => return 0.


if __name__ == '__main__':
	result = recursive_product(5, 12)
	print("result = ", result)