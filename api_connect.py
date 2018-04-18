from coinbase.wallet.client import Client
import warnings

#because of bug in original api code, api is installed using https://github.com/coinbase/coinbase-python/tree/f9ed2249865c2012e3b86106dad5f8c6068366ed

#supresses warnings about including date header in coinbase package
warnings.filterwarnings("ignore")
client = Client(apiKeyInfo)

#bitcoin's trading price
def get_BTC_price():
    return "$"+client.get_sell_price(currency_pair = 'BTC-USD').get("amount")

#float representation of btc price
def get_BTC_value():
    return float(client.get_sell_price(currency_pair = 'BTC-USD').get("amount"))

#bitcoin cash's trading price
def get_BCH_price():
    return "$"+client.get_sell_price(currency_pair = 'BCH-USD').get("amount")

#float representation of bch price
def get_BCH_value():
    return float(client.get_sell_price(currency_pair = 'BCH-USD').get("amount"))

#etherum's trading price
def get_ETH_price():
    return "$"+client.get_sell_price(currency_pair = 'ETH-USD').get("amount")

#float representation of eth price
def get_ETH_value():
    return float(client.get_sell_price(currency_pair = 'ETH-USD').get("amount"))

#litecoin's trading price
def get_LIT_price():
    return "$"+client.get_sell_price(currency_pair = 'LTC-USD').get("amount")

#float represntation of lit trading price
def get_LIT_value():
    return float(client.get_sell_price(currency_pair = 'LTC-USD').get("amount"))


