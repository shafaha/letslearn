import numpy as np
import cv2

img=cv2.imread('image/opencv.png',0)
rows,cols=img.shape
rand=2 +  np.random.randn(rows,cols).reshape(rows,cols)
#ret,rand=cv2.threshold(rand, 1 ,10,cv2.THRESH_BINARY)
modified=np.uint8(img + 3*rand)
blur=cv2.blur(modified,(3,3))

kernel=np.matrix([[1,2,1],[2,4,2],[1,2,1]])
gaussian=cv2.GaussianBlur(modified,(3,3),0)

#actually kernel here working simply as the weight matrix
#finding the gaussian of the image
def gaussian_filter():
   for i in range(0,rows-3,1):
       for j in range(0,cols - 3,1):
          c=np.multiply(modified[i:i+3,j:j+3] , kernel)
          val=sum(sum(np.array(c)))//16
          modified[i+1][j+1] = val    
kernel1= cv2.getGaussianKernel(3*3 , 10).reshape(3,3)
kernel1 = kernel1/np.sum(kernel1)
filter1 =cv2.filter2D(modified,-1,kernel1)
kernel2 = cv2.getGaussianKernel(11*11,5).reshape(11,11)
kernel2=kernel2/np.sum(kernel2)
filter2= cv2.filter2D(modified,  -1,kernel2)

cv2.imshow('image',img)
#cv2.imshow('modified',modified)
cv2.imshow('gaussian',gaussian)
cv2.imshow('blur',blur)
cv2.imshow('filter1',filter1)
cv2.imshow('filter2',filter2)
cv2.waitKey(0)
cv2.destroyAllWindows()


