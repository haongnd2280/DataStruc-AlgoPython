from typing import MutableMapping


class MapBase(MutableMapping): 
    """Our own abstract base class that includes a nonpublic _Item class."""

    # -------------------------- nested _Item class --------------------------------
    class _Item: 
        """Lightweight composite to store key-value pairs as map items."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v): 
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key                 # compare items based on their keys

        def __ne__(self, other):
            return not (self == other)                     # opposite of __eq__

        def __lt__(self, other): 
            return self._key < other._key                  # compare items based on their keys 

    
class UnsortedTableMap(MapBase):
    """Map implementation using an unordered list."""

    def __init__(self): 
        """Create an empty map."""
        self._table = []                                   # list of _Item's (abstract type)

    def __getitem__(self, k): 
        """Return value associated with key k (raise KeyError if not found)."""
        for item in self._table:                           # item is _Item object
            if k == item._key:                             
                return item._value                            
        raise KeyError('Key Error: ' + repr(k))

    def __setitem__(self, k, v): 
        """Assign value v to key k, overwriting existing value if present."""
        for item in self._table:                           # item is _Item object, stored in table
            if k == item._key:                             # found a match (for key): 
                item._value = v                            # reassign value 
                return                                     # and quit
        # did not find match for key
        self._table.append(self._Item(k, v))               # use Inheritance from MapBase class

    def __delitem__(self, k): 
        """Remove item associated with key k (raise KeyError if not found)."""
        for j in range(len(self._table)):                  # need index j to used pop method of list
            if k == self._table[j]._key:                   # found a match: 
                self._table.pop(j)                         # remove _Item object of index j
                return                                     # and quit
        raise KeyError('Key Error: ' + repr(k))

    def __len__(self): 
        """Return number of items in the map."""
        return len(self._table)

    def __iter__(self):                                    # create generator
        """Generate iteration of the map's keys."""
        for item in self._table:                           # item is _Item instance
            yield item._key                                # yield the KEY


if __name__ == '__main__':
    Map = UnsortedTableMap()
    print(len(Map))
    Map['K'] = 2 
    Map['B'] = 4
    Map['U'] = 2
    Map['V'] = 8 
    Map['K'] = 9 
    print(Map['B'])
    # print(Map['X'])
    print(Map.get('F'))              # concrete method from MutableMapping class
    print(Map.get('F', 5))
    print(Map.get('K', 5))
    print(len(Map))
    del Map['V']
    print(Map.pop('K'))              # concrete method from MutableMapping class
    print(Map.keys())                # concrete method from MutableMapping class 
    print(Map.values())
    print(Map.items())
    print(Map.setdefault('B', 1))
    print(Map.setdefault('A', 1))
    print(Map.popitem())





    


         
