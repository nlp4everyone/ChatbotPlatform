from dotenv import load_dotenv
import os
load_dotenv()
# Basic telethon params
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
interval_time = 60

# API params
current_price_url = os.getenv("PRICE_URL")
history_crypto_url = os.getenv("HISTORY_URL")

# Key
openai_key = os.getenv("OPENAI_KEY")

# Chanel params
channel_link = "https://t.me/alert34234"