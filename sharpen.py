from PIL import Image
im=Image.open("krapi.jpg")
im=im.convert("L")
i1=im.copy()
width,height=im.size
print(str(width)+" "+str(height))
sum1=0
for i in range(1,width-1):
	for j in range(1,height-1):
		sum1=0
		for a in range(i-1,i+2):
			for b in range(j-1,j+2):
				t=(a,b)
				if(a==i and b==j):
					sum1=sum1-(8*im.getpixel(t))
				else:
					sum1=sum1+im.getpixel(t)
		tu=(i,j)
		i1.putpixel(tu,int(sum1))
		x1=i1.getpixel(tu)
i1.save("sharpen.jpg")
i2=im.copy()
for i in range(0,width):
	for j in range(0,height):
		tup=(i,j)
		x=im.getpixel(tup)+i1.getpixel(tup)
		i2.putpixel(tup,x)
i2.save("sharpen_final.jpg")
i1.show()
i2.show()