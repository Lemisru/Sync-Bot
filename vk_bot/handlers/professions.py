from vk_bot.AsyaCommandRule import AsyaCommandRule
from vkbottle.bot import BotLabeler

from config import Config
from data import database

from vk_bot.isReplyTo import isReplyTo

from vk_bot.handlers.admin import getUserRank

import random

import vk_bot.vk as vk

professions_labeler = BotLabeler()

professions = database.professions

graphics = ["График '2 через 2'", "Скользящий график", "Удаленная работа", "График как пойдёт"]

@professions_labeler.message(AsyaCommandRule(Config().VK_PREFIXES, ["моя профессия", "моя работа", "профессия", "работа"]))
async def professions_handler(message):
    user = await vk.getBot().api.users.get(message.from_id)
    profession = random.choice(professions.get_professions()).profession
    answer = (f"✅Сегодня [id{message.from_id}|{user[0].first_name} {user[0].last_name}]"
              f"устроился на новую работу👷‍♂: \n\n"
              f"{profession}!\n\n"
              f"💰Зарплата {random.randint(1,40)*5} 000₽/мес.\n"
              f"📊{random.choice(graphics)}.\n\n" 
              f"🎆НУ ЕСТЬ ЖЕ НАЛИВАЙ!✨🎉")

    await message.answer(answer, reply_to=isReplyTo(message.id))

@professions_labeler.message(AsyaCommandRule(Config().VK_PREFIXES, ['профессия добавить <profession>', 'добавить профессию <profession>',
                                                                    'работа добавить <profession', 'добавить работу <profession>']))
async def professions_add_handler(message, profession):
    permission_level = Config().permissions['professions']['add']
    user_rank = getUserRank(message.from_id)
    if user_rank < permission_level:
        answer = (
            f"📝Для добавления профессии нужен {permission_level}-й ранг админки\n"
            f"У вас - {user_rank}-й"
        )
        await message.answer(answer, reply_to=isReplyTo(message.id))

    professions.add_professions(profession)

    await message.answer(f"Профессия {profession} успешно добавлена", reply_to=isReplyTo(message.id))
    
