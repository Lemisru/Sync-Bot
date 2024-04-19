from vkbottle.dispatch.rules.base import CommandRule
from vkbottle.bot import BotLabeler

from config import VK_PREFIXES
from vk_bot.isReplyTo import isReplyTo

import random

import vk_bot.vk_bot as vk_bot

articles_labeler = BotLabeler()

def getArticlesList(file_path: str) -> list:
    output = []

    with open(file_path, 'r', encoding="utf-8") as f:
        for i in f.readlines():
            line = i.rstrip("\n").split("|")
            output.append(line)
    return output

def createMessage(user_data: list, type, num, text, punishment) -> str:
    answer = f"🤷‍♂Сегодня [id{user_data[0]}|{user_data[1]} {user_data[1]}] "
    answer += f"приговаривается к  статье {num} {type} - {text}.\n\n"
    answer += f"👮‍♂Наказание - {punishment}.\n\n 🎆Мусора бляди!✨🎉"

    return answer

types = {"🚗ПДД РФ🚗": "data/articles/pdd.txt", "УК РФ": "data/articles/uk.txt"}

@articles_labeler.message(CommandRule("моя статья", VK_PREFIXES))
async def articles_handler(message):
    user = await vk_bot.getBot().api.users.get(message.from_id)
    article_type = random.choice(["🚗ПДД РФ🚗", "УК РФ"])
    article_list = random.choice(getArticlesList(types[article_type]))

    answer = createMessage([message.from_id, user[0].first_name, user[0].last_name], article_type, *article_list)

    await message.answer(answer, reply_to=isReplyTo(message.id))

@articles_labeler.message(CommandRule("моя статья ук", VK_PREFIXES))
async def articles_handler(message):
    user = await vk_bot.getBot().api.users.get(message.from_id)
    article = random.choice(getArticlesList(types['УК РФ']))

    answer = createMessage([message.from_id, user[0].first_name, user[0].last_name], "УК РФ", *article)

    await message.answer(answer, reply_to=isReplyTo(message.id))

@articles_labeler.message(CommandRule("моя статья пдд", VK_PREFIXES))
async def articles_handler(message):
    user = await vk_bot.getBot().api.users.get(message.from_id)
    article = random.choice(getArticlesList(types['🚗ПДД РФ🚗']))

    answer = createMessage([message.from_id, user[0].first_name, user[0].last_name], "🚗ПДД РФ🚗", *article)

    await message.answer(answer, reply_to=isReplyTo(message.id))