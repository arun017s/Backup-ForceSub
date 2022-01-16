# (C) Arunkumar Shibu 

# January 15th 2022

import os
from pyrogram import Client, filters, idle
from pyrogram.types import ChatPermissions
from pyrogram.errors import UserNotParticipant
from helpers import copy_msg, force_sub

FSUB_CHANNEL = int(os.environ.get("FSUB_CHANNEL"))
SESSION = os.environ.get("SESSION")
GROUPS = os.environ.get("GROUPS").split()

Bot = Client(session_name="forwardfsub",
             api_id=int(os.environ.get("API_ID")),
             api_hash=os.environ.get("API_HASH"),
             bot_token=os.environ.get("BOT_TOKEN"),
             workers=300)
# 🥲
User = Client(session_name=SESSION,
              api_id=int(os.environ.get("API_ID")),
              api_hash=os.environ.get("API_HASH"),
              workers=300)

@Bot.on_message(filters.private & filters.command("start"))
async def start(bot, message):
    await message.reply(f"<b>Hello {message.from_user.mention}</b>")

@Bot.on_message(filters.group)
async def fsub(bot, message):
    try:
       await force_sub(bot, message)       
    except Exception as e:
       print(e)

@User.on_message(filters.document & filters.video) 
async def forward(user, message):
#    if str(message.chat.id) in GROUPS:
        try:
           await copy_msg(message)
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
           await bot.restrict_chat_member(chat_id=update.message.chat.id, 
                                          user_id=user,
                                          permissions=ChatPermissions(can_send_messages=True,
                                                                      can_send_media_messages=True,
                                                                      can_send_other_messages=True)
                                          )
           await update.message.edit(f"Hello {update.from_user.mention}!\nWelcome to {update.message.chat.title}")
    else:
       await update.answer("Wew 😳", show_alert=True)
    
User.start()
print("Userbot Started!")
Bot.start()
print("Bot Started!")

idle()

User.stop()
print("Userbot Stopped!")
Bot.stop()
print("Bot Stopped!")
