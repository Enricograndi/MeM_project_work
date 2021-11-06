import datetime
import time
from datetime import datetime


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

