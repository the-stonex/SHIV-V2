
from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from VIPMUSIC import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

SHLOK = ["Jai shree ram"]

# Command
SHLOK_COMMAND = ["Shloka", "Shlok", "shloka", "Gita", "shlok", "gita"]

@app.on_message(
    filters.command(SHLOK_COMMAND)
    & filters.group
    )
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(SHLOK),
        
    )

@app.on_message(
    filters.command(SHLOK_COMMAND)
    & filters.private
    )
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(SHLOK),
        
)

