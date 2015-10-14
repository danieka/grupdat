def split(s):
	word_start = 0
	for i in range(0, len(s), 1):
		if s[i] == " ":
			print(s[word_start:i+1])
			word_start = i +1
	print(s[word_start:])