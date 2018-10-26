#Started: 10/18/2018
#Finished: 10/25/2018

#Sources:

# https://www.atopon.org/mandel/#
# https://en.wikipedia.org/wiki/Julia_set
# https://www.youtube.com/watch?v=mg4bp7G0D3s
# http://paulbourke.net/fractals/juliaset/
# https://www.youtube.com/watch?v=2AZYZ-L8m9Q
# http://www.brucelindbloom.com/index.html?Math.html

#Honor Code: I have not given nor recieved any unauthorized aid.

#Brief Explanations:

#Mandelbrot 1:
# I added the alpha channel to the RGB and started creating gradients, that in combination with the modulus got a pattern that was both segmented and gradient.

# Mandelbrot 2:
# I created a modulus based system with each modulus being colored with a screen-wide gradient that's based on the coordinates rather that the mandelbrot values.
# The result was a modular-gradient fractal with shifting different colors.

# Julia:
# I used the same modulus system I used for the madelbrot 2, but with a different gradient. I alternated between two similar blue gradients and left one modulus transparent,
# or rather I started another julia set with a different c-value in the place of it. I scaled the new julia set a but just so that it frames the other one. I fulled the 
# transparent space behind the existing julia set with a red-yellow gradient. Then, I split the second julia set into modules each colored with the same gradient but accross different 
# axis for contrast. So it's basically two julia sets colored by gradients.


from PIL import Image

import math

#Variables for the pixel values

xcoor = 1024.0

ycoor = 1024.0

#Different ranges for all the different fractals I made

xRange = [-2, 2]

xRange2 = [-1.25, 1.25]

xRange3 = [-0.3441721598307292, -0.3412628173828125]

yRange = [-2,  2]

yRange2 = [-1.25,  1.25]

yRange3 = [0.613800048828125, 0.6167093912760416]

xRange4 = [-0.4324595133463542, -0.4109293619791667]

yRange4 = [0.58946126302084,  0.6114247639973959]

#count is for the julia set function, juliana(z,c)
#count2. is for the mandelbrot set function, melbourne(z,c)

count = 0

count2 = 0

#xer is used later in the printpercent(i) function that prints progress for the generation of the fractals

xer = False

#Julia set function

def juliana(z, c) :

	global count 

	storeVal = [0,0]

	storeVal[0] = ((z[0] ** 2) - (z[1] ** 2))

	storeVal[1] = (2 * z[0] * z[1])

	summation = [0,0]

	summation[0] = c[0] + storeVal[0]

	summation[1] = c[1] + storeVal[1]

	count += 1

	if math.sqrt((summation[0] ** 2) + (summation[1] ** 2)) <= 2 and count < 255 :


		juliana(summation, c)

#Mandelbrot set function

def melbourne(z, c) :

	global count2 

	storeVal = [0,0]

	storeVal[0] = ((z[0] ** 2) - (z[1] ** 2))

	storeVal[1] = (2 * z[0] * z[1])

	summation = [0,0]

	summation[0] = c[0] + storeVal[0]

	summation[1] = c[1] + storeVal[1]

	count2 += 1

	if math.sqrt((summation[0] ** 2) + (summation[1] ** 2)) <= 2 and count2 < 255 :


		melbourne(summation, c)

#"Progress indicator"

#xer is alternated between true and false to prevent each percentage from being printed more than twice

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

#Julia Set Function

