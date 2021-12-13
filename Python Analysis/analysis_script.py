import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import DateFormatter, DayLocator
import datetime
import matplotlib.dates as mdates
import seaborn as sns

def calculator(capital,dayI,dayF):
    #Find the values of first day
    df_i = df_binance[df_binance["Open time"]==dayI]
    #Find the values of last day
    df_f = df_binance[df_binance["Open time"]==dayF]
    #calculate the last value
    percentual_increase = ((df_f["Open"].iloc[-1]-df_i["Open"][0])/df_i["Open"][0])*100
    #print the findings
    print("Percentual increase: ", percentual_increase,"%")
    print("If you had invested ",capital," in ",dayI, " and disinvested in "
          , dayF," you would have earned ", ((percentual_increase*capital)/100)-capital)
