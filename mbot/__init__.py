"""MIT License

Copyright (c) 2022 Daniel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from pyrogram import Client
from os import environ,sys,mkdir,path
import logging
import requests
from flask import Flask
from threading import Thread
import pytz
import time
from apscheduler.schedulers.background import BackgroundScheduler
from sys import executable
#from Python_ARQ import ARQ
from aiohttp import ClientSession
from dotenv import load_dotenv
import shutil 
load_dotenv("config.env")
import os 
# Log
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(message)s",
    handlers = [logging.FileHandler('bot.log'), logging.StreamHandler()]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

# Mandatory Variable
try:
    API_ID = int(environ['API_ID'])
    API_HASH = environ['API_HASH']
    BOT_TOKEN = environ['BOT_TOKEN']
    OWNER_ID = int(environ['OWNER_ID'])
except KeyError:
    LOGGER.debug("One or More ENV variable not found.")
    sys.exit(1)
# Optional Variable
F_SUB = environ.get('F_SUB',False)
F_SUB_CHANNEL_ID = environ.get('F_SUB_CHANNEL_ID')
F_SUB_CHANNEL_INVITE_LINK = environ.get('F_SUB_CHANNEL_INVITE_LINK')
SUDO_USERS = environ.get("SUDO_USERS",str(OWNER_ID)).split()
SUDO_USERS = [int(_x) for _x in SUDO_USERS]
if OWNER_ID not in SUDO_USERS:
    SUDO_USERS.append(OWNER_ID)
AUTH_CHATS = environ.get('AUTH_CHATS',None ).split()
AUTH_CHATS = [int(_x) for _x in AUTH_CHATS]
LOG_GROUP = environ.get("LOG_GROUP", None)
if LOG_GROUP:
    LOG_GROUP = int(LOG_GROUP)
BUG = environ.get("BUG", None)
if BUG:
    BUG = int(BUG)
genius_api = environ.get("genius_api",None)
if genius_api:
    genius_api = genius_api
  # this code is removed :)
 #try:
 #   ARQ_API_KEY = environ['ARQ_API_KEY']
 #   ARQ_API_URL = "https://arq.hamker.in"
 #   aiohttpsession = ClientSession()
 #   arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)

#except Exception as e:
#    pass
#    print(f"python arq key is not a valid string skiping it ...! Reason:{e}")
#   aiohttpsession = ClientSession()
#    arq = None
def paste(text):
    try:
        url = "https://spaceb.in/api/"
        res = requests.post(url, json={"content": text, "extension": "txt"})
        return f"https://spaceb.in/{res.json()['payload']['id']}"
    except Exception:
        url = "https://dpaste.org/api/"
        data={'format': 'json',
            'content': text.encode('utf-8'),
            'lexer': 'python',
            'expires': '604800', #expire in week
            }
        res = requests.post(url,data=data)
        return res.json()["url"]
    
class Mbot(Client):
    def  __init__(self):
        name = self.__class__.__name__.lower()
        super().__init__(
            ":memory:",
            plugins=dict(root=f"{name}/plugins"),
            workdir= "", #"./cache/",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            sleep_threshold=30
        )
    async def start(self):
      #  os.system(f"rm -rf ./cache/")
     #   os.system(f"mkdir ./cache/")
        global BOT_INFO
        await super().start()
        BOT_INFO = await self.get_me()
        if not path.exists('/tmp/thumbnails/'):
            mkdir('/tmp/thumbnails/')
        for chat in AUTH_CHATS:
            await self.send_photo(chat,"https://telegra.ph/file/97bc8a091ac1b119b72e4.jpg","**Spotify Download Started**")
        LOGGER.info(f"Bot Started As {BOT_INFO.username}\n")
    
    async def stop(self,*args):
        await super().stop()
        LOGGER.info("Bot Stopped, Bye.")
        

# =============================[ UPTIME ISSUE FIXED ]================================#


RENDER_EXTERNAL_URL = environ.get("RENDER_EXTERNAL_URL", "http://localhost:5000")

def ping_self():
    url = f"{RENDER_EXTERNAL_URL}/alive"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logging.info("Ping successful!")
        else:
            logging.error(f"Ping failed with status code {response.status_code}")
    except Exception as e:
        logging.error(f"Ping failed with exception: {e}")

def start_scheduler():
    scheduler = BackgroundScheduler(timezone=pytz.utc)
    scheduler.add_job(ping_self, 'interval', minutes=3)
    scheduler.start()

app = Flask(__name__)

@app.route('/alive')
def alive():
    return "I am alive!"

def run_flask():
    app.run(host='0.0.0.0', port=10000)

Thread(target=run_flask).start()
start_scheduler()
