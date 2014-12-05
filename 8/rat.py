



class Rational:
	def __init__(self, numerator, denominator):
		self.num = numerator
		self.den = denominator

	def __repr__(self):
		return "%d/%d" % (self.num, self.den)

	def __add__(self, other):
		if type(other) == int:
			return Rational(self.num + other*self.den, self.den)
		else:
			return Rational(self.num*other.den + other.num*self.den, self.den*other.den)

	def __eq__(self, other):
		return self.num == other.num and self.den == other.den

a = [Rational(2, 5), Rational(3,5), Rational(4,5)]
print(Rational(2, 5) + Rational(3,5))
print(Rational(2, 5).__add__(Rational(3,5)))

a = Rational(2, 5)
b = Rational(2, 5)

d = Rational(2, 5)
c = d
c.num = 5