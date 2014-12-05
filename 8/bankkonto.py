# Feel free to extend this program as an exercise. Some suggestions:
# Implement transfering money between accounts
# Implement a class Owner that can have several Accounts and every Account has an Owner
# Implement some checks to make sure the user enters a valid account

class Account:
	""" A simple class representing an account. 

	Implements withdraw, balance and insert. Notice that all methods have the self parameter. 
	But this self parameter is automatically added by Python when calling."""
	def __init__(self, owner, balance):
		""" The __init__ method is the objects constructor, which is called when the object is created.
		In this method we do all the setup that needs to be done. In this case we initialize the account
		by assigning it to an owner and setting the initial balance. """
		self.owner = owner # Here we set the attribute self.owner to the parameter owner
		self.bal = balance #The keyword self refers to the own object. So when we write self.bal we mean "set my balance"

	def __repr__(self):
		"""__repr__ is a special method that is used by Python when we want to print this object.

		So when we write print(ett_konto) this method will be called. The underscores in front of and after repr
		indicates that this method is a "magic" object. That means that it is used internally by Python.
		We should never use double underscores for our own methods."""
		return "Kontot ägs av: " + self.owner + " och hen har: " + str(self.balance) + "kr"

	def withdraw(self, amount):
		""" This methods withdraws amount from the account. Returns true if withdraw succeds, else returns false.
		If withdraw fails no money is withdraw.

		The method will fail if the amount is bigger than the balance on the account or if the amount is negative."""
		if self.bal >= amount and self.bal => 0:  	# We need to check that the client has sufficient money and that the sum to be withdrawn
			self.bal -= amount						# is positive
			return True
		else:
			return False

	def insert(self, amount):
		""" This method inserts amount to account. Will fail if amount is negative."""
		if self.bal >= 0:
			self.bal += amount
			return True
		else:
			return False

	def balance(self):
		"""Simply return the balance on the account"""
		return self.bal


accounts = {} 	#For easy lookup we save the accounts in a dictionary
while True:
	operation = int(input("1 för nytt konto, 2 för sätta in, 3 för ta ut, 4 för utskrift:"))
	if operation == 1:
		name = input("Namn: ")
		amount = int(input("Balans:"))
		accounts[name] = Account(name, amount)
	else if operation == 2:
		account = input("Vilket konto? ")
		amount = int(input("Summa att sätta in: "))
		accounts[account].insert(amount)		# This operation will fail if the account does not exist
	else if operation == 3:
		account = input("Vilket konto? ")       # account and Account names do not clash because Python is case-sensitive
		amount = int(input("Summa ta ut: "))
		accounts[account].withdraw(amount)
	else if operation == 4:
		account = input("Vilket konto? ")
		print(accounts[account])




