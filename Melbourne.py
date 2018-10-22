from PIL import Image

import math

xcoor = 1024.0

ycoor = 1024.0

xRange = [-2, 2]

yRange = [-2, 2]

count = 0

image = Image.new("RGB", (int(xcoor), int(ycoor)))

def melbourne(z, c) :

	global count 

	storeVal = [0,0]

	storeVal[0] = ((z[0] ** 2) - (z[1] ** 2))

	storeVal[1] = (2 * z[0] * z[1])

	summation = [0,0]

	summation[0] = c[0] + storeVal[0]

	summation[1] = c[1] + storeVal[1]

	count += 1

	if math.sqrt((summation[0] ** 2) + (summation[1] ** 2)) <= 2 and count < 255 :


		melbourne(summation, c)


for i in range(0, int(xcoor)) :

	for j in range (0, int(ycoor)) :

		thingy = [i/(xcoor/(xRange[1] - xRange[0]))+ xRange[0], j/(ycoor/(xRange[1] - xRange[0])) + yRange[0]]

		print(thingy)

		count = 0

		melbourne([0,0], thingy)

		print(count)

		color = count % 4

		if color == 1:

			image.putpixel((i,j),(155, 0, 0))

		elif color == 2:

			image.putpixel((i,j),(100, 0, 0))

		elif color == 3:

			image.putpixel((i,j),(55, 0, 0))

		else :

			image.putpixel((i,j),(255, 0, 0))

name = input("Save As: ")
image.save(str(name), "PNG")





