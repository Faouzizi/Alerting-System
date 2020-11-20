#############################################################################
###########               Import python packages
#############################################################################
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
import matplotlib.dates as mdates
import matplotlib.ticker as ticker

#############################################################################
###########               Plot time series using last 24 or 48 hour
#############################################################################
def plot_figure(nb_hour, df):
    if nb_hour==24:
        df_24 = df[-nb_hour*12:]
        fig, ax = plt.subplots()
        ax.xaxis.grid(True, which='minor')
        ax.plot(df_24.index, df_24)
        ax.set_xlabel('Time')
        ax.set_ylabel('CA')
        ax.xaxis.set_major_locator(MultipleLocator(0.5))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('\n %d-%m'))
        ax.xaxis.set_minor_locator(MultipleLocator(0.07))
        ax.xaxis.set_minor_formatter(mdates.DateFormatter('%Hh'))
        plt.tight_layout()
        plt.savefig('./plots/plot_24h.png')
    else:
        df_48 = df[-nb_hour*12:]
        fig, ax = plt.subplots()
        ax.xaxis.grid(True, which='minor')
        ax.plot(df_48.index, df_48)
        ax.set_xlabel('Time')
        ax.set_ylabel('CA')
        ax.xaxis.set_major_locator(MultipleLocator(1))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('\n %d-%m'))
        ax.xaxis.set_minor_locator(MultipleLocator(0.17))
        ax.xaxis.set_minor_formatter(mdates.DateFormatter('%Hh'))
        plt.tight_layout()
        plt.savefig('./plots/plot_48h.png')
