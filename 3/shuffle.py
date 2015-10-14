import random

def shuffle(l):
	res = []
	for i in range(len(l)):
		pos = random.randint(0, len(l) - 1)
		res.append(l.pop(pos))
	return res

l = [1,2,3,4,5,6,7,8,9]
print(shuffle(l))
print(l)

print("Pythons random:")
l2 = [1,2,3,4,5,6,7,8,9]
print(random.shuffle(l2))
print(l2)