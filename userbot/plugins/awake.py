import os
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME , CMD_HELP
from userbot.utils import admin_cmd
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events , errors , custom
import io
from platform import python_version , uname

ALIVE_PIC = Config.ALIVE_PHOTTO
if ALIVE_PIC is None :
    ALIVE_PIC = "https://telegra.ph/file/27429a8aa60255b15f77e.jpg"

DEFAULTUSER = str ( ALIVE_NAME ) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

ALIVE_MESSAGE = Config.ALIVE_MSG
ALIVE_MESSAGE = "**MASTEROID IS AWAKE... \n\n\n**"
ALIVE_MESSAGE += "`My Bot Status \n\n\n`"
ALIVE_MESSAGE += "`Default User Interface: KDE Plasma \n\n`"
if ALIVE_MESSAGE is None :
    ALIVE_MESSAGE = "**MASTEROID IS AWAKE \n\n\n**"
    ALIVE_MESSAGE += "`My Bot Status \n\n\n`"
    ALIVE_MESSAGE += "`Default User Interface: KDE Plasma \n\n`"
    ALIVE_MESSAGE += f"`ᎷᎽ ᏰᏫᏕᏕ`: {DEFAULTUSER} \n\n "


# @command(outgoing=True, pattern="^.awake$")
@borg.on ( admin_cmd ( pattern=r"awake" ) )
async def amireallyalive ( awake ) :
    """ For .awake command, check if the bot is running.  """
    await awake.delete ()
    await borg.send_file ( awake.chat_id , ALIVE_PIC , caption=ALIVE_MESSAGE )
