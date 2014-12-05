def triangel_bas_upp(dist, bredd):
	if bredd <= 0:
		return
	print(' '*(dist), '*'*bredd)
	triangel_bas_upp(dist+1, bredd-2)

def triangel_bas_ner(dist, bredd):
	if bredd <= 0:
		return
	triangel_bas_ner(dist+1, bredd -2)
	print(' '*(dist), '*'*bredd)

triangel_bas_ner(5, 5)
triangel_bas_upp(5, 5)