from PIL import Image
import random
imgx = 512
imgy = 512
image = Image.new("RGB", (imgx, imgy))
def streamer() :
	x = random.randint(0, 512)
	colorR = random.randint(0, 255)
	colorG = random.randint(0, 255)
	colorB = random.randint(0, 255)
	image.putpixel((0,x),(colorR, colorG, colorB))
	for i in range(512) :
		if x >= 510 :
			x = 510
		elif x <= 0 :
			x = 1
		z = random.random()
		if z >= 0.5 :
			image.putpixel((x+1,i),(colorR, colorG, colorB))
			image.putpixel((x,i),(colorR, colorG, colorB))
			x = x+1
		else :
			image.putpixel((x-1,i),(colorR, colorG, colorB))
			image.putpixel((x,i),(colorR, colorG, colorB))
			x = x-1
for i in range(0, 50) :
	streamer()
image.save("y.png", "PNG")
print(image)