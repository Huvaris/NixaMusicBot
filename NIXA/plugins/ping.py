import os

from telethon import Button, events

from NIXA import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/ed8051b0e0a2f844b2373.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@give_up_to_god"
)

CAPTION = f"**ð£ ð¢ ð¡ ð ð **\n\n   Â» {ms}\n   Â» á´Ê á´á´sá´á´Ê ~ã{ALIVE}ã"


@NIXA.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[
             Button.url("â¢ sá´á´á´á´Êá´ â¢", url="https://t.me/FRIENDS_DRAMA_CLUB"),
             Button.url("â¢ á´á´á´á´á´á´s â¢", url="https://t.me/TechQuard")
                       ]]
    await NIXA.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
