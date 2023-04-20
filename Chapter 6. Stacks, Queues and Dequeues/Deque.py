class Empty(Exception):
	"""Error attempting to access an element from an empty container."""
	pass


class ArrayDeque():
	"""Double-end queue implementation using a Python list as underlying storage."""
	DEFAULT_CAPACITY = 10  # moderate capacity for all new queues. (constant)

	def __init__(self):
		"""Create an empty queue."""
		self._data = [None] * ArrayDeque.DEFAULT_CAPACITY  # reference to a list instance with fixed capacity.
		self._size = 0  # current number of elements stored in the double-end queue
		self._front = 0  # integer representing the index of the first element in double-end queue.

	def __len__(self):  # Done
		"""Return the number of elements in the double-end queues."""
		return self._size

	def is_empty(self):  # Done
		"""Return True if the double-end queue is empty."""
		return self._size == 0

	def first(self):  # Done
		"""Return (but do not remove) the element at the front of the double-end queue.

		Raise Empty exception if the double-end queue is empty.
		"""
		if self.is_empty():
			raise Empty('Double-end queue is empty.')
		return self._data[self._front]

	def last(self):
		"""Return (but do not remove) the element at the back of the double-end queue."""
		if self.is_empty():
			raise Empty('Double-end queue is empty.')
		back = (self._front + self._size - 1) % len(self._data)
		return self._data[back]

	def add_first(self, e):
		"""Add an element to the front of the double-end queue."""
		if self._size == len(self._data):
			self._resize(2 * len(self._data))  # double the aray size

		avail = (self._front - 1) % len(self._data)
		self._data[avail] = e
		self._front = avail
		self._size += 1

	def add_last(self, e):  # Done
		"""Add an element to the back of the double-end  queue."""
		if self._size == len(self._data):
			self._resize(2 * len(self._data))  # double the array size

		avail = (self._front + self._size) % len(self._data)  # index of the new element e
		self._data[avail] = e
		self._size += 1

	def delete_first(self):  # Done
		"""Remove and return the first element of the double-end queue (i.e, FIFO).

		Raise Empty exception if the double-end queue is empty.
		"""
		if self.is_empty():
			raise Empty('Queue is empty.')

		answer = self._data[self._front]
		self._data[self._front] = None  # help garbage collection
		self._front = (self._front + 1) % len(self._data)  # update front variable (incrementing)
		self._size -= 1

		if 0 < self._size < len(self._data) // 4:
			self._resize(len(self._data) // 2)

		return answer

	def delete_last(self):
		"""Remove and return the last element of the double-end queue.

		Raise Empty exception if the double-end queue is empty.
		"""
		if self.is_empty():
			raise Empty('Queue is empty.')

		back = (self._front + self._size - 1) % len(self._data)
		answer = self._data[back]
		self._data[back] = None                     # help garbage collection
		self._size -= 1

		if 0 < self._size < len(self._data) // 4:
			self._resize(len(self._data) // 2)

		return answer

	def _resize(self, cap):  # we assume cap >= len(self) Done (also work well with cap < len(self))
		"""Resize to a new list of capacity >= len(self)."""
		old = self._data  # keep track of existing list.
		self._data = [None] * cap  # allocate list with new capacity.
		walk = self._front

		for k in range(self._size):  # only consider existing elements
			self._data[k] = old[walk]  # intentionally shift indices
			walk = (walk + 1) % len(old)  # use old size as modulus
		self._front = 0  # front has been realigned


if __name__ == '__main__':
	D = ArrayDeque()
	D.add_last(5)
	D.add_first(3)
	D.add_first(7)
	print(D.first())
	print(D.delete_last())
	print(len(D))
	print(D.delete_last())
	print(D.delete_last())
	D.add_first(6)
	print(D.last())
	D.add_first(8)
	print(D.is_empty())
	print(D.last())

