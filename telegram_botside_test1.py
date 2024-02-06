from telethon import TelegramClient,events
from config import params
from service import run_prompt
from service.exchange_api import CoingeckoAPI
client = TelegramClient(session="bot",api_id=params.api_id,api_hash=params.api_hash).start(bot_token=params.bot_token)
# Bot only listen on this group
group_id = 4123501748
group_link = ""

instruction = "Transfer this text to Chinese:"
# Event handle
# @client.on(events.NewMessage(incoming=True))
# async def command_start(event):
#     print(event.text)
#     if not str(event.text).startswith('/instruct'):
#         start_message = """
#         Hello to Price Predictor Group. I'm here for supporting you everything about price 	\U0001F471
#         """
#         # Get chat info
#         chat = await event.get_chat()
#
#         # Get message info
#         message = event.message
#         group_info = await client.get_entity("https://t.me/testanser")
#         print(instruction)
#
#         # Send message
#         await client.send_message(entity=group_info,message=start_message)

@client.on(events.NewMessage(incoming=True))
async def command_start(event):
    global instruction
    # Get chat info
    chat = await event.get_chat()
    group_info = await client.get_entity("https://t.me/testanser")

    if str(event.text).startswith("/instruct"):
        # Get message info
        # Remove text
        removed_index = str(event.text).index("/instruct") + len("/instruct")
        # Remove index
        input_text = str(event.text)[removed_index:]
        # Strip text
        input_text = input_text.strip()
        instruction = input_text
        # Send message back
        await client.send_message(chat,f"Update instruction: {instruction}")
    else:
        question = event.text
        # print(f"Question:{question}")
        # print(f"Instruction:{instruction}")
        # Return answer
        anwser = run_prompt.get_answer(question,instruction)
        # Send answer to group
        await client.send_message(chat,f"Send : {anwser} to group")

        # Send out answer
        await client.send_message(entity=group_info, message=anwser)
    # Send message
    # await client.send_message(entity=group_info, message=start_message)


print("Run the server!")
# client.loop.run_until_complete(main())
client.run_until_disconnected()

# client.loop.run_until_complete(main())