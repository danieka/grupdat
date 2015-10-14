def longest(s):
	words = s.split()
	longest_word = ""
	for word in words:
		if len(word) > len(longest_word):
			longest_word = word
	return longest_word

with open("/home/daniel/Code/grupdat/3/dikt.txt") as f:
	s = f.read()
	print(longest(s))
print("Nu filer stängd")