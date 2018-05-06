import numpy as np
import matplotlib.pyplot as plt
import cv2
from scipy.signal import convolve2d as conv2

from skimage import color, data, restoration


astro = cv2.imread('image/im.jpg',1)
astro = color.rgb2gray(astro)
psf = np.ones((5, 5)) / 25
astro = conv2(astro, psf, 'same')
# Add Noise to Image
astro_noisy = astro.copy()
astro_noisy += (np.random.poisson(lam=25, size=astro.shape) - 10) / 255.

# Restore Image using Richardson-Lucy algorithm
for i in range(5):
      astro_noisy = restoration.richardson_lucy(astro_noisy, psf, iterations=30)
      cv2.imshow("original_convolved",astro)
      cv2.imshow("noisy",astro_noisy)
      #cv2.imshow("deconvolved",deconvolved_RL)
      cv2.waitKey(0)
cv2.destroyAllWindows()