import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import quandl
from matplotlib import style
style.use('ggplot')

#resampling is not happening
df=pd.read_pickle('fiddystatespct_change.pickle')

txresampled=df.resample('A',how='ohcl')
plt.title('HPI data')
df['TXhpi'].plot(color='g',label='monthly resampled data')
txresampled.plot(color='b',label='yearly resampled data')
plt.legend()


plt.show()




