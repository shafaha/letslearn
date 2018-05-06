import cv2
import numpy as np


screen = np.zeros((1000,1000),dtype = np.uint8)
cap = cv2.VideoCapture(0)
while cap.isOpened:
    _,frame = cap.read()
    frame= cv2.flip(frame,180)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l=np.array([110,50,50])
    u=np.array([150,255,255])
    mask =cv2.inRange(frame,l,u)
    frame = cv2.bitwise_and(frame,frame,mask = mask)
    cv2.imshow('new',frame)
    #cv2.imshow('mask',mask)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()