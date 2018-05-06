import numpy as np

a=np.array([[1,2,3],[4,5,6]]).reshape(2,3)
b=np.ones((2,3),dtype=int)
print(a[1:,:] - b[1:,:])
