import cv2
import numpy as np

img = cv2.imread('image/lips.jpg',0)
img = cv2.resize(img,None,fx = 3,fy=3,interpolation = cv2.INTER_LANCZOS4)
def sharpner(img2,k1,k2):
    rows,cols, = img2.shape
    img3 = img2.copy()
    for i in range(0,rows-3,1):
       for j in range(0,cols - 3,1):
          c=(np.multiply(img2[i:i+3,j:j+3] , k1)  - np.multiply(img2[i:i+3,j:j+3],k2)) -1
          val=sum(sum(np.array(c)))
          img3[i+1][j+1] = val
    return img3

k1 =  np.array([[0,0,0],[0,2,0],[0,0,0]])
k2 = np.ones((3,3))/8
img=sharpner(img,k1,k2)

cv2.imshow('gray',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
