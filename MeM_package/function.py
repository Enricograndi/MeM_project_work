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
    'This function translate the gregorian
    'data format into Unix Timestamp usefull to call Binance API'
    # Remove space and concatenate with second and milliseconds
    date_string = (date.replace(" ", "") + ", 00:00:00")
    # Transform the string in a DataTime object
    dtObj = datetime.strptime(date_string, "%m/%d/%Y, %H:%M:%S")
    # Transform in Timestamp and remove the last two digits
    timestamp = str(time.mktime(dtObj.timetuple()) * 1000)[:-2]
    # Return the str timestamp
    return str(timestamp)
