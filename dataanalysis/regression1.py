import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


x=[12,19, 21,25]
y=[201,206,220,250]
c1=sum(y)
a1=sum(x)
b1=len(x)
c2=sum(np.array(x) * np.array(y))
a2=sum(np.array(x) * np.array(x))
b2=a1
mat=np.array([a1,b1,a2,b2])
mat=mat.reshape(2,2)
mat2=np.array([c1,c2]).reshape(2,1)
matinv=np.linalg.inv(mat)
mato=np.dot(matinv,mat2)
print(mato[0])



plt.scatter(x,y)
plt.show()
