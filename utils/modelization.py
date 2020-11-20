#############################################################################
###########               Import python packages
#############################################################################
import pandas as pd
from fbprophet import Prophet


#############################################################################
###########               Modelization
#############################################################################
def make_prediction(df):
    df_temp = df.copy()
    df_temp.drop('y', axis=1, inplace=True)
    df_temp.rename(columns={'sellTime':'ds','CA':'y'}, inplace=True)
    model_fb = Prophet()
    model_fb.fit(df_temp[['ds','y']][:-1])
    future = model_fb.make_future_dataframe(periods=1, freq='5min')
    forecast = model_fb.predict(future)
    df = pd.merge(df,forecast[['ds','yhat','yhat_lower', 'yhat_upper']], how='inner', left_on='sellTime', right_on='ds')
    #############################################################################
    ###########               Alerting or not
    #############################################################################
    df['alert_high'] = 0
    df['alert_low'] = 0
    df.loc[df.shape[0]-1,'alert_high'] = 1 if df['CA'].iloc[-1]>df['yhat_upper'].iloc[-1] else 0
    df.loc[df.shape[0]-1,'alert_low'] = 1 if df['CA'].iloc[-1]<df['yhat_lower'].iloc[-1] else 0
    return(df)

