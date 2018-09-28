import random as rand

a = []

count = 0

i = 1

while count < 3000 :

	if (2 * i) % 6 != 0 :

		a.append(2 * i)

		count = count + 1

	if (3 * i) % 6 != 0 :

		a.append(3 * i)

		count = count + 1

	i = i + 1

print(a)