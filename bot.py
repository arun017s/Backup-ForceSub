# (C) Arunkumar Shibu 

# January 15th 2022

import os
from pyrogram import Client, filters, idle
from helpers import copy_msg, force_sub, check_fsub, auto_delete

FSUB_CHANNEL = int(os.environ.get("FSUB_CHANNEL"))
SESSION = os.environ.get("SESSION")
GROUPS = []
for grp in (os.environ.get("GROUPS").split()):
       ADMINS.append(int(grp))

AUTO_DELETE = os.environ.get("AUTO_DELETE")


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
    await message.reply(f"<b>Hello {message.from_user.mention}!\nI will forward all files from your groups to backup channel\nAlso you can use me as a ForceSubscribe Bot!\n\nYou can make your own bot from this [SOURCE CODE](https://github.com/Arun-TG/Forward-Fsub)</b>",
                        disable_web_page_preview=True)

@Bot.on_message(filters.chat(GROUPS))
async def fsub(bot, message):
    try:
       await force_sub(bot, message)       
    except Exception as e:
       print(e)

@User.on_message(filters.chat(GROUPS)) 
async def user_bot(user, message):
    if message.document or message.video:      
        try:
           await copy_msg(Bot, message)
        except Exception as e:
           print(e) 
    if AUTO_DELETE == "True":
        try:
            await auto_delete(Bot, message)
        except Exception as e:
            print(e) 
      
@Bot.on_callback_query(filters.regex("checksub"))  
async def try_again(bot, update):
    try:
       await check_fsub(bot, update)
    except Exception as e:
           print(e) 
   
User.start()
print("Userbot Started!")
Bot.start()
print("Bot Started!")

idle()

User.stop()
print("Userbot Stopped!")
Bot.stop()
print("Bot Stopped!")
