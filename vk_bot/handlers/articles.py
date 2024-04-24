from vk_bot.AsyaCommandRule import AsyaCommandRule
from vkbottle.bot import BotLabeler

from config import VK_PREFIXES
from vk_bot.isReplyTo import isReplyTo
from vk_bot.handlers.admin import isAdmin

import random

import vk_bot.vk_bot as vk_bot

articles_labeler = BotLabeler()

def getArticlesData(file_path: str) -> list:
    output = []

    with open(file_path, 'r', encoding="utf-8") as f:
        for i in f.readlines():
            line = i.rstrip("\n").split("|")
            output.append(line)
    return output

def createMessage(ping: list, type, num, text, punishment) -> str:
    answer = (f"🤷‍♂Сегодня {ping} \n"
              f"приговаривается к статье {num} {type} - {text}\n\n"
              f"👮‍♂Наказание{punishment}.\n\n" 
              f"🎆Мусора бляди!✨🎉")

    return answer

article_types = {"🚗ПДД РФ🚗": "data/articles/pdd.txt", "УК РФ": "data/articles/uk.txt"}

@articles_labeler.message(AsyaCommandRule(VK_PREFIXES, ["моя статья", "статья", "наказание", "мое наказание"]))
async def articles_handler(message):
    user = await vk_bot.bot.api.users.get(message.from_id)
    ping = f"[id{message.from_id}|{user[0].first_name} {user[0].last_name}]"

    code_type = random.choice(list(article_types))
    link = article_types[code_type]

    article_list = random.choice(getArticlesData(link))

    num, text, punishment  = article_list

    answer = createMessage(ping, code_type, num, text, punishment)

    await message.answer(answer, reply_to=isReplyTo(message.id))

@articles_labeler.message(AsyaCommandRule(VK_PREFIXES, ["моя статья ук", "статья ук", "наказание ук", "мое наказание ук"]))
async def pdd_articles_handler(message):
    user = await vk_bot.bot.api.users.get(message.from_id)
    ping = f"[id{message.from_id}|{user[0].first_name} {user[0].last_name}]"

    link = article_types["УК РФ"]

    article_list = random.choice(getArticlesData(link))
    num, text, punishment = article_list

    answer = createMessage(ping, "УК РФ", num, text, punishment)

    await message.answer(answer, reply_to=isReplyTo(message.id))

@articles_labeler.message(AsyaCommandRule(VK_PREFIXES, ["моя статья пдд", "статья пдд", "наказание пдд", "мое наказание пдд"]))

async def uk_articles_handler(message):
    user = await vk_bot.bot.api.users.get(message.from_id)
    ping = f"[id{message.from_id}|{user[0].first_name} {user[0].last_name}]"

    link = article_types['🚗ПДД РФ🚗']

    article_list = random.choice(getArticlesData(link))
    num, text, punishment = article_list

    answer = createMessage(ping, "🚗ПДД РФ🚗", num, text, punishment)

    await message.answer(answer, reply_to=isReplyTo(message.id))