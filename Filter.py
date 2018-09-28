import random as rand

a = []

for i in range(10) :

	a.append(rand.randrange(1,101,1))

print(a)

for i in range(0, len(a) - 1) :


	if (int(a[i+1]) % int(a[0])) == 0 :

		a[i + 1] = 0

print(a)