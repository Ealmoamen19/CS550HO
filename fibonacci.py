a = 1

b = 1

ins = int(input())

for i in range(ins) :

	fibb = a + b

	b = a

	a = fibb

	print(fibb)
