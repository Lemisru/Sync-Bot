from vkbottle.dispatch.rules.base import CommandRule
from vkbottle.bot import BotLabeler

from config import VK_PREFIXES
from vk_bot.isReplyTo import isReplyTo

import configparser

admin = configparser.ConfigParser()
config = configparser.ConfigParser()

admin_labeler = BotLabeler()

def isAdmin(user_id):
    admin_IDes = [int(key) for key in admin["ADMINS"]]
    if user_id in admin_IDes:
        return True
    return False

@admin_labeler.message(CommandRule("конфиг инфо", VK_PREFIXES))
async def reactions_handler(message):
    config.read("config.ini")

    answer = "Вот информация о конфиге:\n"
    for key in config["VK"]:
        if key == 'token':
            answer += f"token=...\n"
            continue
        answer += f"{key}= {config["VK"][key]}\n"
        print(answer)
    await message.answer(answer, reply_to=isReplyTo(message.id))

@admin_labeler.message(CommandRule("конфиг изменить", VK_PREFIXES, 2))
async def reactions_handler(message, args: tuple):
    admin.read("data/admins.ini")

    if isAdmin(message.from_id):
        config.read("config.ini")
        if args[0] in [key for key in config["VK"]]:
            config["VK"][args[0]] = args[1]

            with open('config.ini', 'w') as configfile:
                config.write(configfile)
            await message.answer("Конфиг успешно изменён", reply_to=isReplyTo(message.id))
        else:
            await message.answer("Данного конфига не существует", reply_to=isReplyTo(message.id))
    else:
        await message.answer("Без админки хуй тебе", reply_to=isReplyTo(message.id))
