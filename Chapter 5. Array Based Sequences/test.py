import time 

data = list(range(10000000))

start = time.time()
print(5 in data)
end = time.time()
print('time for "5 in data": {}'.format(end - start))

start = time.time()
print(9999995 in data)
end = time.time()
print('time for "9999995 in data": {}'.format(end - start))

start = time.time()
print(-5 in data)
end = time.time()
print('time for "-5 in data": {}'.format(end - start))
