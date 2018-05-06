import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_pickle('usa.pickle')
texas=df.TX
alaska=df.AL
texas_12mean=pd.rolling_mean(texas,12)
texas_12std=pd.rolling_std(texas,12)
#finding the corelation table

texas_alaska=pd.rolling_corr(df.TX,df.AL,12)



fig=plt.figure()
ax1=plt.subplot2grid((2,1),(0,0))
ax2=plt.subplot2grid((2,1),(1,0),sharex=ax1)
texas.plot(ax=ax1,label="tx")
alaska.plot(ax=ax1,label="al")
texas_alaska.plot(ax=ax2,label="tx_al")
plt.show()




