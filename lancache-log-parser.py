import time
import requests
from discord_webhook import DiscordWebhook

## LogChannel 
LogChannel = "https://discordapp.com/api/webhooks/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
LogLocation = "/home/prefill/SteamPrefill-2.2.2-linux-x64/app.log"
UserTaggingEnabled = False
UserTagging = "<@DISCORDTAG>"

FirstRun = True
def SendToDiscord(DiscordMSG, webhooklink):
	webhook = DiscordWebhook(url=(webhooklink), content=(DiscordMSG))
	response = webhook.execute()


with open(LogLocation) as f:
    while True:
        line = f.readline()
        if not line:
            time.sleep(1)
            FirstRun = False
        else:
            if FirstRun == False:
                try:
                    print(line)
                    SendToDiscord(line, LogChannel)
                    if "Finished" in line and UserTaggingEnabled == True:
                        DiscordMSG = "Hey there, the prefill finished a update. Tagging: "+UserTagging
                        print(line)
                        SendToDiscord(DiscordMSG, LogChannel)
      
                except Exception as e:
                    print("Something went wrong.")
                    print(e)
                    try:
                        DiscordMSG = "Something went wrong in try, check logs - trying to send exception to Discord."
                        SendToDiscord(DiscordMSG, LogChannel)

                        DiscordMSG = e
                        SendToDiscord(DiscordMSG, LogChannel)
                    except:
                        print("Oof..")
