from PIL import Image

import math


xcoor = 1024.0

ycoor = 1024.0

zcoor = 1024.0

xRange = [-1, 1]

yRange = [-1, 1]

zRange = [-1, 1]

count = 0

image = Image.new("RGB", (int(xcoor), int(ycoor)))

def melbourne(z, c) :

	global count 

	r = math.sqrt(((z[0]**2) + (z[1]**2) + (z[2]**2)))

	theta = math.atan(math.sqrt(((z[0]**2) + (z[1]**2)))/z[2])

	phi = math.atan(z[1]/z[0])

	storeVal = [0,0,0]

	storeVal[0] = (r**2) * (math.sin(2 * theta)) * (math.cos(2 * phi))

	storeVal[1] = (r**2) * (math.sin(2 * theta)) * (math.sin(2 * phi))

	storeVal[2] = (r**2) * math.cos(2 * theta)

	summation = [0,0,0]

	summation[0] = c[0] + storeVal[0]

	summation[1] = c[1] + storeVal[1]

	summation[2] = c[2] + storeVal[2]

	count += 1

	if math.sqrt((summation[0] ** 2) + (summation[1] ** 2) + (summation[2] ** 2)) <= 2 and count < 255 :


		melbourne(summation, c)


for k in range(0, int(zcoor)) :

	for i in range (0, int(xcoor)) :

		for j in range(0, int(ycoor)) :

			thingy = [i/(xcoor/(xRange[1] - xRange[0]))+ xRange[0], j/(ycoor/(xRange[1] - xRange[0])) + yRange[0], k/(zcoor/(xRange[1] - xRange[0])) + yRange[0]]

			print(thingy)

			count = 0

			melbourne([1,1,1], thingy)

			print(count)

			color = count % 4

			coordinate = i, j

			if image.getpixel(i j)[0] < 50 and image.getpixel(i j)[1] < 50 and image.getpixel(i j)[2] < 50 :

				image.putpixel((i,j),(count, 0, 0))



			


		

name = input("Save As: ")
image.save(str(name), "PNG")





