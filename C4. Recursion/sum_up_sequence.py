def sum_up_sequence(A):
	"""Sum up the values in a sequence A of n integers, where n is a power of 2."""
	if len(A) == 1:
		return A[0]
	else:
		B = [0] * (len(A) // 2)
		for i in range(len(B)):
			B[i] += A[2 * i] + A[2 * i + 1]
		return sum_up_sequence(B)


if __name__ == '__main__':
	A = [1, 2, 3, 4, 5, 6, 4, 2, 6, 9, 8, 3, 7, 2, 5, 7]
	result = sum_up_sequence(A)
	print(result)
