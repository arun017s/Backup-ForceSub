import os

API_ID=int(os.environ.get("API_ID"))
API_HASH=os.environ.get("API_HASH")
BOT_TOKEN=os.environ.get("BOT_TOKEN")
SESSION=os.environ.get("SESSION")

GROUPS = []
for grp in (os.environ.get("GROUPS").split()):
    GROUPS.append(int(grp))

AUTO_DELETE = bool(os.environ.get("AUTO_DELETE"))
DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
FSUB_CHANNEL = int(os.environ.get("FSUB_CHANNEL"))
CHANNEL_LINK = os.environ.get("CHANNEL_LINK")

"""
Files with these extensions will not copied to DB_CHANNEL 
Remove or add more extensions as per your need
"""
LIST = ['srt', 'txt', 'jpg', 'jpeg', 'png', 'torrent', 'html', 'aio', 'pdf', 'zip', 'mp3', 'rar', 'apk', 'm4a', 'aac', 'wav', 'flac', 'wma']
