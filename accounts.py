class Accounts:

    """Attributes:
    btc_held (float)
    eth_held (float)
    ltc_held (float)
    btc_money (float)
    eth_money (float)
    ltc_money (float)
    """

    def __init__(self, btc_held=0, btc_money=0, bch_held=0, bch_money=0, eth_held=0, eth_money=0, ltc_held=0, ltc_money=0, emailAddress=None):
        self.btc_held=btc_held
        self.btc_money = btc_money
        self.bch_held=bch_held
        self.bch_money= bch_money
        self.eth_held=eth_held
        self.eth_money = eth_money
        self.ltc_held=ltc_held
        self.ltc_money=ltc_money
        self.emailAddress= emailAddress
#returns amount of bitcoin user has
    def get_btc_held(self):
        return float(self.btc_held)

#returns amount of USD user invested in BTC
    def get_btc_money(self):
        return float(self.btc_money)

# returns amount of bitcoin user has
    def get_bch_held(self):
         return float(self.bch_held)

# returns amount of USD user invested in BTC
    def get_bch_money(self):
            return float(self.bch_money)

#returns amount of etherum user has
    def get_eth_held(self):
        return self.eth_held

#returns amount of USD user invested in ETH
    def get_eth_money(self):
        return self.eth_money

#returns amount of litecoin user has
    def get_ltc_held(self):
        return self.ltc_held

#returns amount of USD user invested in LIT
    def get_ltc_money(self):
        return self.ltc_money

#returns total amount of USD invested
    def total_invested(self):
        return self.get_btc_money()+self.get_bch_money()+self.get_eth_money()+self.get_ltc_money()

