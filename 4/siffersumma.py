
def siffersumma(t):
    if t==0:
        return 0
    return siffersumma(t//10) + t%10

print(siffersumma(123))