import os

API_ID=os.environ.get("API_ID"),
API_HASH=os.environ.get("API_HASH"),
BOT_TOKEN=os.environ.get("BOT_TOKEN")
SESSION=os.environ.get("SESSION")

AUTO_DELETE = os.environ.get("AUTO_DELETE")
GROUPS = []
for grp in (os.environ.get("GROUPS").split()):
    GROUPS.append(int(grp))
DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
FSUB_CHANNEL = int(os.environ.get("FSUB_CHANNEL"))
CHANNEL_LINK = os.environ.get("CHANNEL_LINK")

# remove or add more as per your need
LIST = ["srt", "txt", "jpg", "jpeg", "png", "torrent", "html", "aio", "pdf", "zip"] 
