
from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from VIPMUSIC import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

SHLOK = ["**कर्मण्येवाधिकारस्ते मा फलेषु कदाचन।\nमा कर्मफलहेतुर्भूर्मा ते सङ्गोऽस्त्वकर्मणि॥**\n\n**भावार्थ** : श्री कृष्ण समझाते है की केवल कर्म करना ही हमारे हाथ में है। कर्म द्वारा मिलने वाले फल हमारे हाथ में नहीं है। इसलिए निस्वार्थ हो कर सिर्फ अच्छे कर्म करने पर ही ध्यान देना चाहिए।","यदा यदा हि धर्मस्य ग्लानिर्भवति भारत।\nअभ्युत्थानमधर्मस्य तदात्मानं सृजाम्यहम्॥\n\n**अर्थात** : जब धर्म खतरे में आता है उस पर हानि पहुँचती है और अधर्म की वृद्धि होने लगती है। तब श्री कृष्ण अपने महा स्वरुप की रचना द्वारा आगे आते है।","**नैनं छिद्रन्ति शस्त्राणि नैनं दहति पावक: ।\nन चैनं क्लेदयन्त्यापो न शोषयति मारुत ॥**\n\nभावार्थ : श्रीमद भगवत गीता अनुसार आत्मा को कोई शस्त्र काट नहीं सकता, नाही किसी प्रकार की आग उसे जला सकती है। कोई पानी, हवा या आपत्ति भी आत्मा को मार नहीं सकती।","**यो न हृष्यति न द्वेष्टि न शोचति न काङ्‍क्षति।\nशुभाशुभपरित्यागी भक्तिमान्यः स मे प्रियः॥**\n\nअर्थात : जो न कभी हर्षित होता है, न द्वेष करता है, न शोक मनाता है, न कामना करता है तथा जो शुभ और अशुभ कर्मों का त्यागी है। ऐसा भक्तियुक्त पुरुष भगवान श्री कृष्ण को प्रिय है","**क्रोधाद्भवति संमोह: संमोहात्स्मृतिविभ्रम:।\nस्मृतिभ्रंशाद्बुद्धिनाशो बुद्धिनाशात्प्रणश्यति॥**\n\nभावार्थ : क्रोध से मनुष्य मर जाता है, यानी मूढ़ हो जाता है, जिसके परिणामस्वरूप स्मृति भ्रमित हो जाती है। स्मृति-भ्रम से मनुष्य की बुद्धि नष्ट हो जाती है, और बुद्धि नष्ट होने पर व्यक्ति खुद को नष्टता की तरफ ले जाता है।"]

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

