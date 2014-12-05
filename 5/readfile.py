def our_split(string, split_by):
	l = []
	last = 0 
	for i, letter in enumerate(string):
		if letter == split_by:
			l.append(string[last:i])
			last = i
	l.append(string[last:])
	return l


#with open("inp.txt") as f:
#	l = f.read().split()
#	our_split(l, "?")

print(our_split("sen?EAO", "?"))