# (C) Arunkumar Shibu 

# January 15th 2022

import os
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from helpers import copy_msg, force_sub

FSUB_CHANNEL = int(os.environ.get("FSUB_CHANNEL"))

Bot = Client(session_name="forwardfsub",
             api_id=int(os.environ.get("API_ID")),
             api_hash=os.environ.get("API_HASH"),
             bot_token=os.environ.get("BOT_TOKEN"))


@Bot.on_message(filters.private & filters.command("start"))
async def start(bot, message):
    await message.reply(f"<b>Hello {message.from_user.mention}</b>")

@Bot.on_message(filters.group)
async def group(bot, message):
    try:
       await force_sub(bot, message)
       if message.document or message.video:
           await copy_msg(message)
       else:
           return
    except Exception as e:
       print(e)
 
@Bot.on_callback_query(filters.regex("checksub"))  
async def checksub(bot, update):
    try:
       user=update.message.reply_to_message.from_user.id
    except:
       user=update.from_user.id
    if update.from_user.id==user:
       try:
          member = await bot.get_chat_member(FSUB_CHANNEL, user)          
       except UserNotParticipant:
          await update.answer("Aysheri 😏\nJoin in channel!", show_alert=True)
       except Exception as e:
            print(e)
       else:
           await bot.restrict_chat_member(chat_id=msg.chat.id, 
                                          user_id=msg.from_user.id,
                                          permissions=ChatPermissions(can_send_messages=True)
                                          )
           await update.message.edit(f"Hello {update.from_user.mention}!\nWelcome to {update.message.chat.title}")
    else:
       await update.answer("Wew 😳", show_alert=True)
    
Bot.run()
