import time


def power1(x, n):
	"""Compute the value x**n for integer n."""
	if n == 0: 
		return 1
	else: 
		return x * power1(x, n - 1)


def power2(x, n): 
	"""Compute the value x**n for integer n."""
	if n == 0: 
		return 1
	else: 
		partial = power2(x, n // 2)         # rely on truncated division 
		result = partial * partial 
		if n % 2 == 1:                      # if n is odd, include extra factor of x 
			result *= x 
		
		return result    


if __name__=='__main__':
	start = time.time()
	x = power1(2, 30)
	end = time.time()
	print("Time for power1: {}".format(end - start))
	start = time.time()
	y = power2(2, 30)
	end = time.time()
	print("Time for power2: {}".format(end - start))
	print("Power1 = ", x)
	print("Power2 = ", y)
