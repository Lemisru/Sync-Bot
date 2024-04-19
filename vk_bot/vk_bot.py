from vkbottle.bot import Bot

from config import *

import vk_bot.handlers.admin as admin

import vk_bot.handlers.reactions as reactions
import vk_bot.handlers.articles as articles
import vk_bot.handlers.professions as professions

from loguru import logger
import sys
logger.remove()
logger.add(sys.stderr, level="INFO")

labeler.load(admin.admin_labeler)

labeler.load(reactions.reactions_labeler)
labeler.load(professions.professions_labeler)
labeler.load(articles.articles_labeler)

bot = Bot(api=API, labeler=labeler)

def getBot():
    global bot

    return bot

def vk_start():
    bot.run_forever()