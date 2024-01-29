Yahoo Candle Stick Scraper Documentation
============================
Yahoo Candle Stick Scraper is a Python library for extracting chart candle stick data out from [Yahoo Finance](https://finance.yahoo.com/). 
It parses data from the API requests. It saves time for user/programmer by scraping the realtime data.

Usage
===========

**Syntax:**

    import yahoocandles as ys
    
    ys.get_data(symbol: str, interval: str, exchange: str)

    
Quick Start
===========

**Sample Usage Snippet**
    
    import yahoocandles as ys
    
    data = ys.get_data(symbol="TATAPOWER", interval="1m", exchange="NSE")
    
    print(data)

**Sample Output**

This scraper will return the output as a dataframe. The user can export the output as excel/csv using pandas are 
other familiar libraries.

       Symbol	            Date	       Open	       High	       Low	      Close
0	TATAPOWER.NS	2024-01-23 09:15:00	360.000000	360.000000	358.399994	359.950012
1	TATAPOWER.NS	2024-01-23 09:16:00	359.399994	359.399994	356.600006	356.600006
2	TATAPOWER.NS	2024-01-23 09:17:00	356.549988	357.500000	355.850006	356.200012
3	TATAPOWER.NS	2024-01-23 09:18:00	356.200012	356.399994	354.950012	355.799988
4	TATAPOWER.NS	2024-01-23 09:19:00	355.799988	355.950012	355.149994	355.600006



Limitations
=========================
The version 0.0.1 of this scraper will work for all the symbols available in NSE and BSE exchange. The user need
to pass the stock symbol as per the stock exchange.
 
The user can pass time intervals as per the needs as "1m" for 1 Minute candles, "2m" for 2 Minute candles,
"5m" for 5 Minute candles, "15m" for 15 Minute candles, "1d" for 1 Day candles.

1 Minute candles are limited to 7 days before the date of scraping
2 Minute, 5 Minute, 15 Minute candles are limited to 50 days before the date of scraping
1 Day candles are limited to 180 days before the date of scraping

In the version 0.0.1 the user can only pass the Indian Stock Exchanges as "NSE" or "BSE".

Installing Yahoo Candle Stick Scraper
=========================

