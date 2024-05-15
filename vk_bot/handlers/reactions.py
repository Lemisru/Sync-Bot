from vk_bot.AsyaCommandRule import AsyaCommandRule
from vkbottle.bot import BotLabeler

from config import Config
from vk_bot.ping_utils import isReplyTo

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

@reactions_labeler.message(AsyaCommandRule(Config().VK_PREFIXES, ["реакция", "стикер", "эмодзи", "смайлик", "смайл"]))
async def reactions_handler(message):
    sticker = random.choice(list(stickers))

    await message.answer(sticker_id=sticker)