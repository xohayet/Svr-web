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
BOT_TOKEN = "7466801582:AAG7FaNRF7wR8-LwmQ9rJfLyh5osrio3yNU"
SESSION = "BQF8ClsAkTZsdZIQ9sR39WBsfo72WON6uqg0ieaXXpL6hKR0JDC8UCL1hdlKizsJgHhytRnz76CDeJo9Kx_lyHz2KjGD01FIQ2gL2wKKfcSIbquGLzKsfC6Dh06uTK-9Gh2Vb0KXzMVH_l5VMfGidgXR4utNyjJd4PjCSkmhaBXoLaUwtRVw1bclJ2Ss--kJ77jl9LqznyU28KdZ2SrfwnzoR4EB-W870bgLnrVS5czP_6V_asfj1svEEpARFWxSJoycHmZxQ5rtLpphKWWeA6RkKN8iu9ki0Hd-CwdT6z1xJtTeTKp-Agg8eSqnHr3lOj-21XIs2RlIKZ0xLwxds6fJn--BFwAAAAF27pmmAA"
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
