from PIL import Image

imgx = 512
imgy = 512

image = Image.new("CMYK", (imgx, imgy))

image.putpixel((0,0),(255, 0, 0, 0))

image.save("x.jpeg", "JPEG")

print(image)