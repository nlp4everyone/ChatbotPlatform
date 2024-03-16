import random

from telethon import TelegramClient
from config import params
from services.telegram_service.defi_test.defi_test_handler import *
from modules.io_modules.pandas_modules import CsvModules
import asyncio
from telethon import events

# Connect to server
client = TelegramClient(session="session/user",api_id=params.api_id,api_hash=params.api_hash)
client.start(phone=params.user_phone)

# Read csv
df = CsvModules.read_csv("data/question_testcase.csv")
question_column = df["Unnamed: 2"]
key_column = df["Unnamed: 1"]
# Get index
index = df.isin(['Question about token']).any(axis=1).idxmax()
sorted_column = question_column.iloc[index:]
# Remove NaN
sorted_column = sorted_column.to_list()

event_index = 0
# async def main():
#     me = await client.get_entity("https://t.me/intenttrade_devbot")
#     print(me)

@client.on(events.MessageEdited(incoming=True,from_users=[6952885362]))
async def new_message_handler(event):
    global event_index
    chat = event.chat
    # Important parameter
    message = event.message.message
    if not len(message) <= 3:
        print(message)
        await client.send_message(chat,sorted_column[event_index])
        event_index += 1
        if event_index == len(sorted_column):
            raise Exception("Rate all test case")


    # # Send message back
    # async with client.action(chat, 'typing') as action:
    #     # Get question
    #     question = sorted_column[event_index]
    #     await client.send_message(chat,question)

async def main():
    entity = await client.get_entity("https://t.me/intenttrade_devbot")
    while True:
        await client.send_message(entity,"Hello")
        await asyncio.sleep(60)




# client.loop.run_until_complete(main())
print("Run server")
client.loop.run_until_complete(main())
