#(©)CodeXBotz
#Recoded By @Its_Tartaglia_Childe



import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8177755574:AAHmMVV4xl-vD11I8mwX8UXxkO7H2p0S8Pw")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28744454"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "debd37cef0ad1a1ce45d0be8e8c3c5e7")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002362863690"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6266529037"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://jeffreymosesdj:Jeffrey@cluster2.cuiux.mongodb.net/?retryWrites=true&w=majority&appName=Cluster2")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster2")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1002076655534"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1002397319343"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://envs.sh/cQ8.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/jyP.jpg")

HELP_TXT = "<b>Hi Dude!\nThis is an file to link bot work for @Anime_Weekends\n\n❏ Bot Cammands\n├/start : start the bot\n├/about : Our Information\n└/help : Help related Bot\n\n💥 Simply click on link and start the bot join both channels and try again thats it.....!\n\n🧑‍💻 Developed by <a href=https://t.me/JeffreySama>Jҽϝϝɾҽყ ʂαɱα</a></b>"

ABOUT_TXT = "<b>⟦⟧ Hi There {first}!💫\n┏━━━━━━━❪❂❫━━━━━━━━\n◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/JeffreySama>Jҽϝϝɾҽყ ʂαɱα</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/Anime_Weekends>ᴀɴɪᴍᴇ ᴡᴇᴇᴋᴇɴᴅs</a>\n◈ ᴏɴɢᴏɪɴɢ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Ongoing_Weekends>ᴏɴɢᴏɪɴɢ ᴡᴇᴇᴋᴇɴᴅs</a>\n◈ Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>\n◈ ᴍʏ ꜱᴇʀᴠᴇʀ : <a href=https://dashboard.heroku.com>Heroku</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/JeffreySama>Jҽϝϝɾҽყ ʂαɱα</a>\n┗━━━━━━━❪❂❫━━━━━━━━</b>"

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ᴀʀᴀ ᴀʀᴀ... {first}! ❤\n\nɪ ᴀᴍ ᴍᴜʟᴛɪ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ , ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ » @Ongoing_Weekends")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6266529037").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ᴀʀᴀ ᴀʀᴀ {first}!❤\n\n🫧 ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ʙᴏᴛʜ ᴏꜰ ᴏᴜʀ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ...!\n\nʜᴀᴘᴘɪɴᴇss ᴀs ᴀ ᴍᴏᴛʜᴇʀ ᴀɴᴅ ʜᴀᴘᴘɪɴᴇss ᴀs ᴀɴ ɪᴅᴏʟ. ɪᴛ ᴍɪɢʜᴛ ʙᴇ ɴᴏʀᴍᴀʟ ᴛᴏ ʜᴀᴠᴇ ᴏɴʟʏ ᴏɴᴇ ʙᴜᴛ ɪ ᴡᴀɴᴛ ʙᴏᴛʜ..")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "​ᴀʀᴀ!! ᴀʀᴀ!! ɪᴀᴍ ᴏɴʟʏ ᴡᴏʀᴋ ғᴏʀ ᴍʏ ʟᴏᴠᴇʟʏ ᴋᴀᴡᴀɪɪ 🥰 @JeffreySama !"

ADMINS.append(OWNER_ID)
ADMINS.append(6266529037)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
