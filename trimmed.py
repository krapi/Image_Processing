import os,sys,Image
from matplotlib import pyplot as plt


def add(x,y): return x+y
def mask(pixs,i,j) :
  list1=[]
  list1.append(pixs[i-1,j-1])
  list1.append(pixs[i-1,j])
  list1.append(pixs[i-1,j+1])
  list1.append(pixs[i,j-1])
  list1.append(pixs[i,j])
  list1.append(pixs[i,j+1])
  list1.append(pixs[i+1,j-1])
  list1.append(pixs[i+1,j])
  list1.append(pixs[i+1,j+1])
  list1.sort()
  del list1[0:2]
  del list1[-2:]
  return (int)(reduce(add, list1)/5)


img=Image.open('krapi.jpg').convert('L')
pixels=list(img.getdata())
newimg=Image.new('L',img.size)
newimg.paste(img,(0,0))
pixs=newimg.load()
for i in range(1,newimg.size[0]-1) :
  for j in range(1,newimg.size[1]-1) :
    pixs[i,j]=mask(pixs,i,j)

newimg.save('trimmed-krapi.jpg')
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(newimg, cmap = 'gray')
plt.title('Trimmed Average filter image'), plt.xticks([]), plt.yticks([])
plt.show()


