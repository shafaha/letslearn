import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import quandl
from matplotlib import style
style.use('ggplot')


df=pd.read_pickle('fiddystatespct_change.pickle')
df['TXhpi12Ma']=pd.rolling_mean(df['TXhpi'],12)
df['TXhpiStd']=pd.rolling_std(df['TXhpi'],12)
#print(df["TXhpi12Ma"])
#print(df['TXhpistd'])

plt.figure(1)
ax1=plt.subplot2grid((2,2),(0,0))
ax2=plt.subplot2grid((2,1),(1,0),sharex=ax1)
df[['TXhpi','TXhpi12Ma']].plot(ax=ax1)
df['TXhpiStd'].plot(ax=ax2)



plt.figure(2)
ax1=plt.subplot2grid((2,2),(0,0))
ax2=plt.subplot2grid((2,2),(1,0))
tx_ak_hpicorr=pd.rolling_corr(df['TXhpi'],df['AKhpi'],12)

df[['TXhpi','AKhpi']].plot(ax=ax1)
tx_ak_hpicorr.plot(ax=ax2)

plt.show()



