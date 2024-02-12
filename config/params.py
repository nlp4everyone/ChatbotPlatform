from dotenv import load_dotenv
import os
load_dotenv()
# Basic telethon params
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
interval_time = 60

# API params
coingecko_key = os.getenv("COINGECKO_KEY")
token_ids = os.getenv("TOKEN_IDS")

# Key
openai_key = os.getenv("OPENAI_KEY")

# User phone
user_phone = os.getenv("PHONE_NUMBER")