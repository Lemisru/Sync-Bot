from vkbottle.bot import Bot, Message
from vkbottle.dispatch.rules.base import CommandRule

from vk_bot.isReplyTo import isReplyTo
from config import VK_PREFIXES, API, labeler

from vk_bot.handlers.reactions import *
from vk_bot.handlers.admin import *

labeler.load(reactions_labeler)
labeler.load(admin_labeler)

bot = Bot(api=API, labeler=labeler)

def vk_start():
    bot.run_forever()