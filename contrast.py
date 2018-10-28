from PIL import Image
import matplotlib.pyplot as plt
img = Image.open('krapi.jpg').convert('L')
img.show()
pixdata = img.load()
histo = img.histogram()
plt.plot(histo)
plt.show()
for i in range(img.size[1]):
	for j in range(img.size[0]):
		if (pixdata[j,i] >=80) and (pixdata[j,i]<=220):
			pixdata[j,i] = 200


img.show()
img.save('krapislicing.jpg')