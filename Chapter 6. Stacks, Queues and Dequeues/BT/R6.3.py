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


def transfer(S: ArrayStack, T: ArrayStack):
	"""Transfers all elements from stack S onto stack T, so that the element starts at
	the top of S is the first to be inserted onto T, and the element at the bottom of S
	ends up at the top of T.
	"""
	while not S.is_empty():
		T.push(S.pop())       # simultaneously implement push and pop operations


if __name__ == '__main__':
	S = ArrayStack()  # create instance
	T = ArrayStack()
	S.push(5)
	S.push(3)
	S.push(7)
	S.push(9)
	S.push(4)
	S.push(6)

	transfer(S, T)
	while not T.is_empty():
		print(T.pop())



