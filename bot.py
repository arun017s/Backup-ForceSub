# (C) Arunkumar Shibu 
# January 15th 2022

from info import *
from helpers import *
from pyrogram import Client, filters, idle

Bot = Client(name="bot", 
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300)

User = Client(name="user-bot",
              session_string=SESSION, 
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300)
 
@Bot.on_message(filters.private & filters.command("start"))
async def start(bot, message):
    await message.reply(f"<b>Hello {message.from_user.mention}!\nI will forward all files from your groups to backup channel\nAlso you can use me as a ForceSubscribe Bot!\n\nYou can make your own bot from this [SOURCE CODE](https://github.com/arun017s/Backup-ForceSub)</b>",
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
          await copy_msg(message)
       except Exception as e:
          print(e) 
    if AUTO_DELETE:
       try:
          await auto_delete(Bot, message)
       except Exception as e:
          print(e) 
      
@Bot.on_callback_query()  
async def callback(bot, update):
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
