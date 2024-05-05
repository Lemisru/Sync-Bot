from vk_bot.AsyaCommandRule import AsyaCommandRule
from vkbottle.bot import BotLabeler

from vk_bot import vk

from config import Config 
from data import database
from vk_bot.isReplyTo import isReplyTo
from vk_bot.handlers.admin import getUserRank

import random

articles_labeler = BotLabeler()

def getArticlesData(file_path: str) -> list:
    output = []

    with open(file_path, 'r', encoding="utf-8") as f:
        for i in f.readlines():
            line = i.rstrip("\n").split("|")
            output.append(line)
    return output

def createMessage(user, user_id, type, article_list) -> str:
    user_data = database.users.get_user_by_id(user_id)
    num, text, punishment = article_list

    user_name = None
    if user_data is not None:
        if user_data.name is not None:
            user_name = user_data.name
    
    if user_name is None:
        user_name = f"{user[0].first_name} {user[0].last_name}"

    ping = f"[id{user_id}|{user_name}]"
    answer = (f"🤷‍♂Сегодня {ping} "
              f"приговаривается к статье {num} {type} - {text}\n\n"
              f"👮‍♂Наказание{punishment}.\n\n" 
              f"🎆Мусора бляди!✨🎉")

    return answer

code_types = {"🚗ПДД РФ🚗": "data/articles/pdd.txt", "УК РФ": "data/articles/uk.txt"}

@articles_labeler.message(AsyaCommandRule(Config().VK_PREFIXES, ["моя статья", "статья", "наказание", "мое наказание"]))
async def articles_handler(message):
    user = await vk.bot.api.users.get(message.from_id)

    code_type = random.choice(list(code_types))
    link = code_types[code_type]
    article_list = random.choice(getArticlesData(link))

    answer = createMessage(user, message.from_id, code_type, article_list)

    await message.answer(answer, reply_to=isReplyTo(message.id))

@articles_labeler.message(AsyaCommandRule(Config().VK_PREFIXES, ["моя статья ук", "статья ук", "наказание ук", "мое наказание ук"]))
async def pdd_articles_handler(message):
    user = await vk.bot.api.users.get(message.from_id)

    link = code_types["УК РФ"]

    article_list = random.choice(getArticlesData(link))

    answer = createMessage(user, message.from_id, "УК РФ", article_list)

    await message.answer(answer, reply_to=isReplyTo(message.id))

@articles_labeler.message(AsyaCommandRule(Config().VK_PREFIXES, ["моя статья пдд", "статья пдд", 
                                                                 "наказание пдд", "мое наказание пдд"]))

async def uk_articles_handler(message):
    user = await vk.bot.api.users.get(message.from_id)

    link = code_types['🚗ПДД РФ🚗']

    article_list = random.choice(getArticlesData(link))

    answer = createMessage(user, message.from_id, "🚗ПДД РФ🚗", article_list)

    await message.answer(answer, reply_to=isReplyTo(message.id))