from telethon import TelegramClient
from config import params
from modules.telegram_module.crypto_bot_handler import *
from modules.telegram_module.base import base_button

# Login
client = TelegramClient(session="session/crypto_bot",api_id=params.api_id,api_hash=params.api_hash)
client.start(bot_token=params.bot_token)
group_link = -4196966879
delay_time = 30

# Define event handler
event_handlers = [start_chat_handler,price_chart_handler,marketcap_chart_handler,callback_query_handler]
# Add event
for handler in event_handlers: client.add_event_handler(handler)

async def loop_function(entity,delay_time=delay_time):
    while True:
        await client.send_message(entity=entity,message="Hello from hell")
        await asyncio.sleep(delay_time)

async def main():
    # Loop
    entity = await client.get_entity(group_link)
    await loop_function(entity)

# client.send_file()
# Run the server
print("Run the server")
# client.loop.run_until_complete(main())
client.run_until_disconnected()