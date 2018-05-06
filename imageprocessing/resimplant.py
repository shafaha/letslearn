import cv2
import numpy as np

window=cv2.namedWindow("masker",cv2.WINDOW_NORMAL)
img=cv2.imread('image/implant.png',0)
pre = img.copy()
mask = np.zeros(img.shape,dtype= np.uint8)
ix,iy = 0,0
fx,fy = 0,0
def line_maker(event,x,y,flags,params):
    global ix,iy,fx,fy
    if event ==cv2.EVENT_LBUTTONDOWN:
        ix,iy = x,y
    elif event == cv2.EVENT_LBUTTONUP:
        fx,fy = x,y
        cv2.line(mask,(ix,iy),(fx,fy),(255,255,255),5)
        cv2.line(img,(ix,iy),(fx,fy),(255,255,255),5)
cv2.setMouseCallback('masker',line_maker)

while True:
    cv2.imshow('masker',img)
    if cv2.waitKey(1) & 0xFF == ord('d'):
        break
cv2.imshow("letsee",mask)
dst = cv2.inpaint(pre,mask,3,cv2.INPAINT_NS)
cv2.imshow('result',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
 