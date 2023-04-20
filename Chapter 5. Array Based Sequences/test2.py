data1 = ([0] * 6) * 3
print('data1')
print(data1)

data2 = [[0] * 6] * 3   # all three entries of data2 reference to the same instance
print('data2')
print(data2)
data2[2][0] = 100
print(data2)

# this is true: we must ensure that each cell of the primary (outer) list
# refers to an INDEPENDENT INSTANCE of a secondary list.
data3 = [[0] * 6 for j in range(3)]   # comprehension syntax
print('data3')
print(data3)
data3[2][0] = 100
print(data3)
