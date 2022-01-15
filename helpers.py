# (C) Arunkumar Shibu 

# January 15th 2022

import os
import asyncio
from pyrogram.errors import FloodWait

CHANNEL = int(os.environ.get("CHANNEL"))

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
           
    
