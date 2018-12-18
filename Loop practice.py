#Partner1: Eyad
#Partner2: Anan

#1-
for i in range(5):
	print(i)
#2-
for i in range(5):
	print(4-i)
#3-
for i in range(10):
	print(15-i)
#4-
for i in range(10):
	print(i-5)
#5-
for i in range(25, 50, 2):
	print(i)

for i in range(25,50):
	if i%2 == 1:
		print(i)
#6-
for i in range(1,11):
	print(i**2)
#7-
#1)
x = 0
while x < 5:
	print(x)
	x += 1
#2)
x = 4
while x <= 0:
	print(x)
	x -= 1
#3)
x = 15
while x <= 5:
	print(x)
	x -= 1
#4)
x = -5
while x <= 5:
	print(x)
	x += 1
#5)
x = 25
while x < 50:
	if x%2 == 1:
 		print(x)
 	x += 1
x = 25
while x < 50:
	print(x)
	x += 2
#6)
x = 1
while x <= 10:
	print(x**2)
	x += 1

#8-
days = -1
for i in range(4, 58) :
	days += 1

#9-
numDays = 0
classmates = 5
beans = 30
while beans > 0:
	beans = beans - classmates - 2
	days += 1

#10-
for x in range(14, 20)
	daysleft = 20 - x
	print(daysleft, "until vacation!!!")
print("vacation has arrived")

#11-
num = 6
result = 1
for x in range(1, num+1)
	result = result*x

#12-

distance = 390
traveled = float(0)

while distance > traveled:

	distance -= distance - 24

	traveled += 0.25

#13-
n = 6
b = 6
x = 1
for i in range(1,b+1):
	x = x*n

#14-
alphabet = "qwetyuiopasdklzxcvbnm"
for i in range(len(alphabet)):
	print(alphabet[i])

#15-
alphabet = "qwetyuiopasdklzxcvbnm"
for i in range(len(alphabet)):
	if alphabet[i] == "a" or alphabet[i] == "e" or alphabet[i] == "i" or alphabet[i] == "o" or alphabet[i] == "u":
		print(alphabet[i],"is a vowel!")
	else:
		print(alphabet[i],"is a consonant!")

#16-

num = 1
thingy = ""
while num < 10

	for i in range (0, num) :

		thingy += str(num)

	num += 1

print(thingy)

#17-
for i in range(1,21):
	print(1/i)

#18-
summation = 0
avg = 0
for i in range(1,101):
	summation += i
avg = summation/len(range(1, 101))

#19-
n = 200
pi = 0
for i in range(n):
	pi += ((-1)**(i))/(2 * i+1)
	
pi *= 4

#20-
litter = 0
mother = 1
total = mother
for i in range(5):
	for i in range(mother):
		for i in range(12):
			litter += random.randint(1,14)

	mother += litter//2
	total += litter
	litter = 0

#21-

listrabbit = []

def loop () :
	litter = 0
	mother = 1
	total = mother
	for i in range(5):
		for i in range(mother):
			for i in range(12):
				litter += random.randint(1,14)

		mother += litter//2
		total += litter
		litter = 0

	list.append(total)

for i in (1500) :

	loop()

for x in listrabbit:
	listtotal += x

listtotal /= (len(listrabbit))


#22-

for i in range(111) :

	prn = ""

	if i % 3 == 0 :

		prn += "Coza"

	if i % 5 == 0 :

		prn += "Loza"

	if i % 7 == 0 :

		prn += "Woza"

	if i % 7 != 0 and i % 5 != 0 and i % 3 != 0 :

		prn += str(i)

	print(prn)


#23-

item = "* |  1  2  3  4  5  6  7  8  9\n-------------------------------\n"

for i in range(9) :

	item += str(i + 1) + " |"

	for j in range(9) :

		if ((i+1) * (j+1)) >= 10 :

			item += " " + str((i+1) * (j+1))

		else :

			item += "  " + str((i+1) * (j+1))

	item += "\n"

print(item)

#24-

thing = ""

for i in range(7) :

	for j in range(7) :

		if i == 0 or i == 6 :

			thing += "#"

		elif j == 0 or j == 6 :

			thing += "#"

		else:

			thing += " "

	thing += "\n"

print(thing)

thing = ""

for i in range(7) :

	for j in range(7) :

		if i == 0 or i == 6 :

			thing += "#"

		elif i == j or i == 6 - j:

			thing += "#"

		else:

			thing += " "

	thing += "\n"

print(thing)

thing = ""

for i in range(7) :

	for j in range(7) :

		if i == 0 or i == 6  or j == 0 or j == 6:

			thing += "#"

		elif i == j or i == 6 - j:

			thing += "#"

		else:

			thing += " "

	thing += "\n"

print(thing)

#25-

number = 23714

xer = False

finale = ""

ext = 0

while number != 0 or ext != 0:

	if number % 10 != 0 :

		ext += 1

		number -= 1

	else :

		finale += str(ext) + " "

		number = number / 10

		ext = 0

print(finale)












