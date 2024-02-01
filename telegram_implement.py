import telethon,asyncio,time
from telethon import TelegramClient,events
from config import params
from tools import preprocess,streaming

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
    # Get chat info
    chat = await event.get_chat()
    # Get message info
    message = event.message

    # Get market history
    market_history = CoingeckoAPI.get_market_history() # Including prices,market caps and total volumes
    # Price
    list_price = market_history['prices']
    # Market caps
    list_marketcap = market_history['market_caps']
    # Total volumes
    list_totalvolumes = market_history['total_volumes']


    # Send message
    # await client.send_message(entity=chat,message=start_message,reply_to=message.id)
    # Send image
    # await client.send_file(entity=chat,file='img/start.png',caption=start_message,reply_to=message.id)
async def one_iteration(entity,message):
    await client.edit_message(entity=entity,message=message)

@client.on(events.NewMessage(incoming=True,chats=group_id,pattern="/stream"))
async def test_streaming(event):
    test_message = ("Cao Cao, courtesy name Mengde, was a Chinese statesman, warlord, and poet who rose to power towards the end of the Eastern Han dynasty (c. 184–220) and became the effective head of the Han central government during that period. "
                    "He laid the foundation for what was to become the state of Cao Wei (220–265), established by his son and successor Cao Pi, who ended the Eastern Han dynasty and inaugurated the Three Kingdoms period (220–280). Beginning in his own lifetime, a corpus of legends developed around Cao Cao which built upon his talent, his cruelty, and his perceived eccentricities.")
    tokenized_text = preprocess.basic_tokenize(test_message)
    output = streaming.stream(tokenized_text)
    # Get chat info
    chat = await event.get_chat()
    response = await client.send_message(entity=chat,message= "Thinking...")
    # await asyncio.sleep(1)
    # await client.edit_message(entity=response,message="Hello")
    # tasks = [one_iteration(response,out) for out in output]
    # await asyncio.gather(*tasks)
    for out in output:
        # print(out)
        await asyncio.sleep(0.2)
        await client.edit_message(entity=response,message=out)



# Say greeting to new member
@client.on(events.ChatAction())
async def greet_new_member(event):
    # Welcome every new user
    if event.user_joined:
        print(event.user)
        await event.reply('Welcome to the group!')

# Main thread, invoke action after interval time
# async def main():
#     # Get channel entity
#     entity = await client.get_entity(params.channel_link)
#     while True:
#         # pass
#         # await client.send_message(entity=entity, message="Hello")
#         # # Sleep after interval time
#         await asyncio.sleep(params.interval_time)

print("Run the server!")
# client.loop.run_until_complete(main())
client.run_until_disconnected()
