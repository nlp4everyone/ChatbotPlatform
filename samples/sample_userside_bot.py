from telethon import TelegramClient
from config import params

group_link = "https://t.me/+t4n1AOEU-NQyNmM1"
channel_link = "https://t.me/alert34234"
# Connect to server
client = TelegramClient(session="session/user",api_id=params.api_id,api_hash=params.api_hash)
client.start(phone=params.user_phone)
import sys
import_paths = sys.path
print(import_paths)

async def get_users(entity):
    users = await client.get_participants(entity)
    return users

async def get_messages(entity):
    messages = []
    async for message in client.iter_messages(entity): messages.append(message)
    return messages

async def get_draft(entity):
    draft = await client.get_drafts(entity)
    return draft

async def get_dialogs():
    dialogs = await client.get_dialogs()
    return dialogs

async def main():
    # Check if client is connected
    if client.is_connected():
        entity = await client.get_entity(group_link)
        channel_entity = await client.get_entity(channel_link)

        # Print list participant
        list_users = await get_users(entity)

        # Print list message
        list_messages = await get_messages(entity)

        # Print list draft
        drafts = await get_draft(entity)

        # Stats
        dialogs = await get_dialogs()

# client.run_until_disconnected()
client.loop.run_until_complete(main())