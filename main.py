#Import the function of the package
from MeM_package import function as mem
import pandas as pd
import matplotlib.pyplot as plt
#Use the function to download the binance data
binance_data = mem.retrieve_binance_data(mem.create_interval('1/21/2017', 1745))
#Create the Pandas df
df_binance = pd.DataFrame(binance_data)
#Transform the timestamp of the df on a gregorian data
df_binance[0] = pd.to_datetime(df_binance[0], unit='ms')
#Rename the coulmn
df_binance = df_binance.rename(columns={0 : 'Open time',
                                        1 : 'Open', 
                                        2 : 'High', 
                                        3 : 'Low', 
                                        4 : 'Close', 
                                        5 : 'Volume', 
                                        6 : 'Close time', 
                                        7 : 'Quote asset volume', 
                                        8 : 'Number of trades', 
                                        9 : 'Taker buy base asset volume', 
                                        10 : 'Taker buy quote asset volume', 
                                        11:'Ignore'})
#Set the data as index
df_binance_data_as_index = df_binance.set_index("Open time")
#Create the plot
df_binance_data_as_index['Open'].astype(float).plot(linewidth=0.5)
#Save the plot
plt.savefig('Data/BTCUSDT_binace_plot.png')
#Save the df as csv
df_binance.to_csv("Data/binance_data.csv")
