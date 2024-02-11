from telethon import TelegramClient
from config import params
from modules.telegram_module.base_handler import *

# Login
client = TelegramClient(session="bot",api_id=params.api_id,api_hash=params.api_hash)
client.start(bot_token=params.bot_token)

# Add event handler
event_handlers = [chat_action_handler,callback_query_handler,new_message_handler,
                  message_read_handler,message_deleted_handler,
                  user_update_handler,user_update_handler]
for handler in event_handlers: client.add_event_handler(handler)

# Run the server
print("Run the server")
client.run_until_disconnected()