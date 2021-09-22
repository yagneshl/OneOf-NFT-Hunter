# Table of Contents:
* [About NFTHunter](#About-NFTHunter)
    * [Current Functionality](#Current-Functionality)
    * [Disclaimer](#Disclaimer) 
* [Installation](#Installation)
    * [Requirements](#Requirements)
    * [Quick Start](#Quick-Start)
* [Advanced Configuration](#Advanced-Configuration) 
    * [Discord Notifications](#Discord-Notifications)
    
# Quick Links
 * [Discord](https://discord.gg/gCx6VRnQhN) **DO NOT ASK QUESTIONS IN DISCORD BEFORE READING THIS DOCUMENT**
 * [Python Download (3.9.7)](https://www.python.org/downloads/release/python-397/)

# About OneOf NFTHunter
A data scraping tool for notifying user of new listings and showing prices of Non-Fungible Tokens (NFTs) listed on OneOf.com

**If everyone is botting, then no one is botting.**

## Current Functionality

NFT Hunter only works on OneOf.com and can run on a 5min loop to notify you through the console or through a bot on your personal discord server.
![image](https://raw.githubusercontent.com/yagneshl/OneOf-NFT-Hunter/main/Images/example1.png)

### Other Notes on Functionality
* NFT Hunter is designed to check if the specified NFT has a listed price in the NFT marketplace, errors in the OneOf database can break functionality of NFTHunter.  

### Disclaimer 

WARNING: The use of this software can result in OneOf and other service providers restricting access to your account and make it difficult for you to purchase products. By using this software, you acknowledge these risks. These restrictions cannot and will not be resolved by the developer, nor can they be detected/resolved by the standard Customer Support. If this happens, the only resolution is to stop all bots, wait, and hope the limits are lifted within a few days. If this is a major issue you should consider avoiding use of this software. 

Account restrictions may be triggered by any of the following: 1) running multiple instances on one device, 2) configuring an instance to check stock too frequently/aggressively (default settings not guaranteed to be safe). 

Symptoms of account restrictions include: 1) frequent CAPTCHA checks, 2) inability to access the My Account page. You’ll likely have to sit-out a few days of drops to resolve the throttle.

# Installation

## Requirements

Python 3+ is required. It is best if you use the newest version of **3.9** (at this time, 3.9.7) but earlier version should also work. 

Running it on a potato (<2GB of RAM) is not suggested. 

## Quick Start

Here are the very simple steps for running the bot on Windows, however most of these instructions should be followed
regardless of your OS (obviously you aren't running .bat files if you aren't on Windows, or using GitHub Desktop if not 
available on your OS). See [Platform Specific](#Platform-Specific) instructions for help installing Python and
dependencies in other operating systems:
1. [Install Python](https://www.python.org/downloads/release/python-397/). Install to some location that does not include spaces in the path 
   (I suggest C:\Python39). Click the checkbox that says Add Python 3.9 to PATH (or something similar) 
   during the installation.  
2. Install the following dependencies using pip or any other package manager. For Windows, open up a terminal and type the following:
```
py -m pip install requests
```
```
py -m pip install time
```

Additional packages for discord notifications
```
py -m pip install discord
```
```
py -m pip install datetime
```
3. Download the project as a zip and run the script.
4. Identify NFT code by opening the marketplace page for the NFT you want to track and looking at the URL. The NFT code will be between /nft/ and /marketplace-auction/: https://www.oneof.com/nft/{NFTcode}/marketplace-auction
![image](https://raw.githubusercontent.com/yagneshl/OneOf-NFT-Hunter/main/Images/step4.png)
5. Run the script and input the NFT code identified in step 5 along with max price.
6. ???
7. Profit

# Advanced Configuration 
## Discord Notifications

Notifications can be set up using Discord webhooks. You can generate a webhook for a notification bot on your server under the Itegrations menu in the channel settings of your personal notification server. 

![image](https://raw.githubusercontent.com/yagneshl/OneOf-NFT-Hunter/main/Images/discord1.png)
![image](https://raw.githubusercontent.com/yagneshl/OneOf-NFT-Hunter/main/Images/discord2.png)

Once you create an integration, copy the webhook link. It should be in the following format: https://discord.com/api/webhooks/{WebhookID}/{WebhookToken}

![image](https://raw.githubusercontent.com/yagneshl/OneOf-NFT-Hunter/main/Images/discord3.png)

Add {WebhookID} and {WebhookToken} to the top of the script and uncomment (remove ##).

# Issues Running NFTHunter 
## Known Issues
* Null price entries in the OneOf database break functionality and will require a restart of the program once the error is fixed. This is often quickly resolved by the team but may take them some time.
* Installing dependency packages may result in errors. Try troubleshooting by searching the exact error message on Google

# Tips
If I helped make you some money or you just liked the software and would like to let me know, here's my XTZ wallet address: tz1VEXmGT8skqGGmcZgpuxwFUJXgBaMBuzDa
