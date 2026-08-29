import sys

from config import X1, OWNER_ID, SUDO_USERS, CMD_HNDLR as hl
from pyrogram import enums
from os import execl
from telethon import events
from datetime import datetime


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id == enums.ChatMemberStatus.ADMINISTRATOR or enums.ChatMemberStatus.OWNER:
        start = datetime.now()
        altron = await e.reply(f"🐙")
        end = datetime.now()
        mp = (end - start).microseconds / 1000
        await altron.edit(f"✦ ᴘɪɴɢ sᴛᴀᴛs ⏤͟͟͞͞★\n➥ `{mp} ᴍꜱ`")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        await e.reply(f"✦ `ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ...`")
        try:
            await X1.disconnect()
        except Exception:
            pass

        execl(sys.executable, sys.executable, *sys.argv)


@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
async def addsudo(event):
    if event.sender_id == OWNER_ID:
        ok = await event.reply(f"✦ ᴀᴅᴅɪɴɢ ᴜꜱᴇʀ ᴀꜱ ꜱᴜᴅᴏ...")

        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except Exception:
            await ok.edit("✦ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ.")
            return

        if target in SUDO_USERS:
            await ok.edit(f"✦ ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ !!")
        else:
            SUDO_USERS.append(target)
            await ok.edit(f"✦ **ɴᴇᴡ ꜱᴜᴅᴏ ᴜꜱᴇʀ** ➥ `{target}`\n\n⚠️ ɴᴏᴛᴇ: ᴛʜɪꜱ ɪꜱ ᴛᴇᴍᴘᴏʀᴀʀʏ ᴀɴᴅ ᴡɪʟʟ ʀᴇꜱᴇᴛ ᴏɴ ʀᴇꜱᴛᴀʀᴛ. ᴜᴘᴅᴀᴛᴇ ꜱᴜᴅᴏ_ᴜꜱᴇʀꜱ ᴇɴᴠ ᴠᴀʀ ᴏɴ ʀᴀɪʟᴡᴀʏ ꜰᴏʀ ᴘᴇʀᴍᴀɴᴇɴᴛ.")

    elif event.sender_id in SUDO_USERS:
        await event.reply("✦ ꜱᴏʀʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")
