Yahoo Candle Stick Scraper Documentation
============================
Yahoo Candle Stick Scraper is a Python library for pulling chart candle stick data out of [Yahoo Finance](https://finance.yahoo.com/). 
It parses data from the API requests. It saves time for user/programmer by pulling the realtime
data.

Usage
===========

**Syntax:**

    import yahoocandles as ys
    
    ys.get_data(symbol: str, interval: str, exchange: str)

    
Quick Start
===========

**Sample Usage Snippet**
    
    import yahoocandles as ys
    
    data = ys.get_data(symbol="TATAPOWER", interval="1m",exchange="NSE")
    
    print(data)

Limitations
=========================
 The version 0.0.1 of this scraper will work for all the symbols available in NSE and BSE exchange. The user need
 to pass the symbol as per the exchange.

 The user can pass time intervals as per the needs as "1m" for 1 Minute candles, "2m" for 2 Minute candles,
 "5m" for 5 Minute candles, "15m" for 15 Minute candles, "1d" for 1 Day candles.

 1 Minute candles are limited to 7 days before the date of scraping
 2 Minute, 5 Minute, 15 Minute candles are limited to 50 days before the date of scraping
 1 Day candles are limited to 180 days before the date of scraping


Installing Yahoo Candle Stick Scraper
=========================

If you're using a recent version of Debian or Ubuntu Linux, you can
install Beautiful Soup with the system package manager:

    $ apt-get install python-bs4`

Beautiful Soup 4 is published through PyPi, so if you can't install it
with the system packager, you can install it with ``easy_install`` or
``pip``. The package name is ``beautifulsoup4``, and the same package
works on Python 2 and Python 3.

    $ easy_install beautifulsoup4`

    $ pip install beautifulsoup4`

(The ``BeautifulSoup`` package is probably `not` what you want. That's
the previous major release, `Beautiful Soup 3`_. Lots of software uses
BS3, so it's still available, but if you're writing new code you
should install ``beautifulsoup4``.)

If you don't have ``easy_install`` or ``pip`` installed, you can
download the Beautiful Soup 4 source tarball
<http://www.crummy.com/software/BeautifulSoup/download/4.x/> and
install it with ``setup.py``.

    $ python setup.py install`

If all else fails, the license for Beautiful Soup allows you to
package the entire library with your application. You can download the
tarball, copy its ``bs4`` directory into your application's codebase,
and use Beautiful Soup without installing it at all.

I use Python 2.7 and Python 3.2 to develop Beautiful Soup, but it
should work with other recent versions.
