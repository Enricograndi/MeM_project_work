# MeM_project_work

In this repository you can find a file named ```main.py```, which permit to retrieve the data from Binance exchange.

[Binance](https://binance.com//) is an on-line crypto exchange,  it is the worlds biggest bitcoin exchange and altcoin crypto exchange in the world by volume. 
[API documentation page](https://binance-docs.github.io/apidocs/spot/en/#introduction).

> **Note:** the package requires the following modules to run:
*os, binance.client, datetime, time, dateutil.relativedelta, pandas, matplotlib*.

It also require an account in order to generate the API Key



## Documentation 
Documentation can be found in: ```docs/html/index.html``` and provides infos about the functions you can find in the various modules.
 
To read them with your **default browser**, from the main folder use ```$ open docs/html/index.html``` or, for other browsers you may have installed, follow these examples:
- **Chrome:** ```$ open -a "Google Chrome" docs/html/index.html```
- **Safari:** ```$ open -a "Safari" docs/html/index.html```


**DOCUMENTATION MADE WITH: [Sphinx](http://www.sphinx-doc.org/en/master/).**


## How to retrieve data

From the command line, open the package and run main.py
```
python main.py 

```

## Where can I find the data?
The data will be saved as CSV on "Data" folder. It will present also a plot.


## API settings

In order to download the data, you have to create your own account on Binance. Next you will have to generate
your personal key. Finally, you have to set the keys generated on the function.py in the dedicated variable.

## Support
You need help? Get in touch with the authors on [Linkedin](https://www.linkedin.com/)!

## Authors and acknowledgment
Thank you all for the collaboration! Follow the authors on linkedin!

- [**Enrico Grandi**](https://www.linkedin.com/in/enrico-grandi/)



## License
[GPL](https://www.gnu.org/licenses/gpl-3.0.html)