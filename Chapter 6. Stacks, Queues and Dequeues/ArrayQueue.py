class Empty(Exception): 
	pass 


class ArrayQueue:
	"""FIFO queue implementation using a Python list as underlying storage."""
	DEFAULT_CAPACITY = 10      # moderate capacity for all new queues. (constant)
	
	def __init__(self):
		"""Create an empty queue."""
		self._data = [None] * ArrayQueue.DEFAULT_CAPACITY   # reference to a list instance with fixed capacity.
		self._size = 0         # current number of elements stored in the queue
		self._front = 0        # integer representing the index of the first element in queue.

	def __len__(self):   # Done
		"""Return the number of elements in the queues."""
		return self._size

	def is_empty(self):  # Done
		"""Return True if the queue is empty."""
		return self._size == 0

	def first(self):  # Done 
		"""Return (but do not remove) the element at the front of the queue.
		
		Raise Empty exception if the queue is empty.
		"""
		if self.is_empty():
			raise Empty('Queue is empty.')
		return self._data[self._front]

	def dequeue(self):   # Done 
		"""Remove and return the first element of the queue (i.e, FIFO).
		
		Raise Empty exception if the queue is empty.
		"""
		if self.is_empty():
			raise Empty('Queue is empty.')

		answer = self._data[self._front]
		self._data[self._front] = None                      # help garbage collection
		self._front = (self._front + 1) % len(self._data)   # update front variable (incrementing)
		self._size -= 1

		if 0 < self._size < len(self._data) // 4: 
			self._resize(len(self._data) // 2)

		return answer 

	def enqueue(self, e):   # Done
		"""Add an element to the back of the queue."""
		if self._size == len(self._data): 
			self._resize(2 * len(self._data))                   # double the array size 

		avail = (self._front + self._size) % len(self._data)    # index of the new element e
		self._data[avail] = e
		self._size += 1

	def _resize(self, cap):     # we assume cap >= len(self) Done (also work well with cap < len(self))
		"""Resize to a new list of capacity >= len(self).""" 
		old = self._data                   # keep track of existing list.
		self._data = [None] * cap          # allocate list with new capacity.
		walk = self._front
		
		for k in range(self._size):        # only consider existing elements
			self._data[k] = old[walk]      # intentionally shift indices 
			walk = (walk + 1) % len(old)   # use old size as modulus
		self._front = 0                    # front has been realigned 


if __name__ == '__main__':
	Q = ArrayQueue()
	Q.enqueue(5)
	Q.enqueue(3)
	print(len(Q))
	print(Q.dequeue())
	print(Q.is_empty())
	print(Q.dequeue())
	print(Q.is_empty())
	print(Q.dequeue())
	Q.enqueue(7)
	Q.enqueue(9)
	print(Q.first())
	Q.enqueue(4)
	print(len(Q))
	print(Q.dequeue())

	
	


