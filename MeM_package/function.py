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

