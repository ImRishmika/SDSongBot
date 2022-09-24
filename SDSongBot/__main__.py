#SDBOTs <https://t.me/SDBOTs_Inifinity>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from SDSongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from SDSongBot import SDbot as app
from SDSongBot import LOGGER

pm_start_text = """
👋 Hey [{}](tg://user?id={}), \n\n **I'm Emo Song Downloader Bot**
**Now send me the song name you want to download**
     
Example : ```/song Faded```
      
Powerd By @EmoBotDevolopers ⚡ 
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        text="⚡ Channel ⚡ ", url="https://t.me/EmoBotDevolopers"
                    ),
                    InlineKeyboardButton(
                        text="👨‍💻 Devoloper 👨‍💻", url="https://t.me/ImRishmika"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("""
Emo  Song Downloader is Online !""")
idle()
