a = 1

b = 1

fibb = 1

fib = []

count = 0

while count < 50 :

	if (fibb % 2) != 0 :

		fib.append(fibb)

		count = count + 1

	fibb = a + b

	b = a

	a = fibb

print(fib)