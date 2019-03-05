 from discord_webhook import DiscordWebhook

 hookurl = 'https://discordapp.com/api/webhooks/540255081736568842/46WlEOEtXksA0heFXEU########################'

def discosend(message):
    webhook = DiscordWebhook(url=hookurl, content=message)
    webhook.execute()

def main():
    discosend('First message')

if __name__ == '__main__':
    main()
