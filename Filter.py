import random as rand

a = []

for i in range(10) :

	a.append(rand.randrange(1,101,1))

print(a)

for i in range(0, len(a)) :

	print (i)

	print(a[0])

	if (a[i] % a[0]) == 0 :

		a[i] = 0

print(a)