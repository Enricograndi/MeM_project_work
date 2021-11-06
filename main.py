#Import all the packaged required the function of the package
import os
from binance.client import Client
import pandas as pd
from MeM_package import function as mem
from datetime import datetime
# Here API key from private binance account
binance_api = "" 
# Here secrete key from private binance account
secrete_key = ""
#Set account
api_key = os.environ.get(binance_api)
#Set account
api_secret = os.environ.get(secrete_key)
#Create connection
client = Client(api_key, api_secret)
#use the custom function to transform timestamp
timestamp = mem.create_timestamp('1/21/2017')
#Call the Binance data to download the data
binance_data = client.get_historical_klines('BTCUSDT', #symbol
                                            '1d', #interval
                                            timestamp, #start interval
                                            limit=1000)#Api Limit
#Create the Pandas df
df_binance = pd.DataFrame(binance_data)
#Rename the coloumns
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
#Transform the timestamp into data
df_binance['Open time'] = pd.to_datetime(df_binance['Open time'], unit="ms")
#Transform the timestamp into data
df_binance['Close time'] = pd.to_datetime(df_binance['Close time'], unit="ms")
#Save the CSV
df_binance.to_csv("Data/binance_data.csv")

