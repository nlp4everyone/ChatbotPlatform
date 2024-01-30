from dotenv import load_dotenv
import os
load_dotenv()
# Basic telethon params
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
interval_time = 60

# API params
price_url = os.getenv("PRICE_URL")

# Chanel params
channel_link = "https://t.me/alert34234"