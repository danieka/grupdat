




class Rational(object):
	def __init__(self, numerator, denominator):
		self.numerator = int(numerator)
		self.denominator = int(denominator)

	def __repr__(self):
		return "%d/%d" % (self.numerator, self.denominator)

	def __add__(self, b):
		return Rational(self.numerator*b.denominator + b.numerator*self.denominator, self.denominator*self.denominator)


r = [Rational(2, 5), Rational(2,5)]

print(r[0] + r[1])