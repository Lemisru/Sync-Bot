from vk_bot.AsyaCommandRule import AsyaCommandRule
from vkbottle.bot import BotLabeler

from config import Config 
from vk_bot.isReplyTo import isReplyTo

from data import database

admin_labeler = BotLabeler()

def getUserRank(user_id):
    user_rank = database.get_user_by_id(user_id).rank

    if user_rank is None:
        user_rank = 0

    return True

@admin_labeler.message(AsyaCommandRule(Config().VK_PREFIXES, ["конфиг инфа", "настройки инфа", "админка инфа", "админ инфа"]))
async def config_info_handler(message):
    pass

@admin_labeler.message(AsyaCommandRule(Config().VK_PREFIXES, ["конфиг инфа", "настройки инфа", "админка инфа", "админ инфа"]))
async def config_info_handler(message):
    answer =f"config_change_level: :\n"
