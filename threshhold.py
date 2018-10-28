from PIL import Image


img = Image.open("krapi.jpg")
img = img.convert("L")

pixdata = img.load()

for i in range(img.size[1]):
	for j in range (img.size[0]):
		if pixdata[j,i] < 115:
			pixdata[j,i] = 0
		else:
			pixdata[j,i] = 255
img.show()
img.save("krapithreshold.jpeg")
