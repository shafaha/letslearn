import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#merging and concatenation
#creating a dataframe
df1=pd.read_csv('ban.csv')

df1=pd.DataFrame({     'input':df1.input,
                       'output':df1.output,
                       'donated':df1.donated,
                       'date':pd.date_range(start='01/01/2017',end='2/12/2017',freq='w')})
print(df1.head())
df2=pd.DataFrame({'date':pd.date_range(start='02/19/2017',end='03/10/2017',freq='w'),
                  'input':np.array([450]*3,dtype=np.int32),
                  'output':[100,500,800],
                  'donated':[50,60,70]
                  })
                  
tomerge=pd.DataFrame({'date':pd.date_range(start='1/1/2017',end='02/12/2017',freq='w'),
                       'expected':np.array([800,900,400,500,600,300,800]),

                       })
df3=pd.merge(df1,tomerge,on='merge')
#actually merge can take more than on parameter

print(df3)
#now i gonna cancatenate and merge the data


