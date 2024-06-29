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
BOT_TOKEN = "7261995052:AAG0ZvjxEYeTW6ygmaO7ps3FCOthuZpJwa8"
SESSION = "BQF8ClsAasqXDYFzK2C6L8yDTn4KOEwpVj5NaXxHgLjJdlEm2fNjGHvsTZj7ge__fy5hHykTHbJ4k2LUOc2ies1JiRaSDIxl6g5aWlXnHwGwYV0AG0ief-mM6-ZD0erCVz04FrusEj9dabg86ygY1JRobNOYfW6X-NJqL8nlZi6bnVn7H1fgtyWv6_JxJMhsU3msSWREkwiGKH2HKGA4G5pwHH30H1R6F7uwOYu4fY_LbqmJ0M0OtMfyeVFa5JQ2aBMm9R77m_uQYGmQ5VMCtgsv1tOoDSf6K9gOSwgp2N2FwLkpyXQMBwwdmTtpWaxwZerAbsSC_-9hCXQudECFGVxjugDgYwAAAAF27pmmAA"
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
