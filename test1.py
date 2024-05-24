from telethon import TelegramClient, events

api_id = '20135128'
api_hash = '69073faa2dd4ed77331bb2a243837534'
phone_number = '+16172859986'

client = TelegramClient(phone_number, api_id, api_hash)

@client.on(events.NewMessage(chats='testforotto'))
async def new_message_listener(event):
    print(f"Message from {event.chat_id}: {event.raw_text}")

client.start()
client.run_until_disconnected()
