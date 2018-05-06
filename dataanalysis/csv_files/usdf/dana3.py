import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import quandl
import pickle

def state_list():
    x='AK_AL_AR_AZ_CA_CO_CT_DE_FL_GA_HI_IA_ID_IL_IN_KS_KY_LA_MA_MD_ME_MI_MN_MO_MS_MT_NC_ND_NE_NH_NJ_NM_NV_NY_OH_OK_OR_PA_RI_SC_SD_TN_TX_UT_VA_VT_WA_WI_WV_WY'
    return x.split('_')
def grab_data():
    lis=state_list()
    main_df = pd.DataFrame()
    for abbr in lis:
        fil = str(abbr) + '.csv'
        nam = str(abbr) + 'hpi'
        df1 = pd.read_csv(fil)
        df1.columns = ['Date', nam]
        df1.set_index('Date',inplace=True)
        df1.columns=[nam]
        df1[nam]=(df1[nam]-df1[nam][0])/df1[nam][0] * 100
        #print(df1.head())
        if main_df.empty:
            main_df = df1
        else:
            main_df = main_df.join(df1)
    print(main_df.head())
    print(main_df.tail())
    pickle_out=open('fiddystatespct_change.pickle','wb')
    pickle.dump(main_df,pickle_out)
    pickle_out.close()


grab_data()
hppct_change=pd.read_pickle('fiddystatespct_change.pickle')
#print(hppct_change)
#hppct_change.plot()
#plt.legend().remove()
plt.show()

hppct_change_correlation=hppct_change.corr()
#print(hppct_change_correlation)











