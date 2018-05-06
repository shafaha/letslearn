import cv2
import numpy as np
import time
'''
your computer will be destroyed
camera extracting beautiful out of series of image
'''
cap = cv2.VideoCapture(0)
ret,frame= cap.read()
time.sleep(2)
while True:
    image_list = []
    for i in range(5):
        ret,frame= cap.read()
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        frame = cv2.flip(frame,180)
        image_list.append(frame)
        #name = chr(97 + i) + '.png'
        #cv2.imwrite(name,frame)
    dst = cv2.fastNlMeansDenoisingMulti(image_list, 2, 5, None, 4, 7, 35)
    cv2.imshow('destination',dst)
    #type q to get out
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #cv2.imwrite('result.png',dst)    
cap.release()
cv2.destroyAllWindows()