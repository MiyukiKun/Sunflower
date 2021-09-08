from pyrogram import Client as Bot
from sunutils import group_call
from pytgcalls import idle
import logging
import config
from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID, SESSION_NAME
import time
import asyncio

loop = asyncio.get_event_loop()


bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers")
)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)
logger = logging.getLogger('__name__') 


print("Ohto Ai: Starting.....!!!")

bot.start()
group_call.start()
idle()