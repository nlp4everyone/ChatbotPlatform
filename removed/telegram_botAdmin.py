from telethon import TelegramClient,events
from config import params
from modules.ai_module import run_prompt
from modules.api_module.exchange_api import CoingeckoAPI
client = TelegramClient(session="bot2",api_id=params.api_id,api_hash=params.api_hash).start(bot_token=params.bot_token)
# Bot only listen on this group
group_id = 4123501748
group_link = ""

instruction = "Transfer this text to English:"

@client.on(events.NewMessage(incoming=True))
async def command_start(event):
    global instruction
    # Get chat info
    chat = await event.get_chat()
    group_info = await client.get_entity("https://t.me/testanser")

    account = await client.get_entity("+84589263703")
    print(account)
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
        chain = run_prompt.get_answer(instruction)
        # Send answer to group
        # await client.send_message(chat,f"Send : {anwser} to group")



        # Send out answer
        # try:
        chat_entity = None
        text = ""
        # async for chunk in chain.astream({"question":question}):
        #     print(chunk)
            # if len(text) == 0:
            #     text += chunk
            #     chat_entity = await client.send_message(entity=group_info, message="Thinking..")
            # else:
            #     text += chunk
            #     await client.edit_message(entity=chat_entity, message=text)



        # except:
        #     print("You've not been in this group")
    # Send message
    # await client.send_message(entity=group_info, message=start_message)


print("Run the server!")
# client.loop.run_until_complete(main())
client.run_until_disconnected()

# client.loop.run_until_complete(main())