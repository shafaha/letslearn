import cv2
import numpy as np
'''numpy.random.randn(d1,d2,d3,d4) to produce the very gaussian noise in the image'''

def gnoise(img):
    x,y= img.shape
    noise = np.float32(np.random.randn(x,y))
    noisy =np.float32(img)
    noisy = (img + noise*50) %255
    return noisy
def removing_gnoise(noisy):
    kernel = np.ones((3,3),dtype = np.float32)/25
    filtered=cv2.filter2D(noisy,-1,kernel)
    return filtered
def weighted_average(noisy):
    kernel = np.array([[1,2,1],[2,4,2],[1,2,1]],dtype = np.float32)/16
    filtered=cv2.filter2D(noisy,-1,kernel)
    return filtered
def sharpen(noisy):
    kernel = np.array([[0,0,0],[0,2,0],[0,0,0]],dtype = np.float32)/5
    msk = np.ones((3,3),dtype = np.float32)/9
    msk = kernel - msk
    sharpen  = cv2.filter2D(noisy ,  -1,kernel)
    return sharpen
def clearer(noisy):
    for i in range(3):
         #img = cv2.GaussianBlur(img,(3,3),0,0)
         noisy =cv2.medianBlur(noisy,3)
    dst = cv2.fastNlMeansDenoisingColored(noisy,None,10,10,7,21)
    b,g,r = dst[:,:,0],dst[:,:,1],dst[:,:,2] 
    r = sharpen(r)
    g = sharpen(g)
    b=sharpen(b)
    dst  = cv2.merge((b,g,r))
    #dst = sharpen(dst)
    return dst
    

img= cv2.imread('image/in.jpg',1)
gray  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
noisy = np.uint8(gnoise(gray))
#go get some intuition of gaussian kernel
'''   cv2.GaussianBlur(noisy,(kernel_shape),sigmax,sigmay)'''
gaussian_blur =cv2.GaussianBlur(noisy,(31,31),10,10) 
sharp =clearer(img)

cv2.imshow("original",img)
cv2.imshow("noisy",noisy)
cv2.imshow("sharp",sharp)
#cv2.imshow("filtered",filtered)

cv2.waitKey()
cv2.destroyAllWindows()