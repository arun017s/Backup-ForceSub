# (C) Arunkumar Shibu 

# January 15th 2022

import os
import asyncio
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import ChatPermissions

DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
FSUB_CHANNEL = int(os.environ.get("FSUB_CHANNEL"))
CHANNEL_LINK = os.environ.get("CHANNEL_LINK")

LIST = ["srt", "txt", "jpg", "jpeg", "png", "torrent", "html", "aio", "pdf", "zip"]

async def copy_msg(msg):
    file = msg.document or msg.video
    name = file.file_name.split(".")[-1]
    if name in LIST: 
       return
    else:
       try:
           await msg.copy(CHANNEL)
       except FloodWait as e:
           await asyncio.sleep(e.x)
           await msg.copy(CHANNEL)
           

async def force_sub(bot, msg):
    if msg.from_user.is_bot:
       return
    else:
       try:
          member = await bot.get_chat_member(FSUB_CHANNEL, msg.from_user.id)
          if member.status == "banned":
            await msg.reply(f"Sorry {msg.from_user.mention}!\n You are banned in our channel, you will be banned from here within 10 seconds")
            await asyncio.sleep(10)
            await bot.ban_chat_member(msg.chat.id, msg.from_user.id)
       except UserNotParticipant:
            await bot.restrict_chat_member(chat_id=msg.chat.id, 
                                           user_id=msg.from_user.id,
                                           permissions=ChatPermissions(can_send_messages=False)
                                           )
            await msg.reply(f"Hello {msg.from_user.mention}!\n\nYou have to join in our channel to message here", 
                            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔥 Join Channel 🔥", url=CHANNEL_LINK)],
                                                               [InlineKeyboardButton("♻️ Try Again ♻️", callback_data="checksub")]])
                            )
       except Exception as e:
            print(e)

    
