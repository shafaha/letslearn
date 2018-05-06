import cv2
import numpy as np
def histogram_equalizer(img):
    nb = cv2.equalizeHist(img[:,:,0])
    ng = cv2.equalizeHist(img[:,:,1])
    nr = cv2.equalizeHist(img[:,:,2])
    equalized = cv2.merge((nb,ng,nr))
    return equalized
def effecient_Equalizer(img):
    # create a CLAHE object (Arguments are optional).
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    nb = clahe.apply(img[:,:,0])
    ng = clahe.apply(img[:,:,1])
    nr = clahe.apply(img[:,:,2])
    equalized = cv2.merge((nb,ng,nr))    
    return equalized
def sharpner(img2):
    k1 =  np.array([[0,1,0],[1,-4,1],[0,1,0]])
    k2 = np.ones((3,3))/9
    #img2 =cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    rows,cols, = img2.shape
    img3 = img2.copy()
    for i in range(0,rows-3,1):
       for j in range(0,cols - 3,1):
          c=(np.multiply(img2[i:i+3,j:j+3] , k1)  - np.multiply(img2[i:i+3,j:j+3],k2)) -1
          val=sum(sum(np.array(c)))
          img3[i+1][j+1] = val
    return img3


img = cv2.imread('image/pro.jpg',0)
window = cv2.namedWindow('true',cv2.WINDOW_NORMAL)
ix,iy,fx,fy = 0,0,0,0
def resizer(event,x,y,flags,param):
    global ix,iy,fx,fy
    if event == cv2.EVENT_LBUTTONDOWN:
        ix,iy = x,y
    elif event == cv2.EVENT_LBUTTONUP:
        fx,fy = x,y
cv2.setMouseCallback('true',resizer)
while True:
    cv2.imshow('true',img)
    if cv2.waitKey(1) & 0xFF ==ord('d'):
         break
resized = cv2.resize(img[iy:fy,ix:fx],None,fx=3,fy= 3,interpolation = cv2.INTER_LANCZOS4)
sharp = sharpner(resized)
cv2.imshow('modified1',sharp)
cv2.waitKey(0)
cv2.destroyAllWindows()