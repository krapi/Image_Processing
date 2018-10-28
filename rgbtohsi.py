import cv2
import math
import numpy as np
img = cv2.imread('imgserver.jpg',1)


newimg = np.zeros(img.shape,dtype=np.int)

		

for y in range(img.shape[1]):
	for x in range (img.shape[0]):
		r = float(img[x,y][2])/255
		g = float(img[x,y][1])/255
		b = float(img[x,y][0])/255
		i = (b + g + r) / 3.0
		min_val = min(r,g,b)
		s = 1 - 3.0*(min_val/(b + g + r+0.00001))
		if s < 0.00001:
			s = 0
		elif s > 0.99999:
			s = 1
		h = 0.0
		if s!=0:
			num = 0.5 *((r-g) + (r-b))
			den = math.sqrt((r-g)*(r-g) + (r-b)*(g-b)+.00001)
			h = num / den
			h = math.acos(h)
			h = math.degrees(h)
			if(b<g):
				h = h
			else :
				h = 360 -h
		newimg[x,y][0] = h
		newimg[x,y][1] = s * 255
		newimg[x,y][2] = i * 255
		
cv2.imwrite("HSI-krapi1.png",newimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
