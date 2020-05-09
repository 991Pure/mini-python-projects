import random

symbols = "!1@2#3$4%5^6&7*8(9)0-_=+qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlL;:'z"
symbols += "xXcCvVbBnNmM,<.>/?"
symbols = list(symbols) 

print(len(symbols))

print(symbols[73])

how_long = input("Enter number of characters you want in your password: ")
how_long = int(how_long)
password = []

while len(password) <= how_long:
	z = 83
	x = random.randint(0,z)
	z = z - 1
	y = symbols[x]
	password.append(y)
	print(password)


final_password = "".join(password)
print(final_password)


# zrobic dodatkowa liste i tam umieszczac wylosowane liczby
# i jesli wylosujemy drugi raz tą samą to nie dziala!