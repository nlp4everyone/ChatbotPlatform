from telethon import TelegramClient
from config import params
from modules.telegram_module.defi_handler import *
from modules.telegram_module import base_button

# Login
client = TelegramClient(session="session/crypto_bot",api_id=params.api_id,api_hash=params.api_hash)
client.start(bot_token=params.bot_token)
group_link = -4196966879
delay_time = 30

# Define event handler
event_handlers = [new_message_handler]
# Add event
for handler in event_handlers: client.add_event_handler(handler)

# async def loop_function(entity,delay_time=delay_time):
#     while True:
#         await client.send_message(entity=entity,message="Hello from hell")
#         await asyncio.sleep(delay_time)

# client.send_file()
# Run the server
print("Run the server")
# client.loop.run_until_complete(main())
client.run_until_disconnected()