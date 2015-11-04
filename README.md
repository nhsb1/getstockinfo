# getstockinfo 

![screenshot1](https://cloud.githubusercontent.com/assets/12847315/10928331/722101be-8275-11e5-943d-83bd0010835a.jpg)

When supplying a list of tickersymbols (e.g. watchlist.txt), getstockinfo will filter the output based on the command line arguments specified.  

File/watchlist: '-f watchlist.txt', using a watchlist text file, which contains one valid Yahoo Finance ticker symbol per line, getstockinfo will loop though each ticker and capture relevent information, and output a report based on the command line arguments specified.  See the sample watchlist.txt file provided for sample data.

Index prices: '-ip', getstockinfo will output the S&P 500 price information (current price, change, and percent change) for today's session.

Outperformance: '-op' getstockinfo will will produce a list of stocks that are outperforming the S&P 500 index on a percentage basis during today's trading session, along with relevent ticker information for each outperforming equity (percent change, percent of average volume, and price).  This feature is designed to be used with '-ip'. 

Volume: '-v', based on the specified watchlist, getstockinfo will list each ticker where today's volume exceeds the average volume.

New High: '-nh', based on the specified watchlist, getstockinfo will list each ticker that is hitting a 52-week high for today's trading session.

New Low: '-nl', based on the specified watchlist, getstockinfo will list each ticker that is hitting a 52-week low for today's trading session.

Winner List: '-wl', based on the specified watchlist, getstockinfo will list each ticker that is trading in positive terriority during today's trading session.

Looser List: '-ll', based on the specified watchlist, getstockinfo will list each ticker that is trading in negative terriority during today's trading session.

Debug/detail: '-d', debug mode will output the details for each item specified in the watch list.


Install
-------

    pip install getstockinfo

Usage
-----

    getstockinfo -v -nl -wl -ll -ip -op -nh -f watchlist.txt

See Also
--------

For more information: https://pypi.python.org/pypi/getstockinfo
