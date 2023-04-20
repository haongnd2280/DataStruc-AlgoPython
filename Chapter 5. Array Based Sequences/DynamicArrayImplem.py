import ctypes                                           # provide low-level arrays
import sys


class DynamicArray:
	"""A dynamic array class akin to to simplified Python list."""

	def __init__(self): 
		"""Create an empty array."""
		self._n = 0                                     # count actual elements 
		self._capacity = 1                              # default array capacity 
		self._A = self._make_array(self._capacity)      # low-level array 

	def __len__(self):    # non-operator overloading 
		"""Return number of elements stored in the array."""
		return self._n

	def __getitem__(self, k): 
		"""Return element at index k."""
		if not 0 <= k < self._n: 
			raise IndexError('invalid index.')
		
		return self._A[k]                               # retrieve from array (via __getitem__)

	def append(self, obj):
		"""Add object to end of the array."""
		if self._n == self._capacity:                   # not enough cell
			self._resize(2 * self._capacity)            # so double capacity
		self._A[self._n] = obj
		self._n += 1

	def _resize(self, c):                               # nonpublic utility
		"""Resize internal array to capacity c."""
		B = self._make_array(c)                         # new (bigger) array
		for k in range(self._n):                        # for each existing value
			B[k] = self._A[k]

		self._A = B                                     # use the bigger array
		self._capacity = c

	def _make_array(self, c):                           # nonpublic utility
		"""Return new array with capacity c."""
		return (c * ctypes.py_object)()                 # see ctypes documentation

	def insert(self, k, value): 
		"""Insert value at index k, shifting subsequent values rightward."""
		# (for simplicity, we assume 0 <= k < n in this version)	
		if self._n == self._capacity:                   # not enough room
			self._resize(2 * self._capacity)            # so double capacity 
		
		for j in range(self._n, k, -1):                 # shift rightmost first 
			self._A[j] = self._A[j - 1]
		
		self._A[k] = value                              # store newest element 
		self._n += 1

	def remove(self, value): 
		"""Remove first occurrence of value (or raise ValueError)."""
		# note: we do not consider shrinking the dynamic array in this version.
		for k in range(self._n):
			if self._A[k] == value:                     # found a match!
				for j in range(k, self._n - 1):         # shift others to fill gap 
					self._A[j] = self._A[j + 1]
				
				self._A[self._n - 1] = None             # help garbage collection
				self._n -= 1                            # we have one less item 
				return                                  # exit immediately
			
		raise ValueError('value not found.')            # only reached if no match

	def show_capacity(self):
		"""Return the current capacity of the array."""
		return self._capacity

if __name__ == '__main__':
	DArray1 = DynamicArray()
	for i in range(1000):
		a = len(DArray1)               # number of elements
		b = DArray1.show_capacity()    # actual size in byes

		print('Length: {0:3d}; Current capacity: {1:4d}'.format(a, b))
		DArray1.append(None)

	# for i in range(100):
	# 	print('A[{0}] = {1}'.format(i, DArray1[i]))




