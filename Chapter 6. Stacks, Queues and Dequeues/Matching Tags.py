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


def is_matched_html(raw):
	"""Return True if all HTML tags are properly matched; False otherwise."""
	S = ArrayStack()
	j = raw.find('<')                   # find first '<' character (if any)
	while j != -1:
		k = raw.find('>', j + 1)        # find next '>' character
		if k == -1:                     # no '>' character exists
			return False                # invalid tag

		tag = raw[j + 1:k]              # strip away < >
		if not tag.startswith('/'):     # this is opening tag
			S.push(tag)
		else:                           # this is closing tag
			if S.is_empty():
				return False            # nothing to match with
			elif tag[1:] != S.pop():    # remove '/' character
				return False            # mismatched delimiter

		j = raw.find('<', k + 1)        # find next '<' character (if any)

	return S.is_empty()


if __name__ == '__main__':
	string = '<body> <center> <h1> </h1> </center> <p> </p> </body>'
	print(is_matched_html(string))