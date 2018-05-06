import cv2
import numpy as np
eye_cascade = cv2.CascadeClassifier('cml/haarcascade_eye.xml')
face_cascade= cv2.CascadeClassifier('cml/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret,img = cap.read()
    img = cv2.flip(img,180)
    gray =  cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    for x,y,l,b in faces:
        cv2.rectangle(img,(x,y),(x+l,y+b),(0,225,255),2)
        eyes = eye_cascade.detectMultiScale(gray[y:y+b,x:x+l],1.3,5)
        for xe,ye,le,be in eyes:
            cv2.rectangle(img,(x+xe,y+ye),(x+xe+le,y+ye+be),(0,200,255),2)
    cv2.imshow('classified',img)
    if cv2.waitKey(1) & 0xFF == ord('d'):
        break
cap.release()
cv2.destroyAllWindows()
