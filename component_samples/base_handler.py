from telethon import events
import asyncio

@events.register(events.NewMessage())
async def new_message_handler(event):
    # New message handler
    print("New message handler")

    # Important parameter
    chat = await event.get_chat() # Get chat object
    # Define client
    client = event.client

    # Send message back
    async with client.action(chat, 'typing') as action:
        await client.send_message(chat,'Hello')

@events.register(events.UserUpdate())
async def user_update_handler(event):
    print("User update handler")
    # Message Edited handler

    # Important parameter
    chat = await event.get_chat()  # Get chat object
    # Define client
    client = event.client

    # Send message back
    async with client.action(chat, 'typing') as action:
        await client.send_message(chat, 'Hello')

@events.register(events.MessageEdited())
async def message_edited_handler(event):
    print("Message Edited handler")

    # Important parameter
    chat = await event.get_chat()  # Get chat object
    # Define client
    client = event.client

    # Send message back
    async with client.action(chat, 'typing') as action:
        await client.send_message(chat, 'Hello')

@events.register(events.MessageDeleted())
async def message_deleted_handler(event):
    print("Message Deleted handler")
    # Important parameter
    chat = await event.get_chat()  # Get chat object
    # Define client
    client = event.client

    # Send message back
    async with client.action(chat, 'typing') as action:
        await client.send_message(chat, 'Hello')

@events.register(events.MessageRead())
async def message_read_handler(event):
    print("Message Read handler")

    # Define client
    client = event.client

@events.register(events.CallbackQuery())
async def callback_query_handler(event):
    print("Callback query handler")

    # Important parameter
    chat = await event.get_chat()  # Get chat object
    # Define client
    client = event.client

    # Send message back
    async with client.action(chat, 'typing') as action:
        await client.send_message(chat, 'Hello')

@events.register(events.ChatAction())
async def chat_action_handler(event):
    print("Chat Action handler")
    # Important parameter
    chat = await event.get_chat()  # Get chat object
    # Define client
    client = event.client

    # Send message back
    async with client.action(chat, 'typing') as action:
        await client.send_message(chat, 'Hello')