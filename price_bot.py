import telethon,asyncio,time
from telethon import TelegramClient,events
from config import params
client = TelegramClient(session="bot",api_id=params.api_id,api_hash=params.api_hash).start(bot_token=params.bot_token)
# Bot only listen on this group
group_id = 4123501748



# Event handle
@client.on(events.NewMessage(incoming=True,chats=group_id,pattern="/start"))
async def new_message(event):
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

