import numpy as np
import pandas as pd
import quandl
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')


df1=pd.DataFrame({'HPI':[80,85,88,85],
                 'Int_Rate':[2,3,2,2],
                  'Us_Gdp_Rate':[50,55,65,55]},
                 index=[2001,2002,2003,2004])
df2=pd.DataFrame({'HPI':[80,85,88,85],
                 'Int_Rate':[2,3,2,2],
                  'Us_Gdp_Rate':[50,55,65,55]},
                 index=[2005,2006,2007,2008])
df3=pd.DataFrame({'HPI':[80,85,88,85],
                 'Int_Rate':[2,3,2,2],
                  'Low_tier_HPI':[50,52,50,53]},
                 index=[2001,2002,2003,2004])

df4=pd.concat([df1,df2],axis=0,keys=['df1','df2'])
print(df4)
#mering donot mind about all the index
#it has how parameter which take {left,right,inner,outer}
#join is used if index is to be considered



df5=df1.merge(df3,on=(['HPI','Int_Rate']))
print(df5)

df6=df1.join(df2)
print(df6)
