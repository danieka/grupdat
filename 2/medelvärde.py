
n = int(input("Hur många tal vill du skriva in?"))
summa = 0

for x in range(n):
	inp = int(input("Ett tal: "))
	summa += inp

print(summa / n)