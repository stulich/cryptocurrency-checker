import api_connect
from accounts import Accounts

#given a user id (key) for a dictionary off accounts a report of profits for each currency
#is generate along with a total profit report
def generate_report(message, dictionary, new_account):
    bit_output=""
    bch_output=""
    eth_output=""
    lit_output=""
    bit_profit=0
    bch_profit=0
    eth_profit=0
    lit_profit=0
    #if account is new special output is at the begining of report, otherwise empty string is there
    is_new=""
    if (new_account is True):
        is_new="New account created. Your user ID is %s. In future send only user id to get report." %(message)

    #checks for new and existing accounts
    #if the message is a valid user_id a report generated is info on holdings
    if (message in dictionary.keys()):

        account = dictionary[message]
        # if the user possesed bitcoin
        btc_holdings=0
        if(account.get_btc_held()!=0):
             btc_holdings= account.get_btc_held()*api_connect.get_BTC_value()
             bit_profit= ((btc_holdings-account.get_btc_money()))
             percentage_gain= ((bit_profit/account.get_btc_money())*100)
             if(percentage_gain)>0:
                 placement="Up"
             elif(percentage_gain)==0:
                 placement=""
             else:
                 placement="Down"
             bit_output="\nBITCOIN (Currently "+api_connect.get_BTC_price()+") \n" \
                    "Current Holdings: $%.2f\n" \
                    "Profit: $%.2f (%s %.2f%%)\n" %(btc_holdings,bit_profit,placement,abs(percentage_gain))

        #if user possessed bitcoin cash
        bch_holdings=0
        if (account.get_bch_held() != 0):
            bch_holdings = account.get_bch_held() * api_connect.get_BCH_value()
            bch_profit = ((bch_holdings - account.get_bch_money()))
            percentage_gain = ((bch_profit / account.get_bch_money()) * 100)
            if (percentage_gain) > 0:
                placement = "Up"
            elif (percentage_gain) == 0:
                placement = ""
            else:
                placement = "Down"
            bch_output = "\nBITCOIN CASH (Currently " + api_connect.get_BCH_price() + ") \n" \
                                                                                 "Current Holdings: $%.2f\n" \
                                                                                 "Profit: $%.2f (%s %.2f%%)\n" % (
                                                                                 bch_holdings, bch_profit, placement,
                                                                                 abs(percentage_gain))

        #if the user possesed etherum
        eth_holdings=0
        if (account.get_eth_held() != 0):
            eth_holdings = account.get_eth_held() * api_connect.get_ETH_value()
            eth_profit = ((eth_holdings - account.get_eth_money()))
            percentage_gain = ((eth_profit / account.get_eth_money()) * 100)
            if (percentage_gain) > 0:
                placement = "Up"
            elif (percentage_gain) == 0:
                placement = ""
            else:
                placement = "Down"
            eth_output = "\nETHERUM (Currently "+api_connect.get_ETH_price()+") \n" \
                     "Current Holdings: $%.2f\n" \
                     "Profit: $%.2f (%s %.2f%%)\n" % (eth_holdings, eth_profit, placement, abs(percentage_gain))

        #if the user possed litecoin
        ltc_holdings=0
        if (account.get_ltc_held() != 0):
            ltc_holdings = account.get_ltc_held() * api_connect.get_LIT_value()
            lit_profit = ((ltc_holdings - account.get_ltc_money()))
            percentage_gain = ((lit_profit / account.get_ltc_money()) * 100)
            if (percentage_gain) > 0:
                placement = "Up"
            elif (percentage_gain) == 0:
                placement = ""
            else:
                placement = "Down"
            lit_output = "\nLITECOIN (Currently "+api_connect.get_LIT_price()+") \n" \
                         "Current Holdings: $%.2f\n" \
                         "Profit: $%.2f (%s %.2f%%)\n" % (ltc_holdings, lit_profit, placement, abs(percentage_gain))

        #for total holdings
        #total_holdings= "\nTotal holdings: $%.2f"%(btc_holdings+bch_holdings+eth_holdings+ltc_holdings)

        #for total gains and losses
        total_profit=bit_profit+bch_profit+eth_profit+lit_profit
        total_percent_gain=(((total_profit)/account.total_invested())*100)
        if(total_percent_gain>0):
            total_placement="Up"
        elif(total_percent_gain==0):
            total_placement=""
        else:
            total_placement="Down"
        total_output=("\nTotal Profit: $%.2f (%s %.2f%%)" %(total_profit, total_placement, abs(total_percent_gain)))


        #returns individual reports of each currency and total, if currency was not possesed it's output is an empty string
        #return (is_new + bit_output + eth_output + lit_output + total_holdings + total_output)
        return (is_new+bit_output+bch_output+eth_output+lit_output+total_output)


    #the account is not a new account and does not exist, gives directions on how to set up account
    else:
        output_string="User Id not recognized. To create an account send a message with the number '0000' followed by" \
                      " the amount of bitcoin you have, the amount of money you paid for it, the amount of bitcoin cash you have, the amount of money you paid for it,, the amount of etherum you" \
                      " have, the amount of money you paid for it, and the amount of litecoin you have and the amount " \
                      " you paid for it. Please seperate each number by a comma. If you do not possess a certain currency " \
                      " enter in it's value with a 0. Finally add an email if you would like to receive a report generated" \
                      " daily and sent to your email."
        return output_string



