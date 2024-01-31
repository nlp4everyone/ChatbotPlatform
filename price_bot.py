import telethon,asyncio,time
from telethon import TelegramClient,events
from config import params
from tools.api import CoingeckoAPI
client = TelegramClient(session="bot",api_id=params.api_id,api_hash=params.api_hash).start(bot_token=params.bot_token)
# Bot only listen on this group
group_id = 4123501748

# Event handle
@client.on(events.NewMessage(incoming=True,chats=group_id,pattern="/start"))
async def command_start(event):
    start_message = """
    Hello to Price Predictor Group. I'm here for supporting you everything about price 	\U0001F471 
    """
    # Get chat info
    chat = await event.get_chat()
    # Get message info
    message = event.message

    # Send message
    # await client.send_message(entity=chat,message=start_message,reply_to=message.id)
    # Send image
    await client.send_file(entity=chat,file='img/start.png',caption=start_message,reply_to=message.id)

@client.on(events.NewMessage(incoming=True,chats=group_id,pattern="/price"))
async def ask_price(event):
    market_history = CoingeckoAPI.get_market_history() # Including prices,market caps and total volumes
    # Price
    list_price = market_history['prices']
    # Market caps
    list_marketcap = market_history['market_caps']
    # Total volumes
    list_totalvolumes = market_history['total_volumes']
    # Get chat info
    chat = await event.get_chat()
    # Get message info
    message = event.message

    # Send message
    # await client.send_message(entity=chat,message=start_message,reply_to=message.id)
    # Send image
    # await client.send_file(entity=chat,file='img/start.png',caption=start_message,reply_to=message.id)

# Say greeting to new member
@client.on(events.ChatAction())
async def greet_new_member(event):
    # Welcome every new user
    if event.user_joined:
        print(event.user)
        await event.reply('Welcome to the group!')

# Main thread, invoke action after interval time
async def main():
    # Get channel entity
    entity = await client.get_entity(params.channel_link)
    while True:
        # pass
        await client.send_message(entity=entity, message="Hello")
        # # Sleep after interval time
        await asyncio.sleep(params.interval_time)

print("Run the server!")
client.loop.run_until_complete(main())

