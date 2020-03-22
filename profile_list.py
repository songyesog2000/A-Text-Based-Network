import argparse
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import nltk
import re
import json

nltk.download('stopwords')
parser = argparse.ArgumentParser(description='')
parser.add_argument('--tickers',  type=str)
args = parser.parse_args()

def read_profile(tic=None):
    if type(tic) is str:
        theurl = 'https://finance.yahoo.com/quote/' + tic +'/profile?p='+tic
    else:
        print('input data type is not a str of ticket')

    response = urlopen(theurl)
    tic_html = response.read()
    file1 = bs(tic_html,'html.parser')
    #Find description and get it in a string type
    text1 = file1.find("span", string="Description").parent.parent.p.text
    # lower case
    text1 = text1.lower()
    #remove punction
    text1 = re.sub(r'[^\w\s]', '', text1)
    #remove tokens including numbers
    #text1 = re.sub("^\d+\s|\s\d+\s|\s\d+$", "", text1)
    # remove stopwords

    sw = nltk.corpus.stopwords.words('english')
    text1 = ' '.join([ _ for _ in text1.split() if _ not in sw ])
    return text1


if __name__ == '__main__':
    if args.tickers is not None:
        tics = args.tickers.split(',')
    else:
        tics = ['JPM', 'BAC', 'GOOG', 'AAPL', 'MMM', 'AAC', 'T', 'VZ', 'XOM', 'CVX', 'KO', 'BUD']


    # use dictionary type to store profile_list
    profile_list = {}
    for tic in tics:
        try:
            profile_list.update({tic:read_profile(tic=tic)})
        except:
            print(tic,'may not be a ticker symbol')

    #save as a jason
    json = json.dumps(profile_list)
    f = open("profile_list.json", "w")
    f.write(json)
    f.close()








