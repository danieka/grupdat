# Feel free to extend this program as an exercise. Some suggestions:
# Change __eq__ so it's mathematically correct. Right now 5/5 != 2/2, which is bad.
# Add some more arithmetic operators. More on what the operatiors should be name can be found on: https://docs.python.org/2/library/operator.html

class Rational:
	""" A simple class representing a rational number. 

	Only supports adding and eqaulity checking."""
	def __init__(self, numerator, denominator):
		self.num = numerator
		self.den = denominator

	def __repr__(self):
		return "%d/%d" % (self.num, self.den) 	# This stuff is called string formatting, and it's a bit more fancy so only pay attention
												# if you want to.

	def __add__(self, other):
		"""This method adds either two Rationals or one Rational and one Int"""
		if type(other) == int:
			return Rational(self.num + other*self.den, self.den)
		else:
			return Rational(self.num*other.den + other.num*self.den, self.den*other.den)

	def __eq__(self, other):
		""" Compares the two rational numbers and returns true if equal. """
		return self.num == other.num and self.den == other.den

a = [Rational(2, 5), Rational(3,5), Rational(4,5)]
print(Rational(2, 5) + Rational(3,5))
print(Rational(2, 5).__add__(Rational(3,5)))

a = Rational(2, 5)
b = Rational(2, 5)
a == b #This will return True since both a and b have the value 2/5
a is b #This will return False since a and b are different objects

d = Rational(2, 5)
c = d
d is c #Will return true since they are the same object
c.num = 5
print(d.num) #This will print 5, when changing c d was also changed since they are the same object.