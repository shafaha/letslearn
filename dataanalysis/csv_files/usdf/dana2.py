import pandas as pd
import quandl
import numpy as np
import matplotlib.pyplot as plt
import pickle
#pandas have its own pickling
#query=Quandl.get('query',auth_token=a_key)
def state_list():
    x='AK_AL_AR_AZ_CA_CO_CT_DE_FL_GA_HI_IA_ID_IL_IN_KS_KY_LA_MA_MD_ME_MI_MN_MO_MS_MT_NC_ND_NE_NH_NJ_NM_NV_NY_OH_OK_OR_PA_RI_SC_SD_TN_TX_UT_VA_VT_WA_WI_WV_WY'
    return x.split('_')
def grab_data():
    lis=state_list()
    main_df = pd.DataFrame()
    for abbr in lis:
        fil = str(abbr) + '.csv'
        nam = str(abbr) + 'hpi'
        print(fil)
        df1 = pd.read_csv(fil)
        df1.columns = ['Date', nam]
        if main_df.empty:
            main_df = df1
        else:
            main_df = main_df.merge(df1, on=['Date'])
    pickle_out=open('fiddystates.pickle','wb')
    pickle.dump(main_df,pickle_out)
    pickle_out.close()
grab_data()

pickle_in=open('fiddystates.pickle','rb')
HPI_data=pickle.load(pickle_in)
#print(HPI_data)
pickle_in.close()
#pandas has its own pickling method at all
HPI_data.to_pickle('pandpickl.pickle')

pick=pd.read_pickle('pandpickl.pickle')
pick.plot()
plt.legend().remove()
plt.show()
print(pick.head())

#### NEXT DANA3 IS IN CONTINUATION










