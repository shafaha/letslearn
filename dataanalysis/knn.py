import numpy as np
import cv2
import matplotlib.pyplot as plt


cordinates=np.random.randint(0,100,(25,2)).astype(np.float32)
#print(cordinates)
occurence=np.random.randint(0,2,(25,1)).astype(np.float32)
#print(occurence)

red=np.where(occurence.ravel() == 0)
red_c=cordinates[red]

print(red_c[:,0])
#print(red_x[:,1])'''
plt.scatter(red_c[:,0],red_c[:,1],marker='^',color='r')

blue_c=cordinates[np.where(occurence.ravel() == 1)]
plt.scatter(blue_c[:,0],blue_c[:,1],marker='h',color='b')

newcomer=np.random.randint(0,100,(1,2)).astype(np.float32)
new=newcomer.ravel()
print(newcomer)
plt.scatter(new[0],new[1],marker='H')


knn=cv2.ml.KNearest_create()
knn.train(cordinates,cv2.ml.ROW_SAMPLE,occurence)

ret,result,neighbour,dist=knn.findNearest(newcomer,3)
print("result: ",result)
print("neighbours: ",neighbour)
print("distances: ",dist)
plt.show()