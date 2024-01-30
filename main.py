import telethon,asyncio
from telethon import TelegramClient,events
api_id = 27112116
api_hash = "50684ff8e8317189889a0dba51ab6560"
phone_number = "+84868919926"
channel_name = "@soy_sniperbot"
token_address = "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"
id_crypto = "-2001134144"
client = TelegramClient(session="anon",api_id=api_id,api_hash=api_hash).start(phone=phone_number)
from telethon.tl.types import ChannelParticipantsAdmins

async def main():
    if client.is_connected():
        pass
        #me = await client.get_me()
        # Basics infor of channel soy
        #entity = await client.get_entity("https://t.me/JoneStone86_bot")
        #print(entity)
        #client.iter_participants()

        # async for user in client.iter_participants(chat, filter=ChannelParticipantsAdmins):
        #     print(user.first_name)

    # async for message in client.iter_messages('-2001134144'):
    #     print(message.id, message.text)
    # # Send buy message
    # await client.send_message(channel_name,message="/buy")
    # # Delay 1 second
    # await asyncio.sleep(1)
    # # Send token
    # await client.send_message(channel_name,message=token_address)
    #
    # await asyncio.sleep(1)
    # # Get entity
    # async for message in client.iter_messages(channel_name):
    #     print(message.chat.title, message.text)
@client.on(events.NewMessage(incoming=True,chats = [6772754199]))
async def reply(event):
    print(event)
client.run_until_disconnected()
#client.loop.run_until_complete(main())