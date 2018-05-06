from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv('ban.csv',index_col=0)
#here we have modified the csv data
df.columns=['used','output','pleasure']
print(df.head(5))

df.to_csv('banmodified.csv',header=False)
#
#using the modified
df2=pd.read_csv('banmodified.csv',names=['date','input','output','donated'],index_col=0)
print(df2.head())
#modifying single column
df2.rename(columns={'input':'used',
            'donated':'pleasure'},inplace=True)
print(df2.head()) 