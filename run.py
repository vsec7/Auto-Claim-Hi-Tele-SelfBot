import time
from telethon import TelegramClient, sync

# Simple Auto claim hi.com Telegram Bot
# Crafted by cath / viloid (github.com/vsec7)

# Configurations
# Get api_id & api_hash from https://my.telegram.org/
api_id = 14483301
api_hash = 'b2c60a18d2d213a9056a3658ea684bf9'

client = TelegramClient('session', api_id, api_hash).start()
to = client.get_entity("hiofficialbot")

def main():	
  client.send_message(entity=to, message="👋 Claim Daily Reward")
  time.sleep(10)
  msg = client.get_messages("hiofficialbot")[0].click(0)


while True:
  main()
  time.sleep(90000) # 90000 seconds = 25 hours 
