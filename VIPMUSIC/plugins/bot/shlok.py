
from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from VIPMUSIC import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

SHLOK = ["**कर्मण्येवाधिकारस्ते मा फलेषु कदाचन
मा कर्मफलहेतुर्भूर्मा ते सङ्गोऽस्त्वकर्मणि

भावार्थ - श्री कृष्ण समझाते है की केवल कर्म करना ही हमारे हाथ में है कर्म द्वारा मिलने वाले फल हमारे हाथ में नहीं है  इसलिए निस्वार्थ हो कर सिर्फ अच्छे कर्म करने पर ही ध्यान देना चाहिए।**",]

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

