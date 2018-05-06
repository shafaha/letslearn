import pandas as pd
import pickle
import matplotlib.pyplot as plt
#creating pickle of the data
#creating the percentage change in the data
def grab_data():
   fl=open('states.txt','r')
   maindf=pd.DataFrame()
   for lines in fl:
      x=lines.split('_')
      v=x[1][:2]
      df=pd.read_csv('csv_files/usdf/'+v+'.csv') 
      df.columns=['Dates',v]
      df.set_index('Dates',inplace=True)
      if maindf.empty :
           maindf=df
      else:
           maindf=maindf.join(df)
      pickle_out=open('pickleing.pickle','wb')
      pickle.dump(maindf,pickle_out)
      pickle_out.close()
#grab_data()
pickle_in=open('pickleing.pickle','rb')
data=pickle.load(pickle_in)
print(data) 
data.plot()
plt.show()
pickle_in.close()

#print(maindf.head()) 
def grab_pct_change():
   fl=open('states.txt','r')
   maindf=pd.DataFrame()
   for lines in fl:
      x=lines.split('_')
      v=x[1][:2]
      df=pd.read_csv('csv_files/usdf/'+v+'.csv')
      df.columns=['Dates',v]
      df.set_index('Dates',inplace=True)
      df=df.pct_change()
      df=df.dropna()
      if maindf.empty :
           maindf=df
      else:
           maindf=maindf.join(df)
      pickle_out=open('pickleing_percentage.pickle','wb')
      pickle.dump(maindf,pickle_out)
      pickle_out.close()
grab_pct_change()
pickle_in=open('pickleing_percentage.pickle','rb')
data=pickle.load(pickle_in)
print(data) 
data.plot()
plt.show()
pickle_in.close()