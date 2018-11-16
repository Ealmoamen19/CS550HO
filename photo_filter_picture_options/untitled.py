from PIL import Image

import PIL

img = Image.open("astronomy-cosmos-dark-733475.jpg")

img2 = Image.open("IMG_5816.JPG")

width, height = img2.size

print(width, height)

xcoor = width

xer = False

def printpercent(i):

	global xcoor

	global xer

	percent = i/xcoor

	percentage = int(percent * 100)

	if percentage == 10 and xer == False:

		print("10%")
		xer = True

	elif percentage == 20 and xer == True:

		print("20%")
		xer = False

	elif percentage == 30 and xer == False:

		print("30%")
		xer = True

	elif percentage == 40 and xer == True:

		print("40%")
		xer = False

	elif percentage == 50 and xer == False:

		print("50%")
		xer = True

	elif percentage == 60 and xer == True:

		print("60%")
		xer = False

	elif percentage == 70 and xer == False:

		print("70%")
		xer = True

	elif percentage == 80 and xer == True:

		print("80%")
		xer = False

	elif percentage == 90 and  xer == False:

		print("90%")
		xer = True

for i in range(0, width) :

	for j in range(0, height) :

		xy = i, j

		R, G, B = img2.getpixel(xy)

		R2, G2, B2 = img.getpixel(xy)

		if B >= 200 :

			img2.putpixel((i,j),(R2, G2 , B2))

		else :

			img2.putpixel((i, j), (R - 30, G - 30, B - 30))

		printpercent(i)

img2.show()

