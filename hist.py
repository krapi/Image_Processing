from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('krapi histo.jpg').convert('L')
img.save('krapi-grey2.jpg')

pixdata = img.load()
histo = img.histogram()
print histo
#l=[i for i in range(0,256)]
histo1 = []
histo1 = img.histogram()    

#calculate cdf
sum1 = histo[0]
for i in range(1,256):
    sum1 = sum1 + histo[i]
    histo[i] = histo[i] + histo[i-1]

cdf = []
for i in range(0,256):
    div = float(histo[i])/float(sum1)
    cdf.append(int(div*255))

# replacing new grey levels
for y in range(img.size[1]):
    for x in range(img.size[0]):
        pixdata[x,y] = cdf[pixdata[x,y]]

#list of new grey level used to create the image again
final = []
for y in range(img.size[1]):
    for x in range(img.size[0]):
        final.append(pixdata[x,y])

img.putdata(final)
img.show()        
      

plt.figure(0)
plt.bar(range(len(histo1)),histo1)
plt.ylabel('Pixel Frequency')
plt.xlabel('Pixel')
plt.xlim(0,250)
plt.figure(1)
plt.bar(range(len(img.histogram())),img.histogram())
plt.ylabel('Pixel Frequency')
plt.xlabel('Pixel')
plt.show()

to_save = "histogram-krapi2.jpeg"
img.save(to_save)