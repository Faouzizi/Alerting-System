#############################################################################
###########               Import python packages
#############################################################################
import pandas as pd
import utils.import_export_data as import_export_data
import utils.porcessing_extreme_values as pev
import utils.modelization as modelization
from send_email import send_alerting_email
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
    send_alerting_email()
touch README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/Faouzizi/Alerting-System.git
git remote set-url origin https://github.com/Faouzizi/Alerting-System.git
git push -u origin master