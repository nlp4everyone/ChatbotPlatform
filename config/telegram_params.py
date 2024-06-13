from dotenv import load_dotenv
import os
load_dotenv()
# Basic telethon params
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

# User phone
user_phone = os.getenv("PHONE_NUMBER")

# default folder
session_dir = "sessions_folder"
audio_dir = "cached_voices_folder"
image_dir = "cached_photos_folder"
video_dir = "cached_videos_folder"
interval_time = 60