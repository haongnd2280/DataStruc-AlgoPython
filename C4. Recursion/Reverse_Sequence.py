def reverse(S, start, stop):
	"""Reverse elements in implicit slice S[start:stop]."""
	if start < stop - 1:                                      # if at least 2 elements
		S[start], S[stop - 1] = S[stop - 1], S[start]         # swap first and last
		reverse(S, start + 1, stop - 1)


if __name__ == '__main__':
	array = [4, 3, 6, 2, 8, 9, 5]
	reverse(array, 0, len(array))
	print("new array = ", array)