def imagery(xRange, yRange) :

	global xcoor

	global ycoor

	global count

	global count2

	for i in range(0, int(xcoor)) :

		for j in range (0, int(ycoor)) :

			#thingy is the coordinate variable for the 1st Julia set, thingy2 is for the 2nd

			thingy = [i/(xcoor/(xRange[1] - xRange[0]))+ xRange[0], j/(ycoor/(xRange[1] - xRange[0])) + yRange[0]]

			thingy2 = [i/(xcoor/(xRange2[1] - xRange2[0]))+ xRange2[0], j/(ycoor/(xRange2[1] - xRange2[0])) + yRange2[0]]

			printpercent(i)

			count = 0

			juliana(thingy, [0.285, 0.01])

			color = count % 4

			if color == 2 :

				image.putpixel((i,j),(31 , int(j//(ycoor//256)), 214 , 255))

			elif color == 3:

				image.putpixel((i,j),(31 , int(i//(xcoor//256)), 180 , 255))

			elif color == 0:

				image.putpixel((i,j),(50 , int(j//(ycoor//256)), 214 , 255))

			elif color == 1:

				juliana(thingy2, [0.285,0])

				color2 = count % 4

				count = int(count // 4.6)

				if thingy[0] >= -0.86 and thingy[0] <= 0.86 and thingy[1] >= -1.12 and thingy[1] <= 1.12 :

					image.putpixel((i,j),(255 , int(j//(ycoor//256)), 0 , 255))

				elif color2 == 2 :

			 		image.putpixel((i,j),( 255, int(i//(xcoor//256)), 0 , 255))

				elif color2 == 3:

					image.putpixel((i,j),( 229, 33, count % 255, 255))
					if j >= 514:
						image.putpixel((i,j),(0,0,0, abs(j - 769)))

					else:
						image.putpixel((i,j),(0,0,0, abs(j - 259)))

				elif color2 == 0:

					image.putpixel((i,j),(0 , count % 255, 255, 255))
					if j >= 514:
						image.putpixel((i,j),(0,0,0, abs(j - 769)))

					else:
						image.putpixel((i,j),(0,0,0, abs(j - 259)))

				elif color2 == 1:

					image.putpixel((i,j),( 255, int(j//(ycoor//256)),  0, 255))

	#Save As function

	print("100%\n")
	name = input("Save As: ")
	name = name + ".png"
	image.save(str(name), "PNG")

	#Mandelbrot 2 function

def imagery2(xRange, yRange) :

	global xcoor

	global ycoor

	global count2

	for i in range(0, int(xcoor)) :

		for j in range (0, int(ycoor)) :

			printpercent(i)

			thingy = [i/(xcoor/(xRange[1] - xRange[0]))+ xRange[0], j/(ycoor/(xRange[1] - xRange[0])) + yRange[0]]

			count2 = 0

			melbourne([0,0], thingy)

			color2 = count2 % 4

			if color2 == 0 :

				image.putpixel((i,j),(int(i//(xcoor//256)) , 53, int(j//(ycoor//256)) , 255))

			elif color2 == 1:

				image.putpixel((i,j),(int(j//(ycoor//256)) , 53, int(i//(xcoor//256)) , 255))

			elif color2 == 2:

				image.putpixel((i,j),(103 , int(j//(ycoor//256)), int(i//(xcoor//256)) , 255))

	#Save as function

	print("100%\n")
	name = input("Save As: ")
	name = name + ".png"
	image.save(str(name), "PNG")


#Mandelbrot 1 function

def imagery3(xRange, yRange) :

	global xcoor

	global ycoor

	global count2

	for i in range(0, int(xcoor)) :

		for j in range (0, int(ycoor)) :

			thingy = [i/(xcoor/(xRange[1] - xRange[0]))+ xRange[0], j/(ycoor/(xRange[1] - xRange[0])) + yRange[0]]

			printpercent(i)

			count2 = 0

			melbourne([0,0], thingy)

			color2 = count2 % 4

			if color2 == 0 :

				image.putpixel((i,j),(count2 % 255 , 40, 170 - int(i//(ycoor//145)) , 255))

			elif color2 == 1:

				#Alpha channel gradients

				image.putpixel((i,j),( 229, 33, count2 % 255, 255))

				if j//(xcoor/1024) >= 514:
					image.putpixel((i,j),(0,0,0, abs(int(j/(xcoor/1024)) - 769)))

				else:
					image.putpixel((i,j),(0,0,0, abs(int(j/(xcoor/1024)) - 259)))

			elif color2 == 2:

				#Alpha channel gradients

				image.putpixel((i,j),(0 , count2 % 255, 255, 255))

				if j//(xcoor/1024) >= 514:
					image.putpixel((i,j),(0,0,0, abs(int(j/(xcoor/1024)) - 769)))

				else:
					image.putpixel((i,j),(0,0,0, abs(int(j/(xcoor/1024)) - 259)))

			elif color2 == 3:

				image.putpixel((i,j),( 1, 19, count2 % 255, 255))

	#Save As function

	print("100%\n")
	name = input("Save As: ")
	name = name + ".png"
	image.save(str(name), "PNG")


#Checker makes sure all input values are valid, if not, the while loop loops back

checker = True

while checker == True :

	#A user friendly interface giving the choice between Mandelbrot 1 and 2 and the Julia set

	#Users can also pick whatever resolution they want

	x = input("Which Fractal would you like to print?\n\n(1) Mandelbrot 1\n(2) Mandelbrot 2\n(3) Julia\n")

	res = input("Output resolution: \nexample: 1024 --> 1024 x 1024\n\n")

	if res.isnumeric() == True :

		xcoor = float(res)

		ycoor = float(res)

		image = Image.new("RGBA", (int(xcoor), int(ycoor)))

		#Generating fractal feedback

		if int(x) == 3:

			checker = False

			print("Generating Fractal...")

			imagery(xRange, yRange)

		elif int(x) == 2:

			checker = False

			print("Generating Fractal...")

			imagery2(xRange3, yRange3)

		elif int(x) == 1:

			checker = False

			print("Generating Fractal...")

			imagery3(xRange4, yRange4)

		else: 

			print("Invalid input\nTry Again\n\n")

	else:

		print("Invalid input\nTry Again\n\n")


#End of program

#Eyad Al Moamen

	




		