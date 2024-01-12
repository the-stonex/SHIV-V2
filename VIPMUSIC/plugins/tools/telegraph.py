from telegraph import upload_file
from pyrogram import filters
from VIPMUSIC import app
from pyrogram.types import InputMediaPhoto


@app.on_message(filters.command(["tgm" ,"telegraph", "link"]))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("ᴜᴘʟᴏᴀᴅɪɴɢ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x

        i.edit(f' ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴘʜ ᴜʀʟ {url}')
