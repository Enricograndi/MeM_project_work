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

    #open the file
df_binance = pd.read_csv("../Data/binance_data.csv")

#To int
df_binance["Open"] = pd.to_numeric(df_binance["Open"])
df_binance["Close"] = pd.to_numeric(df_binance["Close"])
df_binance["High"] = pd.to_numeric(df_binance["High"])
df_binance["Low"] = pd.to_numeric(df_binance["Low"])
df_binance["Open time"] = pd.to_datetime(df_binance["Open time"])

#Calculate the difference between opening and closing
df_binance["Open-Close"] = df_binance["Open"]-df_binance["Close"]
#Calculate the difference between daily highest and lowest values
df_binance["High-Low"] = df_binance["High"]-df_binance["Low"]
#Calculate the percentual between daily highest and lowest values
df_binance["Percentual Increase(High low)"] = df_binance["High-Low"]/df_binance["High"]*100
#Calculate the percentual between opening and closing
df_binance["Percentual Increase(Open close)"] = df_binance["Open-Close"]/df_binance["Open"]*100
#drop columns
df_binance = df_binance.drop(columns=["Unnamed: 0", "Ignore"])

#declare a figure of 3 rows and 2 columns
fig, axs = plt.subplots(3, 2,figsize=(15,15))

# Read the boxplot from left to right
# first box plot
axs[0, 0].boxplot(df_binance["Percentual Increase(High low)"])
axs[0, 0].set_title('Percentual Increase(High low)')

# second boxplot
axs[0, 1].boxplot(df_binance["Percentual Increase(Open close)"], 1)
axs[0, 1].set_title('Percentual Increase(Open close)')

# third boxplot
axs[1, 0].boxplot(df_binance["Open"], 1)
axs[1, 0].set_title('Open')

# fourth boxplot
axs[1, 1].boxplot(df_binance["Close"], 1)
axs[1, 1].set_title('Close')

# fifth boxplot
axs[2, 0].boxplot(df_binance["High"], 1)
axs[2, 0].set_title('High')
# sixt boxplot
axs[2, 1].boxplot(df_binance["Low"], 1)
axs[2, 1].set_title('Low')

print("In order to understand the shape of the data, we are going to plot the boxplot of the most important coulmns. We can see that for all the columns there are a lot of outliers, meawhile the median values are equally distributed to the bottom of the boxplots.") 
input("Press Enter to continue...")

fig.suptitle("Boxplot", fontsize=16)
plt.show()
