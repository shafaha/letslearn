import pandas as pd
import numpy as np

df= pd.DataFrame(np.arange(16).reshape((4,4)),index=['cow','goat','horse','lion'],columns=['eat','sleep','run','walk'])
print(df)
#in this we are going to do slicing indexing mean median cum sum cumprod  idmax corr corwith cov sort_index sort_values

#slicing and selection
print(df[:1])
print(df[['eat','sleep','run']])