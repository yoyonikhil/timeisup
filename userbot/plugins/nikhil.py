m telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba, check pinned in @apnatimechaltahai"

@command(outgoing=True, pattern="^.nikhil$")
async def amireallyalive(tca):
    """ For .nikhil command, check if the bot is running.  """
    await nikhil.edit(" apna time aayega kabhi na kabhi\milte hai ab next crew challenge mein \bye\bye\TO ALL\n`"
                     f"`My peru owner`: {DEFAULTUSER}\n"
                     "[Deploy this userbot Now](https://github.com/yoyonikhil/timeisup)")""".admin Plugin for @apnatimechaltahai """
