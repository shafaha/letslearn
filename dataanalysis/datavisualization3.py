import pandas as pd
import pickle
import matplotlib.pyplot as plt
maindf=pd.DataFrame()
def grab_data():
    global maindf
    fl=open("states.txt",'r')
    for lines in fl:
        l=lines.split('_')[1][:2]
        df=pd.read_csv('csv_files/usdf/'+l+'.csv')
        df.columns=['Date',l]
        df.set_index('Date',inplace=True)
        df[l]=(df[l] - df[l][0])/df[l][0]  *100
        #print(df.head())
        if maindf.empty:
            maindf=df
        else:
            maindf=maindf.join(df)
            
        pickle_out=open('usa.pickle','wb')
        pickle.dump(maindf,pickle_out)
        pickle_out.close()
        
grab_data()
pickle_in=open('usa.pickle','rb')
data=pickle.load(pickle_in)
#data.plot()
#plt.show()
data_rt=data.corr()
print(data_rt)