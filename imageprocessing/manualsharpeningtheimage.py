import numpy as np
import cv2

img=cv2.imread('ks.jpg',0)
rows,cols=img.shape
mod=img[:]


kernel = np.array([[0,0,0],[0,2,0],[0,0,0]])
kernel2 = np.ones((3,3))/9
img2 = img.copy()
img3=img.copy()
def gaussian_filter(img2,k1,k2):
   for i in range(0,rows-3,1):
       for j in range(0,cols - 3,1):
          c=(np.multiply(img2[i:i+3,j:j+3] , k1)  - np.multiply(img2[i:i+3,j:j+3],k2)) -1
          val=sum(sum(np.array(c)))
          img3[i+1][j+1] = val
   return img3
mod=gaussian_filter(img2,kernel,kernel2)
print
cv2.imshow('image',img)
cv2.imshow('mod',mod)


cv2.waitKey(0)
cv2.destroyAllWindows()