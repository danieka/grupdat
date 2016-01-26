class Hashtabell:
	# En enkel hashtabell med linjär probning
	def __init__(self, size):
		#När man skapar tabellen ska man ange önskad storlek
		self.size = size
		self.table = [None] * size #Skapar en tom lista med size antal None-element.

	def put(self, key, value):
		#Stoppar in ett (key, value) par i tabellen
		h = hash(key) 	#Vi använder pythons inbyggda hashfunktion för att få en position
						#Den positionen tar vi sedan modulo tabellens storlek för att garantera att positionen är inom tabellens utrymme
		while self.table[h%self.size] != None:  #Vi loopar tills dess att vi hittar en ledig plats
			h += 1 								#Eftersom vi använder linjär probning stegar vi fram en position i taget
		self.table[h%self.size] = (key, value)  #Vi stoppar in både key och value i tabellen. Key behöver vi vid get-operationen

	def get(self, key):
		#Hämtar ut värdet kopplat till key
		h = hash(key)
		while self.table[h%self.size][0] != key: #Nu loopar vi tills dess att vi hittar rätt (key, value) par
			h += 1
		return self.table[h%self.size][1] #Returnera value


tabell = Hashtabell(1500000) #Tabeller bör vara 50% större än antalet poster
with open("personer.txt") as f:
	for line in f.readlines():
		pnr = line.split(";")[0]
		name = line.split(";")[1].strip() #Strip tar bort nyradstecken som vi annars får med.
		tabell.put(pnr, name)

while True:
	pnr = input("Skriv in ett personnummer: ")
	print(tabell.get(pnr))