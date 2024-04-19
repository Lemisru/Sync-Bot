from vkbottle.dispatch.rules.base import CommandRule
from vkbottle.bot import BotLabeler

from config import VK_PREFIXES
from vk_bot.isReplyTo import isReplyTo

import random

import vk_bot.vk_bot as vk_bot

professions_labeler = BotLabeler()

professions = []
with open("data/professions.txt", 'r', encoding="utf-8") as f:
    [professions.append(i.rstrip("\n")) for i in f.readlines()]

graphics = ["График '2 через 2'", "Скользящий график", "Удаленная работа", "График как пойдёт"]

@professions_labeler.message(CommandRule("моя профессия", VK_PREFIXES))
async def professions_handler(message):
    user = await vk_bot.getBot().api.users.get(message.from_id)
    answer = f"✅Сегодня [id{message.from_id}|{user[0].first_name} {user[0].last_name}] "
    answer += f"устроился на новую работу👷‍♂: \n\n{random.choice(professions)}!\n\n"
    answer += f"💰Зарплата {random.randint(1,40)*5} 000₽/мес.\n 📊{random.choice(graphics)}.\n\n 🎆Поздравляем!✨🎉"

    await message.answer(answer, reply_to=isReplyTo(message.id))