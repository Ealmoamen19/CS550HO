import random as rand

a = []

for i in range(10) :

	a.append(rand.randrange(0,101,1))

print(a)

for i in range(len(a)) :

	z = a[i]
	
	for x in range (len(a)) :

		if (z > a[x]) and (a.index(z) < a.index(a[x])) :

			y = a[x]
			b = a.index(y)
			c = a.index(z)

			a.remove(a[x])

			a.remove(a[c])

			a.insert(y, b)

			a.insert(z, c)

		elif (z < a[x]) and (a.index(z) < a.index(a[x])) :

			y = a[x]
			b = a.index(y)
			c = a.index(z)

			a.remove(a[x])

			a.remove(a[c])

			a.insert(y, b)

			a.insert(z, c)

		print(a)

print(a)


