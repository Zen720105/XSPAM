import asyncio

from config import X1, SUDO_USERS, CMD_HNDLR as hl
from pyrogram import enums
from datetime import datetime

from telethon import events


@X1.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
async def logs(legend):
    if legend.sender_id == enums.ChatMemberStatus.ADMINISTRATOR or enums.ChatMemberStatus.OWNER:
        await legend.reply(
            "✦ `ʟᴏɢꜱ ᴄᴏᴍᴍᴀɴᴅ ᴜɴᴀᴠᴀɪʟᴀʙʟᴇ`\n\n"
            "➥ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ʜᴏꜱᴛᴇᴅ ᴏɴ ʀᴀɪʟᴡᴀʏ, ᴄʜᴇᴄᴋ ʟᴏɢꜱ ᴅɪʀᴇᴄᴛʟʏ ꜰʀᴏᴍ ᴛʜᴇ ʀᴀɪʟᴡᴀʏ ᴅᴀꜱʜʙᴏᴀʀᴅ."
        )

    elif legend.sender_id in SUDO_USERS:
        await legend.reply("✦ ꜱᴏʀʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")
