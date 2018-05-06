import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#camparison of the dataframe lecture=
df=pd.read_csv('csv_files/result.csv')
df2=df[['name','maths']]
print(df2)
df2.loc[(df2.maths < 80),'maths']=np.NaN
df2=df2.interpolate(limit=1)
print(df2.maths)

