from PIL import Image


img = Image.open("krapi.jpg")
img = img.convert("L")

pixdata = img.load()

for y in xrange(img.size[1]):
 for x in xrange(img.size[0]):
 	pixel = pixdata[x,y]
 	pixdata[x,y] = 255-pixel

img.save("krapithreshold.jpeg")
