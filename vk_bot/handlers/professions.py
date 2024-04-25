from vk_bot.AsyaCommandRule import AsyaCommandRule
from vkbottle.bot import BotLabeler

from config import VK_PREFIXES
from vk_bot.isReplyTo import isReplyTo

from vk_bot.handlers.admin import isAdmin

import random

import vk_bot.vk_bot as vk_bot

professions_labeler = BotLabeler()

professions = []
with open("data/professions.txt", 'r', encoding="utf-8") as f:
    [professions.append(i.rstrip("\n")) for i in f.readlines()]

graphics = ["График '2 через 2'", "Скользящий график", "Удаленная работа", "График как пойдёт"]

@professions_labeler.message(AsyaCommandRule(VK_PREFIXES, ["профессия добавить <profession>","работа добавить <profession>",
                                                           "добавить профессию <profession>", "добавить работу <profession>"]))
async def professions_handler(message, profession):
    if not isAdmin(message.from_id):
        await message.answer("Без админки низя добавлять профессии", reply_to=isReplyTo(message.id))
        return
    
    with open("data/professions.txt",'r') as f:
        professions = [i.rstrip("\n") for i in f.readlines()]

    if profession.title() in professions:
        await message.answer(f"Профессия \"{profession.title()}\" уже есть в списке", reply_to=isReplyTo(message.id))
        return

    with open("data/professions.txt", 'a') as f:
        f.write(f"\n{profession.title()}")

    await message.answer(f"Профессия \"{profession.title()}\" успешно добавлена", reply_to=isReplyTo(message.id))

@professions_labeler.message(AsyaCommandRule(VK_PREFIXES, ["моя профессия", "моя работа", "профессия", "работа"]))
async def professions_handler(message):
    user = await vk_bot.getBot().api.users.get(message.from_id)
    answer = (f"✅Сегодня [id{message.from_id}|{user[0].first_name} {user[0].last_name}] \n"
              f"устроился на новую работу👷‍♂: \n\n"
              f"{random.choice(professions)}!\n\n"
              f"💰Зарплата {random.randint(1,40)*5} 000₽/мес.\n"
              f"📊{random.choice(graphics)}.\n\n" 
              f"🎆НУ ЕСТЬ ЖЕ НАЛИВАЙ!✨🎉")


    await message.answer(answer, reply_to=isReplyTo(message.id))