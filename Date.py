import sys 

y = int(sys.argv[1])

m = int(sys.argv[2])

d = int(sys.argv[3])

Y = y - ((14 - m)//12)

X = Y + (Y//4) - (Y//100) + (Y//400)

M = m + 12 * ((14 - m)//12) - 2

D = (d + X + (31 * M)//12) % 7

if D == 0 :

	print ("Sunday")

if D == 1 :

	print("Monday")

if D == 2 :

	print("Tuesday")

if D == 3 :

	print("Wednesday")

if D == 4 :

	print("Thursday")

if D == 5 :

	print("Friday")

if D == 6 :

	print("Saturday")
