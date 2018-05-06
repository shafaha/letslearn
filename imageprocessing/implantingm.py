import cv2
import numpy as np



#ret,img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#img =cv2.erode(img,np.ones((0,0),dtype = np.uint8),iterations = 2)
def method1_basic_bluring(): 
    img = cv2.imread('image/im.jpg',1)
    original =img.copy()
    for i in range(3):
         #img = cv2.GaussianBlur(img,(3,3),0,0)
         img =cv2.medianBlur(img,3)
    cv2.imshow("image",img)
    cv2.imshow("image2",original)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def method2_deionising():
    img = cv2.imread('in.jpg',1)
    original = img.copy()
    for i in range(3):
         #img = cv2.GaussianBlur(img,(3,3),0,0)
         img =cv2.medianBlur(img,3)
    dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
    #dst = [cv2.equalize(i) for i in np.hsplit(dst,3)]
    
    #dst = np.hstack((dst[0],dst[1],dst[2]))
    cv2.imshow("original",original)
    cv2.imshow('metod2',dst)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
method2_deionising()
