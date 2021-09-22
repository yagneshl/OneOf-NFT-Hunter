import requests
import time
import json
import discord
import datetime
from discord import Webhook, RequestsWebhookAdapter, File

### Create webhook
##WEBHOOK_ID = 
##WEBHOOK_TOKEN = ""
##webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_TOKEN,\
## adapter=RequestsWebhookAdapter())

while True:
    jsn = requests.get('https://api.oneof.com/nft/marketplace/' + input("NFT Code:") + '?start=0&limit=1000')
    data = jsn.json()
    hunt = (data['results'])
    maxPrice = input("Enter max price ($USD):")
    
    for n in range(len(hunt)):
            if int(float(hunt[n]["price"])) < int(maxPrice):
                CURRENT_PRICE = ("OneOf Day One NFT #{} was listed for {} {}.".format(hunt[n]["sequence"], hunt[n]["price"], hunt[n]["seller"]))
                print (CURRENT_PRICE)
##                webhook.send("**" + str(datetime.datetime.now().strftime("%Y/%m/%d ""%H:%M:%S")) + "**: " + CURRENT_PRICE)

    time.sleep(300)
