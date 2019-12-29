""".admin Plugin for @apnatimechaltahai """
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba, check pinned in @XtraTgBot"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**`Jis race se mujhe nikaalne ki baat kar rahe hai yeh bewakoof ... woh nahi jaante hai ... us race ka sikandar main hoon  ψ(｀∇´)ψ`**\n\n"
                     "`milte hai crew challenge me yad rakhna Nikhil \nINDIA IS GREAT\n`Crew Challenge: #4 Rank holder\n\nAlways with you, my master!\n`"
                     f"`My peru owner`: {DEFAULTUSER}\n"
                     "[Deploy this userbot Now](https://github.com/yoyonikhil/timeisup)")
