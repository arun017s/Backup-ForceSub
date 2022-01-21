# (C) Arunkumar Shibu 

# January 15th 2022

from pyrogram import Client, filters, idle
from helpers import copy_msg, force_sub, check_fsub, auto_delete
from info import API_ID, API_HASH, BOT_TOKEN, SESSION, GROUPS, AUTO_DELETE

Bot = Client(session_name="backup-fsub", 
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300)
# 🥲
User = Client(session_name=SESSION, 
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300)
 
@Bot.on_message(filters.private & filters.command("start"))
async def start(bot, message):
    await message.reply(f"<b>Hello {message.from_user.mention}!\nI will forward all files from your groups to backup channel\nAlso you can use me as a ForceSubscribe Bot!\n\nYou can make your own bot from this [SOURCE CODE](https://github.com/Arun-TG/Backup-ForceSub)</b>",
                        disable_web_page_preview=True)

@Bot.on_message(filters.chat(GROUPS))
async def fsub(bot, message):
    try:
       await force_sub(bot, message)       
    except Exception as e:
       print(e)

@User.on_message(filters.chat(GROUPS) & ~filters.edited) 
async def user_bot(user, message):
    if message.document or message.video:      
        try:
           await copy_msg(message)
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
