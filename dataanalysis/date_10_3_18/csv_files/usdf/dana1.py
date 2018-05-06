import numpy as np
import pandas as pd
import quandl
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

df=pd.read_csv('simple.csv',parse_dates=['Date'])
#df.set_index('Date',inplace=True)
df.columns=['date','Austin_HOUSE']
plt.plot(df.date,df.Austin_HOUSE,label='hpi',color='g')
plt.xlabel='date'
plt.ylabel='HpI'

print(df.head(10))

plt.show()
#now saving the csv  but without any
df.to_csv('headerless.csv',header=False)

df3=pd.read_csv('headerless.csv',names=['dates','austin_fouse'])
print(df3.head())
#df.remname can do renaming column df.rename({'austin_fouse':'austin house'}