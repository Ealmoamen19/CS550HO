from PIL import Image

import math

from turtle import *

xcoor = 1024.0

ycoor = 1024.0

count = 0

lineLength = 350.0

startingPoint = [384, 512]

angle = 0

image = Image.new("RGBA", (int(xcoor), int(ycoor)))


def cCurve(n, lineLength):

	global count
	

	for i in range(0, n) :

		lineLength = lineLength/2

		count = count + 1

		angle = angle + 45

	penup()

	bk(175)

	rt(angle)

	pendown()

	for i in range(0, count) :		

		fd(lineLength)

		rt(90)

cCurve(5, lineLength)









