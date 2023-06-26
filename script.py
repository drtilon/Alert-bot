import json
from web3 import Web3
import os
from twilio.rest import Client
import time

config = json.load(open('config.json'))


# checks if the provider is valid 
def check_provider(tlos_providers):
    for provider in tlos_providers:
        if tlos_provider := Web3(Web3.HTTPProvider(provider)):
            return tlos_provider

def main():
    tlos_provider = check_provider(config["telos_mainnet"])
    # get_balance fn return tlos price without dot, so needed to devide by "point"
    point = 1000000000000000000
    # user’s environmental variables
    ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
    AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    # a loop that will go over all the accounts and will check if the balance is sufficient enough
    addresses = config["addresses"]

    for name, address_price in addresses.items():
        if(address_price[1] > tlos_provider.eth.get_balance(address_price[0]) / point):
            # from = number of sender / body = the body of the message / to = number of receiver
            message = client.messages.create(
                from_='+XXXXXXXX',
                body='hello your balance in '+ str(name)+" is insufficient",
                to='+XXXXXXXXX'
            )
            print(message.sid)


if __name__ == '__main__':
    main()
    time.sleep(config["interval_sec"])
