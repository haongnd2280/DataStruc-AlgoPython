class Empty(Exception):
	"""Error attempting to access an element from an empty container."""
	pass


class ArrayStack:
	"""LIFO Stack implementation using a Python list as underlying storage."""
	
	def __init__(self):
		"""Create an empty stack."""
		self._data = []                # nonpublic list instance

	def __len__(self):
		"""Return the number of elements in the stack."""
		return len(self._data)

	def is_empty(self):
		"""Return True if the stack is empty."""
		return len(self._data) == 0

	def push(self, e):
		"""Add element e to the top of the stack."""
		self._data.append(e)           # new item stored at the end of list

	def top(self):
		"""Return (but not remove) the element at the top of the stack.

		Raise Empty exception if the stack is empty.
		"""
		if self.is_empty():
			raise Empty('Stack is empty.')
		return self._data[-1]          # the last item in the list.

	def pop(self):
		"""Remove and return the element from the top of the stack (i.e, LIFO).

		Raise Empty exception if the stack is empty.
		"""
		if self.is_empty():
			raise Empty('Stack is empty.')
		return self._data.pop()         # remove last item from list.


def reverse_file(filename):
	"""Overwrite given file with its contents line-by-line reversed."""
	S = ArrayStack()
	original = open(filename)
	for line in original:
		S.push(line.rstrip('\n'))  # we will re-insert newlines when writing
	original.close()

	# now we overwrite with contents in LIFO order.
	output = open(filename, 'w')  # reopening file overwrites original
	while not S.is_empty():
		output.write(S.pop() + '\n')  # re-insert newline characters
	output.close()


if __name__ == '__main__':
	filename1 = "C:\\Users\\admin\\OneDrive\\Documents\\DataStruc&AlgoPython\\reverse_file.txt"
	file = open(filename1, 'w')
	file.write('Hello')
	file.write('World\n')
	file.write('My name is: ')
	file.write('Hao Nguyen\n')
	file.write('Nice to meet you!')
	file.close()

	reverse_file(filename1)
