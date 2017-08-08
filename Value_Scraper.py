import requests
from bs4 import BeautifulSoup

#module no longer used because of changes in coinbase html

#scrapes values off coinbase to current current trading prices of bitcoin, etherum, and litecoin
page= requests.get("https://www.coinbase.com/charts")
soup=BeautifulSoup(page.content, "html.parser")
prices=soup.find_all("span",{"class": "charts-currency-price"})

#bitcoin's trading price
def get_BTC_price():
    return prices[0].contents[3].text

#float representation of btc price
def get_BTC_value():
    return float(get_BTC_price()[1:-4].replace(",",""))

#etherum's trading price
def get_ETH_price():
    return prices[1].contents[3].text

#float representation of eth price
def get_ETH_value():
    return float(get_ETH_price()[1:-4].replace(",",""))

#litecoin's trading price
def get_LIT_price():
    return prices[2].contents[3].text

#float represntation of lit trading price
def get_LIT_value():
    return float(get_LIT_price()[1:-4].replace(",",""))


#prices = soup.find_all("div", {"class": "Flex__FlexBox-gYXKYY bynKgY"})

