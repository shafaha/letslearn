import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

maindf=pd.read_csv("csv_files/result.csv")
df1=maindf[['name','chemistry']]
df2=maindf[['name','physics']]
#concatenation of two dataframe
df3=pd.concat([df1,df2],axis=1,keys=['chemistry','physics'])
print(df3)
#mergingof data1,
df4=pd.merge(df1,df2,on='name',how='outer',indicator=True)
print(df4.head(2))
