import copy


def rearrange_sequence01(S, start, stop):
	"""Recursive Python function that rearranges a sequence of integer values
	so that all the even values appear before all the odd values.
	"""
	if start == stop - 1:
		return
	else:
		if S[start] % 2 == 1:
			for i in range(start + 1, stop):
				if S[i] % 2 == 0:      # there is even element to exchange
					S[start], S[i] = S[i], S[start]
					break
				elif i == stop - 1:    # there is no even element left to exchange
					return             # exit immediately

		rearrange_sequence01(S, start + 1, stop)


def rearrange_sequence02(S, start, stop, check):
	"""Recursive Python function that rearranges a sequence of integer values
	so that all the even values appear before all the odd values.
	"""
	if check > stop - 1:
		return
	elif start == stop - 1:
		return
	else:
		if S[start] % 2 == 1:
			for i in range(check, stop):
				if S[i] % 2 == 0:
					S[start], S[i] = S[i], S[start]
					check = i + 1
					break
				elif i == stop - 1:    # there is no even element left to exchange
					return
		else:
			check = start + 2

		rearrange_sequence02(S, start + 1, stop, check)


if __name__ == '__main__':
	S1 = [1, 5, 2, 7, 4, 6, 9, 8]
	S2 = [2, 4, 7, 6, 5, 9, 14, 3, 8]
	rearrange_sequence01(S1, 0, len(S1))
	rearrange_sequence02(S2, 0, len(S2), 1)
	print("S1 = ", S1)
	print("S2 = ", S2)

