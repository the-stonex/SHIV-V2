import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)
from config import LOGGER_ID as LOG_GROUP_ID
from VIPMUSIC import app  

photo = [
    "",
    "",
    "",
    "",
    "",
]


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)
            username = message.chat.username if message.chat.username else "ᴘʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴘ"
            msg = (
                f"**ᴍᴜsɪᴄ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ ɴᴇᴡ ɢʀᴏᴜᴘ #ɴᴇᴡ_ɢʀᴏᴜᴘ**\n\n"
                f"**ᴄʜᴀᴛ ɴᴀᴍᴇ:** {message.chat.title}\n"
                f"**ᴄʜᴀᴛ ɪᴅ:** {message.chat.id}\n"
                f"**ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ :** @{username}\n"
                f"**ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs:** {count}\n"
                f"**ᴀᴅᴅᴇᴅ ʙʏ:** {message.from_user.mention}"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"😍ᴀᴅᴅ ᴍᴇ ɪɴ ᴍᴏʀᴇ😍", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))



@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = f"✫ <b><u>#𝐋ᴇғᴛ_𝐆ʀᴏᴜᴘ</u></b> ✫\n\n𝐂ʜᴀᴛ 𝐓ɪᴛʟᴇ : {title}\n\n𝐂ʜᴀᴛ 𝐈ᴅ : {chat_id}\n\n𝐑ᴇᴍᴏᴠᴇᴅ 𝐁ʏ : {remove_by}\n\n𝐁ᴏᴛ : @{app.username}"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)

#welcome

@app.on_message(filters.new_chat_members, group=3)
async def _greet(_, message):    
    chat = message.chat
    
    for member in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"**ʜᴇʏ {message.from_user.mention} 𝐖ᴇʟᴄᴏᴍᴇ ɪɴ  {message.chat.title} **\n\n"
                f"**ᴄʜᴀᴛ ɴᴀᴍᴇ:** {message.chat.title}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ:** @{message.chat.username}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**ᴜsᴇʀɪᴅ:** {message.from_user.id}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**ᴜsᴇʀ ɴᴀᴍᴇ:** @{message.from_user.username}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**ᴄᴏᴍᴘʟᴇᴛᴇᴅ {count} ᴍᴇᴍʙᴇʀs🎉**"
            )
            await app.send_photo(message.chat.id, photo=random.choice(photo), caption=msg, )

#tagall
