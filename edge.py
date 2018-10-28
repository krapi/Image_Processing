import os,sys,Image
import math
from matplotlib import pyplot as plt

img=Image.open("krapi.jpg").convert('L')
pixels = img.load()
robertimg=Image.new('L',img.size)
robertimg.paste(img,(0,0))
rpixs=robertimg.load()

prewittimg=Image.new('L',img.size)
prewittimg.paste(img,(0,0))
ppixs=prewittimg.load()

sobelimg=Image.new('L',img.size)
sobelimg.paste(img,(0,0))
spixs=sobelimg.load()


# For Roberts edge detection filter
for i in range(1,img.size[0]-1) :
  for j in range(1,img.size[1]-1) :
    x=( pixels[i,j]) + -1 * pixels[i+1,j+1]
    y=( pixels[i,j+1]) + -1 * pixels[i+1,j]
    rpixs[i,j] = (int)(abs(x) + abs(y))
robertimg.save("edge_krapi_roberts.jpg")


#For Prewitt edge detection filter
for i in range(1,img.size[0]-2) :
  for j in range(1,img.size[1]-2) :
    x = pixels[i+1,j-1] + pixels[i+1,j] + pixels[i+1,j+1]  - (pixels[i-1,j-1] + pixels[i-1,j] + pixels[i-1,j+1])
    y = pixels[i-1,j-1] + pixels[i,j-1] + pixels[i+1,j-1]  -  (pixels[i-1,j+1] + pixels[i,j+1] + pixels[i+1,j+1])
    ppixs[i,j] = int(math.sqrt(x*x + y*y))
prewittimg.save("edge_krapi_prewitt.jpg")



#For Sobel edge detection filter
for i in range(1,img.size[0]-2) :
  for j in range(1,img.size[1]-2) :
    x = pixels[i+1,j-1] + 2*pixels[i+1,j] + pixels[i+1,j+1]  - (pixels[i-1,j-1] + 2*pixels[i-1,j] + pixels[i-1,j+1])
    y = pixels[i-1,j-1] + 2*pixels[i,j-1] + pixels[i+1,j-1]  - (pixels[i-1,j+1] + 2*pixels[i,j+1] + pixels[i+1,j+1])
    spixs[i,j] = int(math.sqrt(x*x + y*y))
sobelimg.save("edge_krapi_sobel.jpg")

f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2,sharex='col', sharey='row')
ax1.imshow(img, cmap = 'gray')
ax1.set_title('Input Image')
ax2.imshow(robertimg, cmap = 'gray')
ax2.set_title("Robert's Edge detected image")
ax3.imshow(prewittimg, cmap = 'gray')
ax3.set_title('Prewitt edge detected image')
ax4.imshow(sobelimg, cmap = 'gray')
ax4.set_title('Sobel edge detected Image')
f.suptitle('Edge Detection',fontsize=16)
plt.show()

