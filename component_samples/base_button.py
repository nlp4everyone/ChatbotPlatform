from telethon.tl.custom.button import Button
# Button text: Force user input already text
# Button url: Display url link
# Button auth: Access url with specific profile
# Button force reply : Force user to reply message

inline_button = Button.switch_inline(text="Hello",query="I'm here") # Not work

# Request phone and location ( Only works in private chat mode)
phone_button = Button.request_phone(text="Please insert phone number",resize=True)
location_button = Button.request_location(text="Please insert location",resize=True)

