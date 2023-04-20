import collections


D = collections.deque
D.append(5)
D.append(3)
print(len(D))
print(D.pop())
print(D.pop())
D.appendleft(6)
D.appendleft(2)
print(D[2])
