from vkbottle.bot import Bot

from config import Config, labeler

from vk_bot.handlers import *

from loguru import logger
import sys
logger.remove()
logger.add(sys.stderr, level="INFO")

bot = Bot(api=Config().VK_API, labeler=labeler)

def getBot():
    global bot

    return bot

def vk_start():
    bot.run_forever()