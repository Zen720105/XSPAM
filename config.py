import logging

from telethon import TelegramClient

from os import getenv
from ROYEDITX.data import AVISHA


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR XBOTS
API_ID = 37096542
API_HASH = "e87f06819f9d2b3364502b978650568f"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
RAILWAY_APP_NAME = getenv("RAILWAY_APP_NAME", None)

BOT_TOKEN = getenv("BOT_TOKEN", default="8670466939:AAGkqOfWy6adbrUaGyU8wr7YhjO3zjNXZlw")


SUDO_USERS = [7812646657]
sudo_env = getenv("SUDO_USERS", default="7812646657").split()
for x in sudo_env:
    SUDO_USERS.append(int(x))
for x in AVISHA:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="7812646657"))
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
