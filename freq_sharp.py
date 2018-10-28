import numpy as np
import cv2
from matplotlib import pyplot as plt
import math

D0 = 30.0
def ideal(M,N):
	H = np.ones((M,N,2))
	for u in range(1,M):
		for v in range(1,N):
			D = math.sqrt((u-M/2)**2 + (v-N/2)**2)
			if D < D0:
				H[u,v] = 0
	return H

def butter(n,M,N):
	H = np.ones((M,N,2))
	for u in range(1,M):
		for v in range(1,N):
			D = math.sqrt((u-M/2)**2 + (v-N/2)**2)
			D = D + 0.00001
			if D < D0:
				H[u,v] = 1/(1+(D0/D)**(2*n))
	return H

def gaussian(M,N):
	H = np.ones((M,N,2))
	for u in range(1,M):
		for v in range(1,N):
			D = math.sqrt((u-M/2)**2 + (v-N/2)**2)
			if D < D0:
				H[u,v] = 1 - math.exp(-(D**2)/(2 * D0**2))
	return H

img = cv2.imread('krapi.jpg',0)
img_float32 = np.float32(img)
dft = cv2.dft(img_float32, flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
rows, cols = img.shape
ideal_mask = ideal(rows,cols)
butter_mask = butter(2,rows,cols)
gaussian_mask = gaussian(rows,cols)

ideal_fshift = dft_shift*ideal_mask
ideal_f_ishift = np.fft.ifftshift(ideal_fshift)
ideal_img_back = cv2.idft(ideal_f_ishift)
ideal_img_back = cv2.magnitude(ideal_img_back[:,:,0],ideal_img_back[:,:,1])

butter_fshift = dft_shift*butter_mask
butter_f_ishift = np.fft.ifftshift(butter_fshift)
butter_img_back = cv2.idft(butter_f_ishift)
butter_img_back = cv2.magnitude(butter_img_back[:,:,0],butter_img_back[:,:,1])

gaussian_fshift = dft_shift*gaussian_mask
gaussian_f_ishift = np.fft.ifftshift(gaussian_fshift)
gaussian_img_back = cv2.idft(gaussian_f_ishift)
gaussian_img_back = cv2.magnitude(gaussian_img_back[:,:,0],gaussian_img_back[:,:,1])


# f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2,sharex='col', sharey='row')
# ax1.imshow(img, cmap = 'gray')
# ax1.set_title('Input Image')
# ax2.imshow(ideal_img_back, cmap = 'gray')
# ax2.set_title('Ideal filtered image')
# ax3.imshow(butter_img_back, cmap = 'gray')
# ax3.set_title('Butterworth filtered image')
# ax4.imshow(gaussian_img_back, cmap = 'gray')
# ax4.set_title('Gaussian filtered Image')

plt.figure(0)
plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title("Magnitude Spectrum"),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(ideal_img_back,cmap='gray')
plt.title("Ideal"),plt.xticks([]),plt.yticks([])
plt.figure(1)
plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title("Magnitude Spectrum"),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(butter_img_back,cmap='gray')
plt.title("utterB"),plt.xticks([]),plt.yticks([])
plt.show()  