from vkbottle.dispatch.rules.base import CommandRule
from vk_bot.AsyaCommandRule import AsyaCommandRule
from vkbottle.bot import BotLabeler

from config import VK_PREFIXES
from vk_bot.isReplyTo import isReplyTo

import configparser

admin = configparser.ConfigParser()
config_parser = configparser.ConfigParser()

admin_labeler = BotLabeler()

def isAdmin(user_id):
    admin.read("data/admins.ini")

    admin_IDes = [int(key) for key in admin["ADMINS"]]
    if user_id in admin_IDes:
        return True
    return False

@admin_labeler.message(AsyaCommandRule(VK_PREFIXES, ["конфиг инфа", "настройки инфа", "админка инфа", "админ инфа"]))
async def config_info_handler(message):
    config_parser.read("config.ini")

    answer = "Вот информация о конфиге:\n"
    for key in config_parser["VK"]:
        if key == 'token':
            answer += f"token=...\n"
            continue
        answer += f"{key}= {config_parser["VK"][key]}\n"
    await message.answer(answer, reply_to=isReplyTo(message.id))

@admin_labeler.message(AsyaCommandRule(VK_PREFIXES, ["конфиг изменить <parameter> <value>", "настройки изменить <parameter> <value>"]))
async def config_change_handler(message, parameter, value):
    if not isAdmin(message.from_id):
        await message.answer("Без админки хуй тебе", reply_to=isReplyTo(message.id))
        return
    
    config_parser.read("config.ini")
    if parameter not in config_parser["VK"]:
        await message.answer("Данного конфига не существует", reply_to=isReplyTo(message.id))
        return
    
    config_parser["VK"][parameter] = value

    with open('config.ini', 'w') as configfile:
        config_parser.write(configfile)
        
    await message.answer(f"Конфиг {parameter} успешно поменял значение на {value}", reply_to=isReplyTo(message.id))
