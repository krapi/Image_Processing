import Image
import math
img = Image.open("krapi.jpg").convert('L')
newImg=Image.new('L',img.size)
newImg.paste(img,(0,0))
pixels=img.getdata()

def runlengthEncode(pixels):
	output=[]
	count=1
	for i in range (len(pixels)-1):
		if(pixels[i]==pixels[i+1]):
			count+=1
		else:
			tup=(pixels[i],count)
			output.append(tup)
			count=1
	#print output
	return output

def runlengthDecode(output):
	newpixels=[]
	count=1
	for i in range (len(output)-1):
		for j in range (output[i][1]):
			newpixels.append(output[i][0])
	return newpixels			



output=runlengthEncode(pixels)
newImg.putdata(runlengthDecode(output))
pix = newImg.getdata()
newImg.save("lossless.jpg")
