from accounts import Accounts
from report_generator import generate_report
from emailer import sendReport
import random
import datetime
import sys
import select
import time

created_accounts={}
def monitorNewAccounts():
    #time when emails will be sent
    start = datetime.time(16,59)
    end = datetime.time(17, 00)
    while (datetime.datetime.now().time()<start or datetime.datetime.now().time()>end):

        #takes input through keyboard on 20 second timer (so it doesnt get tied up when reports get emailed)
        stringer=timed_Input()

        #if there was an email
        if(stringer!=None):
            #parses the input message
            message = stringer.split(",")

            #if the message is saying to create a new account with signal "0000"
            if(message[0] =="0000"):
                if(len(message)>=10):
                # creates new user with an email
                     new_account=Accounts(float(message[1]),float(message[2]),float(message[3]),float(message[4]),
                                          float(message[5]),float(message[6]), float(message[7]), float(message[8]), message[9])
               # email not included
                else:
                    new_account = Accounts(float(message[1]), float(message[2]), float(message[3]), float(message[4]),
                                           float(message[5]), float(message[6]), float(message[7]), float(message[8]))

                #creates new user id, if it already exists increments until finds number that doesnt exist
                new_id=random.randrange(1,999)
                while(new_id in created_accounts):
                    new_id=new_id+1

                #adds new account with new id to the existing accounts
                created_accounts[str(new_id)]=new_account

                #generate report
                reply=generate_report(str(new_id), created_accounts, True)

            #else the user already exists OR you need to create new account
            else:
                reply=generate_report(str(message[0]), created_accounts, False)

            #returns the report generated
            print (reply)
            print('\nEnter something.')

    #in time range to send reports so calls send reports and then loops back in
    sendReports()


def sendReports():
    # iterates through created accounts and if it contains email piece sends email with report
    print('Going to send reports piece.')
    for account in created_accounts:
        destination = (created_accounts[account].emailAddress)
        # the email address is not null so send email to destination with message
        if (destination != None):
            message = (generate_report(account, created_accounts, False))
            sendReport(destination,message)
    time.sleep(60)
    print('Starting to monitor again.')
    monitorNewAccounts()


#code adapted from https://stackoverflow.com/questions/1335507/keyboard-input-with-timeout-in-python from Pontus
def timed_Input():
    timeout = 10
    rlist, _, _ = select.select([sys.stdin], [], [], timeout)
    if rlist:
        s = sys.stdin.readline()
        return s
    else:
        return None




