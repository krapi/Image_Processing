from PIL import Image

img = Image.open('krapi.jpg')
img = img.convert('L') # convert to grayscale
pixdata = img.load() 
filtermask = [1 for i in range(9)]
k = 0
for i in range(1,img.size[1]-1):
    for j in range(1,img.size[0]-1):
        sum1 = 0
        for m in range(i-1,i+2):
            for n in range(j-1,j + 2):
                sum1 = sum1 + pixdata[n,m]*filtermask[k]
                k = k + 1
        k = 0
        pixdata[j,i] = sum1/9
       
final = []
for y in xrange(img.size[1]):
    for x in xrange(img.size[0]):
        final.append(pixdata[x,y])
img.putdata(final)

img.save("krapi_smooth.jpeg")
img.show()       