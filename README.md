# MeM_project_work

In this repository you can find a file named ```main.py```, which permit to retrieve the data from Binance exchange.

[Binance](https://binance.com//) is an on-line crypto exchange,  it is the worlds biggest bitcoin exchange and altcoin crypto exchange in the world by volume. 
[API documentation page](https://binance-docs.github.io/apidocs/spot/en/#introduction).

> **Note:** the package requires the following modules to run:
*os, binance.client, datetime, time, dateutil.relativedelta, pandas, matplotlib*.

It also require an account in order to generate the API Key



## Documentation 
Documentation can be found in: ```docs/html/index.html``` and provides infos about the functions you can find in the various modules.
 

**DOCUMENTATION MADE WITH: [Sphinx](http://www.sphinx-doc.org/en/master/).**


## How to retrieve data

From the command line, open the package and run main.py
```
python main.py 

```

## Where can I find the data?
The data will be saved as CSV on "Data" folder. 

## Data explaination

In this documentation there are ten variables and 48652 records which describe the Bitcoin trend in dollars from August 1, 2017 to October 1, 2021. Data are written in the form of klines, also known as Candlestick, that packs a lot of trade history information into a single data point.

- Open time:	the starting interval time that you set when you retrieve data.
- Open: the value the data acquires at the beginning of the day. 
- High:	the maximum value the data acquires at the beginning of the day.
- Low: the lowest value the data acquires at the beginning of the day.
- Close:  the value the data acquires at the end of the day.
- Volume: the volume of the transaction.
- Close time:	the closing interval time that you set when you retrieve data.
- Quote asset volume: the quantity that is traded at the quoted price.
- Number of trades:the number of Bitcoins processed on a single day.
- Taker buy base asset volume:the amount of of traded coins in the timeframe that were received by the buyer.
- Taker buy quote asset volume:the amount of traded coins in the timeframe paid by the buyer.
- Ignore: Ingore



## API settings

In order to download the data, you have to create your own account on Binance. Next you will have to generate
your personal key. Finally, you have to set the keys generated on the main.py in the dedicated variable.

## Support
You need help? Get in touch with the authors on [Linkedin](https://www.linkedin.com/)!

## Authors and acknowledgment
Thank you all for the collaboration! Follow the authors on linkedin!

- [**Enrico Grandi**](https://www.linkedin.com/in/enrico-grandi/)
- [**Martina Crisafulli**](https://www.linkedin.com/in/martina-crisafulli-58a006209/)
- [**Martina Manno**](https://www.linkedin.com/in/martina-manno-41a6a41a2/)



## License
[GPL](https://www.gnu.org/licenses/gpl-3.0.html)
