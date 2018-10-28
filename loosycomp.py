import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import scipy.fftpack

im = Image.open('jay.jpg').convert('L')
img = np.array(im)
# print type(im)
# print im
#img = cv2.imread('jay.jpg',0)
#print img.shape
img_rows = img.shape[0]
img_col =img.shape[1]

img_centered = np.add(img,-127)

# padding the image for 8*8 blocks
if img_rows%8 != 0:
	row_req = img_rows%8
	padded_img_rows = img_rows + (8-row_req)
else :
	padded_img_rows = img_rows
if img_col%8 != 0 :
	col_req = img_col%8
	padded_img_col = img_col + (8-col_req)
else :
	padded_img_col = img_col
padded_img = np.zeros((padded_img_rows,padded_img_col),dtype=np.int)
for row in range(img_rows):
	for col in range(img_col):
		padded_img[row,col] = img_centered[row,col]
print padded_img.shape

subimage = []
subblock = np.zeros((8,8))
#creating subimages of 8*8 
for row in xrange(0,padded_img_rows,8):
	for col in xrange(0,padded_img_col,8):
		subblock = padded_img[row:row+8, col:col+8]
		subimage.append(subblock.astype(float))

# #performing DCT on each block
dct_list =[]
dct = np.zeros((8,8))
for each in subimage:
	#dct = cv2.dct(each)
	dct = scipy.fftpack.dct(each,norm='ortho')
	dct_list.append(dct)
print len(dct_list)

#performing quantization 
quant = np.array([[16,11,10,16,24,40,51,61],[12,12,14,19,26,58,60,55],[14,13,16,24,40,57,69,56],[14,17,22,29,51,87,80,62],[18,22,37,56,68,109,103,77],[24,35,55,64,81,104,113,92],[49,64,78,87,103,121,120,101],[72,92,95,98,112,100,103,99]])
quant_list =[]
quantised = np.zeros((8,8),dtype=np.int)
for each in dct_list:
	quantised = np.divide(each,quant)
	quantised = quantised.astype(int)
	quant_list.append(quantised)
print len(quant_list)

print quant_list[4]
print quant_list[0]
# this gives comprressed image dct. to recover image perform inverse quantization followed by inverse DCT

zigzag = np.array([00, 01, 10, 20, 11, 02, 03, 12, 21, 30, 40, 31, 22, 13, 04, 05, 14, 23, 32, 41, 50])


print quant_list[0]

# zlist = []
# i = 0
# for each in quant_list:
# 	zig_zag = []
# 	zig_zag = [0] * 64
# 	zig_zag = np.array(zig_zag)
# 	#print trial
# 	for i in range(0,zigzag.shape[0]):
# 		coords = zigzag[i]
# 		zig_zag[i] = each[coords/10][coords%10]
# 	newzig =  zig_zag 
# 	zlist.append(newzig)

# print len(zlist)



iquant_list=[]
iquantised = np.zeros((8,8),dtype=np.int)
for each in quant_list:
	iquantised = np.multiply(each,quant)
	iquant_list.append(iquantised)
#print iquant_list

#inverse dct
idct_list = []
idct = np.zeros((8,8))
for each in iquant_list:
	idct = scipy.fftpack.idct(each.astype(float),norm="ortho")
	#idct = cv2.idct(each.astype(float))
	idct = np.add(idct.astype(int),127)
	idct_list.append(idct)
#print idct_list

#print idct_list[0]
#combinibg the subblocks to form single image
comp_img = np.zeros((padded_img_rows,padded_img_col),dtype=np.int)
i = 0
for row in xrange(0,padded_img_rows,8):
	for col in xrange(0,padded_img_col,8):
		comp_img[row:row+8, col:col+8] = idct_list[i]
		i+=1
#print comp_img

cv2.imwrite('jay-lossycompressed.jpg',comp_img)
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(comp_img, cmap = 'gray')
plt.title('Loosy compressed image'), plt.xticks([]), plt.yticks([])
plt.show()




