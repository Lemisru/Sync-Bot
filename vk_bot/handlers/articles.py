from vkbottle.dispatch.rules.base import CommandRule
from vkbottle.bot import BotLabeler

from config import VK_PREFIXES
from vk_bot.isReplyTo import isReplyTo

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

def createMessage(ping: str, type, num, text, punishment) -> str:
    answer = \
        f"""🤷‍♂Сегодня {ping}
            приговаривается к  статье {num} {type} - {text}.

            👮‍♂Наказание - {punishment}.
            
            🎆Мусора бляди!✨🎉"
            """

    return answer

article_types = {"🚗ПДД РФ🚗": "data/articles/pdd.txt", "УК РФ": "data/articles/uk.txt"}

@articles_labeler.message(CommandRule("моя статья", VK_PREFIXES))
async def articles_handler(message):
    user = await vk_bot.bot.api.users.get(message.from_id)
    ping = f"[{message.from_id}|{user[0].first_name} {user[0].last_name}]"

    article_type = random.choice(list(article_types))
    link = article_types[article_type]

    article_list = random.choice(getArticlesData(link))

    answer = createMessage(ping, article_type, *article_list)

    await message.answer(answer, reply_to=isReplyTo(message.id))

@articles_labeler.message(CommandRule("моя статья ук", VK_PREFIXES))
async def pdd_articles_handler(message):
    user = await vk_bot.bot.api.users.get(message.from_id)
    ping = f"[{message.from_id}|{user[0].first_name} {user[0].last_name}]"

    link = article_types["УК РФ"]

    article_list = random.choice(getArticlesData(link))

    answer = createMessage(ping, "УК РФ", *article_list)

    await message.answer(answer, reply_to=isReplyTo(message.id))

@articles_labeler.message(CommandRule("моя статья пдд", VK_PREFIXES))

async def uk_articles_handler(message):
    user = await vk_bot.bot.api.users.get(message.from_id)
    ping = f"[{message.from_id}|{user[0].first_name} {user[0].last_name}]"

    link = article_types['🚗ПДД РФ🚗']

    article_list = random.choice(getArticlesData(link))

    answer = createMessage(ping, "🚗ПДД РФ🚗", *article_list)

    await message.answer(answer, reply_to=isReplyTo(message.id))