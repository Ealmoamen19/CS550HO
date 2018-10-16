from PIL import Image

import random

imgx = 512
imgy = 512

image = Image.new("RGB", (imgx, imgy))

for i in range(512) :

	for j in range(512) :
		
		image.putpixel((i,j),((i * j)%510, (i*j)%255, (i*j)%255))

image.save("x.png", "PNG")

print(image)