class Empty(Exception):
	"""Error attempting to access an element from an empty container."""
	pass


class ArrayStack:
	"""LIFO Stack implementation using a Python list as underlying storage."""

	def __init__(self):
		"""Create an empty stack."""
		self._data = []  # nonpublic list instance

	def __len__(self):
		"""Return the number of elements in the stack."""
		return len(self._data)

	def is_empty(self):
		"""Return True if the stack is empty."""
		return len(self._data) == 0

	def push(self, e):
		"""Add element e to the top of the stack."""
		self._data.append(e)  # new item stored at the end of list

	def top(self):
		"""Return (but not remove) the element at the top of the stack.

		Raise Empty exception if the stack is empty.
		"""
		if self.is_empty():
			raise Empty('Stack is empty.')
		return self._data[-1]  # the last item in the list.

	def pop(self):
		"""Remove and return the element from the top of the stack (i.e, LIFO).

		Raise Empty exception if the stack is empty.
		"""
		if self.is_empty():
			raise Empty('Stack is empty.')
		return self._data.pop()  # remove last item from list.


def is_matched(expr):
	"""Return True if all delimiters are properly matched; False otherwise."""
	lefty = '({['                     # opening delimiters
	righty = ')}]'                    # respective closing delimiters

	S = ArrayStack()
	for c in expr:                    # loop through the string argument
		if c in lefty: 
			S.push(c)                 # push left delimiter on stack
		elif c in righty:
			if S.is_empty():
				return False          # nothing to match with
			if righty.index(c) != lefty.index(S.pop()):
				return False          # mismatched

	return S.is_empty()               # were all symbols matched?


if __name__ == '__main__':
	expr1 = '()(()){([()])}'
	expr2 = '((()(()){([()])}))'
	expr3 = ')(()){([()])}'
	expr4 = '[(5 + x) - (y + z)]'
	print(is_matched(expr1))
	print(is_matched(expr2))
	print(is_matched(expr3))
	print(is_matched(expr4))

# Note: The stack used above stores only characters from lefty.

