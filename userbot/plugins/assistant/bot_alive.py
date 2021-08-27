from telethon import events

from userbot import ALIVE_NAME, bot

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "MASTEROID"
PM_IMG = "https://telegra.ph/file/27429a8aa60255b15f77e.jpg"
pm_caption = "➥ **MASTEROID IS:** `ONLINE`\n\n"
pm_caption += f"➥ **My Boss** : {DEFAULTUSER} \n"
pm_caption += "➥ **License** : [GNU General Public License v3.0](github.com/DARK-COBRA/DARKCOBRA/blob/master/LICENSE)\n"
pm_caption += "➥ **Copyright** : By [MASTEROID](https://t.me/Masteroid_Channel)\n"
pm_caption += "[Assistant By MASTEROID](https://t.me/MASTEROID_SUPPORT)"

# only Owner Can Use it
@tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
