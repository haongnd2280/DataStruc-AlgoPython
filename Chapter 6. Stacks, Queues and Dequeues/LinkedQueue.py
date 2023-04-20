# This version can add element in the back and remove element in the front of the queue. 
# We wont remove element in the back of the queue because it will be expensive. (we have to 
# start at the front of the queue and reach the end).

class Empty(Exception): 
    pass

class LinkedQueue: 
    """FIFO queue implementation using a singly linked list for storage."""

    class _Node: 
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next): 
            self._element = element
            self._next = next         # reference to the next node
            

    def __init__(self): 
        """Create an empty queue."""
        self._head = None 
        self._tail = None 
        self._size = 0            # number of queue element.

    def __len__(self): 
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty(): 
            raise Empty('Queue is empty.')

        return self._head._element

    def dequeue(self): 
        """Remove and return the first element of the queue.
        
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty(): 
            raise Empty('Queue is empty.')

        answer = self._head._element
        self._head = self._head._next  
        self._size -= 1 
        
        if self.is_empty():               # special case as queue is empty
            self._tail = None             # removed head had been the tail 

        return answer 

    def enqueue(self, e):
        """Add an element to the back of the queue."""
        newest = self._Node(e, None)      # node will be new tail node 

        if self.is_empty():
            self._head = newest           # special case: previously empty
        else: 
            self._tail._next = newest     # update (old) tail node to reference to new node 
        self._tail = newest               # update reference to tail node
        self._size += 1


if __name__ == '__main__':
    LinkedQueue1 = LinkedQueue()
    LinkedQueue1.enqueue(5)
    LinkedQueue1.enqueue(7)
    print(len(LinkedQueue1))
    print(LinkedQueue1.__len__())  # try special method form. that works well, similar to above command.
    print(LinkedQueue1.first())
    print(LinkedQueue1.dequeue())
    print(len(LinkedQueue1))
    print(LinkedQueue1.is_empty())
    LinkedQueue1.enqueue(10)
    print(len(LinkedQueue1))
    print(LinkedQueue1.dequeue())
    print(LinkedQueue1.dequeue())
    print(LinkedQueue1.is_empty())

