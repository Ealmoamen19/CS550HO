import sys

count = 0

i = 1

num = int(sys.argv[1])

while count < 100 :

	if i % num == 0 :

		count = count + 1

		print(i)

	i = i + 1