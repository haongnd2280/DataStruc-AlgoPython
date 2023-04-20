class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d): 
        """Create d-dimensional vector of zeros."""
        self._coords = [0] * d 

    def __len__(self):                # non-operator overloading 
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):         # non-operator overloading 
        """Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):    # non-operator overloading  
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):         # operator overloading + polymorphism 
        """Return sum of two vectors."""
        if len(self) != len(other):   # relies on __len__ method
            raise ValueError('Dimension must agree.')

        result = Vector(len(self))    # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]     # relies on __getitem__ method
        return result

    def __eq__(self, other):          # operator overloading
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords   # compare two lists

    def __ne__(self, other):          # operator overloading
        """Return True if vector differs from other."""
        return not self == other               # relies on existing __eq__ definition

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'    # adapt list representation


if __name__ == '__main__':
    v = Vector(5)
    v[1] = 23
    v[-1] = 45
    print(v[1])
    print(v[-1])
    print(v[4])
    u = v + v
    print(u)

    total = 0
    for entry in v:         # implicit iteration via __len__ and __getitem__
        total += entry
