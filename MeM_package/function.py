import os
from binance.client import Client
import datetime
import time
from dateutil.relativedelta import relativedelta
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
binance_api = ""   # Here API key from private binance account
secrete_key = ""   # Here secrete key from private binance account
# init
api_key = os.environ.get(binance_api)
# Set account, it allows to connect the code with the Web
api_secret = os.environ.get(secrete_key)  # Set account
client = Client(api_key, api_secret)   # Login

def create_timestamp(date):
    """This function translate the gregorian
    data format into Unix Timestamp usefull to call Binance API

    :return: The day
    :rtype: Timestamp
    """
    # Remove space and concatenate with second and milliseconds
    date_string = (date.replace(" ", "") + ", 00:00:00")
    # Transform the string in a DataTime object
    dtObj = datetime.strptime(date_string, "%m/%d/%Y, %H:%M:%S")
    # Transform in Timestamp and remove the last two digits
    timestamp = str(time.mktime(dtObj.timetuple()) * 1000)[:-2]
    # Return the str timestamp
    return str(timestamp)

def create_interval(given_date, end):
    """This function creates a new dictionary containing
    'as key the gregorian value and as value the timestamp

    :return: The values
    :rtype: Dictionary
    """
    
    # Create the dictionary object
    interval = {}
    # Save the start date
    interval[given_date] = {create_timestamp(given_date)}
    # Transform the string in a DataTime object
    dtObj = datetime.strptime(given_date,
                              '%m/%d/%Y')
    # Initialize the for loop to add the days
    # and create the Dictionaty interval
    for x in range(end):
        # start from day 1 (not 0)
        x += 1
        # Add one day to the Data Obj
        future_date = dtObj + relativedelta(days=x)
        # Transform DataObj to a string
        future_date_str = future_date.strftime(date_format)
        # Convert the string into Tinestamp and save it
        interval[future_date_str] = {create_timestamp(future_date_str)}
    # Return the Dicitionary
    return interval

def retrieve_binance_data(interval):
    """This function retrieves the data from the binance 
    'servers for a given interval of time

    :return: The values
    :rtype: List"""

    data = []
    dates = interval.keys()
    for date in dates:
        # print(date)
        timestamp = str(interval[date]).replace("{",
                                                "").replace("}",
                                                            "").replace("'",
                                                                        "")
        new_data = client.get_historical_klines('BTCUSDT',
                                                '1M',
                                                timestamp, 
                                                limit=1000)
        data = data+new_data
    return data
