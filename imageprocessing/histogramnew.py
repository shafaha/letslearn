import cv2
import numpy as np
import matplotlib.pyplot as plt
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














cv2.imshow('equalized',equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()
