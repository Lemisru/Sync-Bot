from vkbottle.bot import Bot
from vkbottle.dispatch.rules.base import CommandRule

from config import API, labeler

import vk_bot.handlers.reactions as reactions
import vk_bot.handlers.admin as admin
import vk_bot.handlers.professions as professions

labeler.load(reactions.reactions_labeler)
labeler.load(admin.admin_labeler)
labeler.load(professions.professions_labeler)

bot = Bot(api=API, labeler=labeler)

def getBot():
    global bot

    return bot

def vk_start():
    bot.run_forever()