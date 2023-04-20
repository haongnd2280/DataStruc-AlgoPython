def find_max(S, start, stop, max):
	"""Recursive algorithm for finding the maximum element in a sequence S of n elements."""
	if start == stop:
		return max
	else:
		if S[start] > max:
			max = S[start]
		return find_max(S, start + 1, stop, max)

# Analysis: The sequence S here is assumed to be arbitrary in order, so the essence of recursive
#           algorithm is still linear.
# The idea of the above recursive function is similar to reverse() function.

if __name__ == '__main__':
	S = [1, 5, 2, 6, 7, 10, 4, 15, 9, 3, 8]
	maximum = find_max(S, 1, len(S), S[0])
	print("max = ", maximum)