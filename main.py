#############################################################################
###########               Import python packages
#############################################################################
import pandas as pd
import utils.import_export_data as import_export_data
import utils.porcessing_extreme_values as pev
import utils.modelization as modelization
from utils.send_email import send_alerting_email
import utils.plots as plots

#############################################################################
###########               Import data
#############################################################################
df = import_export_data.import_data("select * from sales;", "alertingSystem").drop('id', axis=1)
df['CA'] = df['CA'].astype('float')
#############################################################################
###########               Processing extreme values
#############################################################################
df['CA'] = pev.traiter_valeurs_extremes_continues(df, 'CA')

#############################################################################
###########               make model to detect anomalies
#############################################################################
df = modelization.make_prediction(df)

#############################################################################
###########               alert by emails
#############################################################################
if df.loc[df.shape[0]-1, ['alert_low', 'alert_high']].sum()>0:
    low = df['alert_low'].iloc[-1]>0
    df = df[['ds','CA','yhat_lower','yhat_upper']]
    df.set_index('ds', inplace=True)
    plots.plot_figure(24, df)
    plots.plot_figure(48, df)
    if low:
        send_alerting_email('Low Volume', 'Low')
    else:
        send_alerting_email('High Volume', 'High')
