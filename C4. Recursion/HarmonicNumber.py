def GCD(a, b):
	if b == 0:
		return a
	else:
		return GCD(b, a % b)


class Fraction():
	def __init__(self, numerator=1, denominator=1):
		self.numerator = numerator
		self.denominator = denominator

	def __add__(self, other):
		"""This method adds two non-negative fractions and reduces the result."""
		result = Fraction(1, 1)
		result.numerator = self.numerator * other.denominator + other.numerator * self.denominator
		result.denominator = self.denominator * other.denominator

		# reduce the result
		if result.numerator > result.denominator:
			gcd = GCD(result.numerator, result.denominator)
		else:
			gcd = GCD(result.denominator, result.numerator)

		if gcd > 1:
			result.numerator = result.numerator // gcd
			result.denominator = result.denominator // gcd

		return result


def harmonic_number(n):
	"""This function computes the nth Harmonic number."""
	if n == 1:
		return Fraction()
	else:
		return Fraction(1, n) + harmonic_number(n - 1)


if __name__ == '__main__':
	n = 5
	result = harmonic_number(n)
	print("{0}th harmonic number = {1}/{2}".format(n, result.numerator, result.denominator))
