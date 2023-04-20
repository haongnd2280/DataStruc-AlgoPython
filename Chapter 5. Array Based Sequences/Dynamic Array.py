import sys                                # provides getsizeof function

data = []
for k in range(100): 
    a = len(data)                         # number of elements
    b = sys.getsizeof(data)               # actual size in byes 

    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(None)                     # increase length by one

# Note: This program only check the size of instance variables of list + bytes devoted to the array
# (not count the bytes to store elements referenced by the list).


