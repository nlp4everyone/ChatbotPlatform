from telethon import events
import asyncio
def group_type(event):
    output = "private"
    if event.is_channel:
        output = "channel"
    elif event.is_group:
        output = "group"
    return output

def action_type(event):
    result = "user_added"
    if event.user_joined:
        result = "user_joined"
    elif event.user_kicked:
        result = "user_kicked"
    elif event.user_left:
        result = "user_left"
    return result

@events.register(events.NewMessage())
async def new_message_handler(event):
    # New message handler
    print("New message handler")

    # Important parameter
    chat = await event.get_chat() # Get chat object
    message_object = event.message # Message object
    message_text = message_object.message # Message text
    pattern_match = event.pattern_match  # Pattern match

    # Define client
    client = event.client
    # Send message back
    async with client.action(chat, 'typing') as action:
        await asyncio.sleep(1)
        await client.send_message(chat,'Hello')

@events.register(events.UserUpdate())
async def user_update_handler(event):
    print("User update handler")
    # Message Edited handler
    print(dir(event))

    # Define client
    client = event.client

@events.register(events.MessageEdited())
async def message_edited_handler(event):
    print("Message Edited handler")
    # Message Edited handler
    print(dir(event))

    # Define client
    client = event.client

@events.register(events.MessageDeleted())
async def message_deleted_handler(event):
    print("Message Deleted handler")
    # Message Edited handler
    print(dir(event))

    # Define client
    client = event.client

@events.register(events.MessageRead())
async def message_read_handler(event):
    print("Message Read handler")
    # Message Read handler
    print(dir(event))

    # Define client
    client = event.client

@events.register(events.CallbackQuery())
async def callback_query_handler(event):
    print("Callback query handler")
    # Callback query handler
    print(dir(event))

    # Button click
    print(event.data)
    # Define client
    client = event.client

@events.register(events.ChatAction())
async def chat_action_handler(event):
    print("Chat Action handler")
    # ChatAction handler
    # Chat info
    chat_info = await event.chat

    # Action type
    action = action_type(event)
    # Get user infor
    user = event.user
    # Get the user id
    user_id = event.user_id
    # Get the entity of user who kick
    add_by = await event.get_added_by()
    # Get the entity of user who kick
    kicked_by = await event.get_kicked_by()

    # Define client
    client = event.client