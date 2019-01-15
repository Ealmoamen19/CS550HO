
import random as r 

initPosition = [0,0]

blocks = 10

def randwalk () :

	direction = r.randint(1, 4)

	return direction

def exec (walk, position) :

	if walk == 1 :

		position[0] += 1

	elif walk == 2 :

		position[0] -= 1

	elif walk == 3 :

		position[1] += 1

	elif walk == 4 :

		position[1] -= 1

canGoBack = 0

count = 0

for x in range(100):

	for j in range(1000) :

		initPosition = [0,0]

		for i in range(x) :

			exec(randwalk(), initPosition)

		distance = abs(initPosition[0]) + abs(initPosition[1])

		if distance <= 4 :

			canGoBack += 1

		count += 1

	print("Distance Walked: " + str(x))

	print("Rate of Walk Back : " + str(((canGoBack/count) * 100)) + "%\n\n")

	#Monte carlo simulations are algorithms that are based on random sampling and are used to simulate real life situations. They can be used to simulate
#anything from stocks and economic changes to the likelyhood of waking up one hour earlier. What these simulations do is that they run the scenario 
#multiple times with random inputs(within a creatain specified range) and determines the statistical probabilities desired.

#Variable for number of darts hitting the circle portion
circle = 0

#Variable for number of darts hitting the outside of circle portion
nonCircle = 0

#Variable for number of darts that are going to be thrown
repetition = 1000

#For loop to repeat the simulation
for i in range(repetition) :

	# x, y position coordinates of dart impact determined randomly
	position = [(r.random() * 2) - 1, (r.random() * 2) - 1]

	# if statement checking if the coordinates lie within the circle using a circle's equation: x^2 + y^2 = 1
	# inequality is used to cover the inside of the circle: x^2 + y^2 <= 1
	if (position[0] ** 2) + (position[1] ** 2) <= 1 :

		circle += 1

	else :

		nonCircle += 1

total = circle + nonCircle

print("Circle: " + str(circle))

print("Non-Circle: " + str(nonCircle))

print("Circle Rate: " + str((circle/total) * 4))






