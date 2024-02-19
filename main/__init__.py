#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 24906331
API_HASH = "866e8e4637fb269388b50202fb0f169c"
BOT_TOKEN = "6058803397:AAFMCpgYhyjOs7_pCdTt-p-P4DPs1_hxi2E"
SESSION = "BQF8ClsAotLsLtDQzQeuwl9x7zck-eu7y8C2KtoYpztjQnhAZxExjv5Fs_ofwXtvbU1KeZ0Fxa_yXwNru08L9FREn7ASBO_sPuc2q1d2H9PzJFq4iI2g5TNQgrVvZ3ZMiRcDT3fc6balyPIrKTv9uqA7LTgBYFxKSOM5IxY7oA4u8O9mcuJgEbQJbDx8n85xNm_RQ3UbYkr0eKTQk9FbwArHdM5Jn5Q9t0GoDycC8U6yDLMLuZaBRT3vryJqnRiO0kMNcpl86j9NNY5cEAjZnh-7xRAm5VDKm0mahmNcvUIJNSmGWecYqw9EvZT3PZbsdgUHFMh6ZPw9LtneU35t2wTiVD58sgAAAAF27pmmAA"
FORCESUB = "savereeee"
AUTH = 6290315686

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
