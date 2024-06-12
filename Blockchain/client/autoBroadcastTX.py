import requests
import time
import random
from Blockchain.Backend.core.database.database import AccountDB

fromAccount = "15TFGsvgTh4we2T4Q7nxMy3YP3TcN14FoJ"

""" Read all the accounts """
AllAccounts = AccountDB().read()

def autoBroadcast():
    while True:
        for account in AllAccounts:
            if account["PublicAddress"] != fromAccount:
                paras = {"fromAddress": fromAccount,
                        "toAddress": account["PublicAddress"],
                        "Amount": random.randint(1,35)}

                #res = requests.post(url ="http://localhost:5900/wallet", data = paras)   
        time.sleep(1)