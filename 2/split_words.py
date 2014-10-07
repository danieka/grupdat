def split_words_and_reverse(s):
	word_start = len(s)
	for i in range(len(s)-1, 0, -1):
		if s[i] == " ":
			print(s[i+1:word_start])
			word_start = i
	print(s[:word_start])

def split_words(s):
	word_start = 0
	for i in range(0, len(s), 1):
		if s[i] == " ":
			print(s[word_start:i+1])
			word_start = i +1
	print(s[word_start:])

s = "Detta var en väldigt regnig dag :("
print("Först delar vi upp orden i vanlig ordning\n")
split_words(s)
print("\n\n")
print("Nu delar vi orden men vänder på ordningen")
split_words_and_reverse(s)