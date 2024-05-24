from telethon import TelegramClient, events

api_id = 'your_api_id'
api_hash = 'your_api_hash'
phone_number = 'your_phone_number'

client = TelegramClient(phone_number, api_id, api_hash)

# Specify the chat IDs or usernames of the channels or groups
channels_or_groups = ['channel_or_group_username1', 'channel_or_group_username2', 123456789]  # mix of usernames and IDs

@client.on(events.NewMessage(chats=channels_or_groups))
async def new_message_listener(event):
    print(f"Message from {event.chat_id}: {event.raw_text}")

client.start()
client.run_until_disconnected()
