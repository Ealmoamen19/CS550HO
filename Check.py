from PIL import Image
import random
imgx = 512
imgy = 512
color = False 
def check() :
	global color
	if color == True :
				color  = False
	elif color == False :
				color = True
image = Image.new("RGB", (imgx, imgy))
for i in range(512) :
	if i % 2 == 0 :
			check()
	for j in range(512) :		
		if j % 2 == 0 :
			check()
		if color == True :
			image.putpixel((i,j),(255, 0, 0))
image.save("check.png", "PNG")
print(image)