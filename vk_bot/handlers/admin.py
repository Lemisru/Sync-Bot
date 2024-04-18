from vkbottle.dispatch.rules.base import CommandRule
from vkbottle.bot import BotLabeler

from config import VK_PREFIXES
from vk_bot.isReplyTo import isReplyTo

import configparser

admin = configparser.ConfigParser()
config = configparser.ConfigParser()

admin_labeler = BotLabeler()

@admin_labeler.message(CommandRule("конфиг", VK_PREFIXES, 3))
async def reactions_handler(message, args: tuple):
    if args[0] != "изменить":
        return
    
    admin.read("data/admins.ini")
    admin["ADMINS"]

    admin_IDes = [int(key) for key in admin["ADMINS"]]
    if message.from_id in admin_IDes:
        config.read("config.ini")
        if args[1] in [key for key in config["VK"]]:
            config["VK"][args[1]] = args[2]
        else:
            await message.answer("Данного конфига не существует", reply_to=isReplyTo(message.id))
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        await message.answer("Конфиг успешно изменён", reply_to=isReplyTo(message.id))
    else:
        await message.answer("Без админки хуй тебе", reply_to=isReplyTo(message.id))
