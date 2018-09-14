import sys

import random as rand

x = rand.random()

if (x > 0.7) :

	print("It's nice and Sunny outside")

elif (x > 0.5) :

  	print("It's raining outside")

elif (x > 0.2) :

	print("There's a hurricane! You gotta get to a shelter.")

elif (x <= 0.2) :

	print("It's scorching HOT")