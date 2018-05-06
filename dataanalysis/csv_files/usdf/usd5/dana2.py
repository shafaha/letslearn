import pandas as pd
import quandl
import numpy as np
import matplotlib.pyplot as plt

#query=Quandl.get('query',auth_token=a_key)

x='AK_AL_AR_AZ_CA_CO_CT_DE_FL_GA_HI_IA_ID_IL_IN_KS_KY_LA_MA_MD_ME_MI_MN_MO_MS_MT_NC_ND_NE_NH_NJ_NM_NV_NY_OH_OK_OR_PA_RI_SC_SD_TN_TX_UT_VA_VT_WA_WI_WV_WY'
lis=x.split('_')
fil=str(lis[0]+'.csv')
print(fil)
main_df=pd.read_csv('AK.csv')
print(main_df)

'''for abbr in lis:
    fil=str(abbr)+'.csv'
    print(fil)
    df1=pd.read_csv(fil)
    if main_df.empty:
       main_df=df1
    else:
        main_df=main_df.join(df1)
print(main_df)
'''
