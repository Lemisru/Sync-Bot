from vkbottle.dispatch.rules.base import CommandRule
from vkbottle.bot import BotLabeler

from config import VK_PREFIXES
from vk_bot.isReplyTo import isReplyTo

import random

reactions_labeler = BotLabeler()

stickers_intervals = []
with open("data/stickers.txt", 'r', encoding="utf-8") as f:
    for i in f.readlines():
        line = i.rstrip("\n").split("|")
        stickers_intervals.append( [int(line[1]), int(line[2])] )

stickers = set()
for interval in stickers_intervals:
    stickers.update(range(interval[0], interval[1]))

@reactions_labeler.message(CommandRule("реакция", VK_PREFIXES))
async def reactions_handler(message):
    sticker = random.choice(list(stickers))

    await message.answer(sticker_id=sticker)