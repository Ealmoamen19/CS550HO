import random as rand

a = []

count = 0

while count < 100 :

	x = rand.randrange(1, 1001, 1)

	if x % 2 == 0 :

		a.append(x)

		count = count + 1

print(a)

