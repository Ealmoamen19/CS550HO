import random as r

import sys

number = int(sys.argv[1])

def simNoSwitch () :

	hiddenCwap = [1, 2, 3]

	choice = r.randint(1, 3)

	userChoice = r.randint(1, 3)

	while True :

		x = r.randint(1, 3)

		if x != choice and x != userChoice :

			break

	hiddenCwap.remove(x)

	if choice == userChoice :

		return True

	else :

		return False

def simSwitch () :

	hiddenCwap = [1, 2, 3]

	choice = r.randint(1, 3)

	userChoice = r.randint(1, 3)

	while True :

		x = r.randint(1, 3)

		if x != choice and x != userChoice :

			break

	hiddenCwap.remove(x)

	if userChoice == hiddenCwap[0] :

		userChoice = hiddenCwap[1]

	else :

		userChoice = hiddenCwap[0]

	if choice == userChoice :

		return True

	else :

		return False

success = 0

failure = 0

for i in range (number) :

	test = simNoSwitch()

	if test == False :

		failure += 1 

	elif test == True :

		success += 1

print("\n\n-- No Switch Simulation --")

print("Success: " + str(success))

print("Success Rate: " + str((success/(success + failure)) * 100) + "%")

print("Failure: " + str(failure))

print("Failure Rate: " + str((failure/(success + failure)) * 100) + "%\n\n")

success = 0

failure = 0

for i in range (number) :

	test = simSwitch()

	if test == False :

		failure += 1 

	elif test == True :

		success += 1

print("-- Switch Simulation --")

print("Success: " + str(success))

print("Success Rate: " + str((success/(success + failure)) * 100) + "%")

print("Failure: " + str(failure))

print("Failure Rate: " + str((failure/(success + failure)) * 100) + "%\n\n")

#The results for not switching gives a 33% success rate and the results for switching give a 66% success rate. 
#The reason behind this is that you are 33% likely to pick the right door in the beginning. But if one option is eliminated and you switch, 
#statistically speaking, the number of arrangements in which you are switching to the right door is 66% of all arrangements.




