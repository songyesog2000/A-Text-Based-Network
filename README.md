# A-Text-Based-Network
This repo is a Python cover of the R-project, A Text-Based Network, by Majeed Simaan. The original R project refers to Rpubs: https://rpubs.com/simaan84/410145

### Summary
* [Basics](#Basics)
* [Company Profiles](#Company-Profiles)
* [Text-based Network](#Text-based-Network)

### Basics
This program is recommend to run with
- Python version 3.X.
- BeautifulSoup4
- nltk
- pyvis
- numpy
- textdistance
- pandas

Install by downloading the file from the github page, or using git code
Install via GitHub:
```bash
git clone https://github.com/songyesog2000/A-Text-Based-Network.git
```

### Company Profiles
The profiles of listing companies from Yahoo Finance, collected via Web mining. The python program for that executes as
```bash
python profiles_list.py --tickers [string of ticker symbols separated by ',']
```
if the ```--tickers [ticker symbol]``` is not provided, the program is default to collect profiles of 'JPM', 'BAC', 'GOOG', 'AAPL', 'MMM', 'AAC', 'T', 'VZ', 'XOM', 'CVX', 'KO', 'BUD'.
The collected profiles are stored in the json file ```profiles_list.json```.

###Text-based Network
The distance of the companies is defined by the [Jaro-winkler distance](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance) of their profiles.
Then, transfer the distance to truncated similarity values ( truncated by 0.25 in example ).
![example_W_similarity](https://github.com/songyesog2000/A-Text-Based-Network/blob/master/exampe_W_similarty.png)
Based on the similarity, a network graph is composed and stored in ```G.html```, the html file will show up the visualization in browsers.
![network graph](https://github.com/songyesog2000/A-Text-Based-Network/blob/master/network%20graph.png)

All the above process is integrated by running
```bash
python Text-based\ Network.py
```


