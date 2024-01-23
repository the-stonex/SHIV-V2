
from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from VIPMUSIC import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

SHLOK = [" ** कर्मण्येवाधिकारस्ते मा फलेषु कदाचन।
मा कर्मफलहेतुर्भूर्मा ते सङ्गोऽस्त्वकर्मणि॥**\n\nभावार्थ : श्री कृष्ण समझाते है की केवल कर्म करना ही हमारे हाथ में है। कर्म द्वारा मिलने वाले फल हमारे हाथ में नहीं है। इसलिए निस्वार्थ हो कर सिर्फ अच्छे कर्म करने पर ही ध्यान देना चाहिए।",
          "यदा यदा हि धर्मस्य ग्लानिर्भवति भारत।
अभ्युत्थानमधर्मस्य तदात्मानं सृजाम्यहम्॥\n\nअर्थात : जब धर्म खतरे में आता है उस पर हानि पहुँचती है और अधर्म की वृद्धि होने लगती है। तब श्री कृष्ण अपने महा स्वरुप की रचना द्वारा आगे आते है। ",""]

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

