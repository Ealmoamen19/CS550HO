from PIL import Image

import math

xcoor = 1024.0

ycoor = 1024.0

xRange = [-0.4324595133463542, -0.4109293619791667]

xRange2 = [-0.3441721598307292, -0.3412628173828125]

yRange = [0.58946126302084,  0.6114247639973959]

yRange2 = [0.613800048828125, 0.6167093912760416]

count = 0

image = Image.new("RGBA", (int(xcoor), int(ycoor)))

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

def imagery(xRange, yRange) :

	global xcoor

	global ycoor

	global count

	for i in range(0, int(xcoor)) :

		for j in range (0, int(ycoor)) :

			thingy = [i/(xcoor/(xRange[1] - xRange[0]))+ xRange[0], j/(ycoor/(xRange[1] - xRange[0])) + yRange[0]]

			print(thingy)

			count = 0

			melbourne([0,0], thingy)

			print(count)

			color = count % 4

			
			if color == 0 :

			# 	image.putpixel((i,j),(count % 255 , 40, 170 - i//7 , 255))

				image.putpixel((i,j),(i//4 , 53, j//4 , 255))

			elif color == 1:

			# 	image.putpixel((i,j),( 229, 33, count % 255, 255))
			# 	if j >= 514:
			# 		image.putpixel((i,j),(0,0,0, abs(j - 769)))

			# 	else:
			# 		image.putpixel((i,j),(0,0,0, abs(j - 259)))

				image.putpixel((i,j),(j//4 , 53, i//4 , 255))

			elif color == 2:

			# 	image.putpixel((i,j),(0 , count % 255, 255, 255))
			# 	if j >= 514:
			# 		image.putpixel((i,j),(0,0,0, abs(j - 769)))

			# 	else:
			# 		image.putpixel((i,j),(0,0,0, abs(j - 259)))

				image.putpixel((i,j),(103 , j//4, i//4 , 255))

			# elif color == 3:

				# image.putpixel((i,j),(103 , i//4, j//4 , 255))

			# 	image.putpixel((i,j),( 1, 19, count % 255, 255))

	name = input("Save As: ")
	name = name + ".png"
	image.save(str(name), "PNG")

imagery(xRange2, yRange2)
		







