import requests
import time
import json
##import discord
##import datetime
##from discord import Webhook, RequestsWebhookAdapter, File

### Create webhook - add webhookID and webhook token for your discord bot here and remove ## from the code below to uncomment (lines 9, 10, 11, 12, 24)
##WEBHOOK_ID = 
##WEBHOOK_TOKEN = ""
##webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_TOKEN,\
## adapter=RequestsWebhookAdapter())

while True:
    nftCode = input("NFT Code:")
    maxPrice = input("Enter max price ($USD):")
    print("Searching...")
    jsn = requests.get('https://api.oneof.com/nft/marketplace/' + nftCode + '?start=0&limit=1000')
    data = jsn.json()
    hunt = (data['results'])
    jsn2 = requests.get('https://api.oneof.com/nft/' + nftCode)
    meta = jsn2.json()
    nftName = (meta["title"])
        
    for n in range(len(hunt)):
            if int(float(hunt[n]["price"])) < int(maxPrice):
                CURRENT_PRICE = ("OneOf {} NFT #{} was listed for ${} by {}.".format(nftName, hunt[n]["sequence"], hunt[n]["price"], hunt[n]["seller"]))
                print (CURRENT_PRICE)
##                webhook.send("**" + str(datetime.datetime.now().strftime("%Y/%m/%d ""%H:%M:%S")) + "**: " + CURRENT_PRICE)

    time.sleep(300) #loops and refreshes search after 300s
