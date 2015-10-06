#Detta var koden vi skrev på övningen ht-15
#En annan version finns i split_words14

s = "hej då ett ord till"

def split(s):
	for pos in range(len(s)):
		if s[pos] == " ":
			for pos2 in range(pos+1, len(s)):
				if s[pos2] == " ":
					print(s[pos+1:pos2])
					break

split(" " + s + " ")