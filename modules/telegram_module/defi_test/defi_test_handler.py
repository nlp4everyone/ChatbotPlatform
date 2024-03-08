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



