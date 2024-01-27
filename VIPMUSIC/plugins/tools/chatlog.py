import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)
from config import LOGGER_ID as LOG_GROUP_ID
from VIPMUSIC import app  

photo = [
    "https://telegra.ph/file/5d33ec7c387985d78352b.jpg",
"https://telegra.ph/file/3095010ce25b4c55f9823.jpg",
"https://telegra.ph/file/62de4fe21cc8575298dd9.jpg",
"https://telegra.ph/file/62de4fe21cc8575298dd9.jpg",
"https://telegra.ph/file/6f93dcaa2c5943253c149.jpg",
"https://telegra.ph/file/cbbfe284b42c403a6bbbd.jpg",
"https://telegra.ph/file/6f93dcaa2c5943253c149.jpg",
"https://telegra.ph/file/2e909e7dd709b380918f7.jpg",
"https://telegra.ph/file/7f0490e53d3cce83504af.jpg",
"https://telegra.ph/file/842c0a55f982d30fe4f48.jpg",
"https://telegra.ph/file/585cfc47e2240f2ca3dce.jpg",
"https://telegra.ph/file/2329f335339f63b2bbd5c.jpg"
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
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg,)



@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = f"✫ <b><u>#𝐋ᴇғᴛ_𝐆ʀᴏᴜᴘ</u></b> ✫\n\n𝐂ʜᴀᴛ 𝐓ɪᴛʟᴇ : {title}\n\n𝐂ʜᴀᴛ 𝐈ᴅ : {chat_id}\n\n𝐑ᴇᴍᴏᴠᴇᴅ 𝐁ʏ : {remove_by}\n\n𝐁ᴏᴛ : @{app.username}"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)


