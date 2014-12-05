







class Konto:
	def __init__(self, owner, balance):
		self.owner = owner
		self.balance = balance

	def __repr__(self):
		return "Kontot ägs av: " + self.owner + " och hen har: " + str(self.balance) + "kr"

	def withdraw(self, amount):
		if self.balance >= amount:
			self.balance -= amount
			return True
		else:
			return False

	def add(self, amount):
		self.balance += amount
		return True

konton = {}
while True:
	operation = int(input("1 för nytt konto, 2 för sätta in, 3 för ta ut, 4 för utskrift:"))
	if operation == 1:
		name = input("Namn: ")
		amount = int(input("Balans:"))
		konton[name] = Konto(name, amount)
	if operation == 3:
		account = input("Vilket konto? ")
		amount = int(input("Summa ta ut:"))
		konton[account].withdraw(amount)
	print(konton)

#daniels_konto = Konto("Daniel", 100)
#print(daniels_konto)
#daniels_konto.withdraw()




