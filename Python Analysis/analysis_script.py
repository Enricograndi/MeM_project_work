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

#declare the figure
fig = plt.figure(figsize=(10,6))
#Fit function : y = mx + c [linear regression ]
ax = fig.add_axes([0,0,1,1])

#linear regression
x = np.arange(df_binance["Open time"].size)
fit = np.polyfit(x, df_binance["Open"], deg=1)

fit_function = np.poly1d(fit)
#Linear regression plot
ax.plot(df_binance["Open time"], fit_function(x))
ax.plot(df_binance["Open time"],df_binance["Open"], color="blue")

#linear regression grade 3
x = np.arange(df_binance["Open time"].size)
fit = np.polyfit(x, df_binance["Open"], deg=3)
fit_function = np.poly1d(fit)
#Linear regression plot
ax.plot(df_binance["Open time"], fit_function(x))
#Real Values plot
ax.plot(df_binance["Open time"],df_binance["Open"], color="green")



# Set the x-axis values
dtFmt = mdates.DateFormatter('%Y-%m') # define the formatting
plt.gca().xaxis.set_major_formatter(dtFmt) # apply the format to the desired axis
#Set the legend
ax.legend(['Real Value','Regression line grade 1', 'Regression line grade 3'])
#Set x-y labels
plt.xlabel("Date")
plt.ylabel("BTC opening values")

text = ("Here we find some different timeseries, the first with two different regression lines. One regression line has degree 1 Anohter regression line has degree 3 which fit better the distribution of the data")
print(text) 
input("Press Enter to continue...")
print("")
print ("Regression line grade 1 Slope : " + str(fit[0]))
print ("Regression line grade 1 Intercept : " + str(fit[1]))
ax.set_title("Time series of the BTC values")
plt.show()

#declare the figure
fig = plt.figure(figsize=(10,6))
ax = fig.add_axes([0,0,1,1])

# Plot the values
# We are going to normalize to visualize all the lines
ax.plot(df_binance["Open time"],df_binance["Open"]/max(df_binance["Open"]), color="green")
ax.plot(df_binance["Open time"],df_binance["Close"]/max(df_binance["Close"]), color="red")
ax.plot(df_binance["Open time"],df_binance["Open-Close"]/max(df_binance["Open-Close"]), color="blue")

# Set the axis values
dtFmt = mdates.DateFormatter('%Y-%m') # define the formatting
plt.gca().xaxis.set_major_formatter(dtFmt) # apply the format to the desired axis
ax.legend(['Normalized Open Value', 'Normalized Close Value',"Normalized diff" ])
plt.xlabel("Date")
plt.ylabel("BTC opening values")



text = ("Here we find some different timeseries, the open, close and the difference betweene the daily values. The values are normalized to the max values of the variable in order to allow to see the lines")
print(text) 
input("Press Enter to continue...")
ax.set_title("Time series of the BTC normalized open and close values and its difference")
plt.show()

#declare the figure
fig = plt.figure(figsize=(10,6))
ax = fig.add_axes([0,0,1,1])

# Plot the values
# We are going to normalize to visualize all the lines

ax.plot(df_binance["Open time"],df_binance["Open"]/max(df_binance["Open"]), color="green")
ax.plot(df_binance["Open time"],df_binance["Number of trades"]/max(df_binance["Number of trades"]), color="red")

#Set the lables
dtFmt = mdates.DateFormatter('%Y-%m') # define the formatting
plt.gca().xaxis.set_major_formatter(dtFmt) # apply the format to the desired axis
ax.legend(['Normalized Open Value', 'Normalized Number of trades'])
plt.xlabel("Date")
plt.ylabel("BTC opening values")

text = ("Here we find some different timeseries, the open and Number of trades. The values are normalized to the max values of the variable in order to allow to see the lines")
print(text) 
input("Press Enter to continue...")
ax.set_title("Time series of the BTC open and Number of trades")
plt.show()
