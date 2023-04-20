class Empty(Exception): 
    pass


class _DoublyLinkedBase: 
    """A base class providing a doubly linked list representation."""

    class _Node: 
        """Lightweight, nonpublic class for storing a doubly linked list."""
        __slots__ = '_element', '_prev', '_next'              # streamline memory 

        def __init__(self, element, prev, next):              # initialize node's fields
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self): 
        """Create an empty list."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer                    # trailer is after header 
        self._trailer._prev = self._header                    # header is before trailer 
        self._size = 0                                        # number of elements

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size 

    def is_empty(self):
        """Return True if the list is empty."""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor)         # linked to neighbors
        predecessor._next = newest
        successor._prev = newest               
        self._size += 1                
        return newest   

    def _delete_node(self, node): 
        """Delete non-sentinel node from the list and return its element."""
        predecessor = node._prev
        successor = node._next 
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1

        element = node._element                                # record deleted element 
        node._prev = node._next = node._element = None         # deprecate node 
        return element                                         # return deleted element 


class PositionalList(_DoublyLinkedBase): 
    """A sequential container of elements allowing positional access."""

    #--------------------------- nested Positon class ---------------------------
    class Position: 
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node): 
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self): 
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other): 
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node  

        def __ne__(self, other):    # this method is based on the __eq__ method
            """Return True if other does not represent the same location."""
            return not (self == other)

        #----------------------- utility methods -----------------------------
        def _validate(self, p): 
            """Return position's node, or raise appropriate error if invalid."""
            if not isinstance(p, self.Position): 
                raise TypeError('p must be proper Position type.')
            if p._container is not self: 
                raise ValueError('p does not belong to this container.')
            if p._node._next is None:                        # convention for deprecated nodes
                raise ValueError('p is no longer valid.')
            
            return p._node

        def _make_position(self, node): 
            """Return Position instance for given node (or None if sentinel)."""
            if node is self._header or node is self._trailer: 
                return None                                  # boundary violation 
            else: 
                return self.Position(self, node)             # legitimate position

        #----------------------- accessors -----------------------------------
        def first(self): 
            """Return the first Position in the list (or None if list is empty)."""
            return self._make_position(self._header._next)

        def last(self): 
            """Return the last Position in the list (or None if list is empty)."""
            return self._make_position(self._trailer._prev)
