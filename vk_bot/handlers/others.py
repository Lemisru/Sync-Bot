from vkbottle.bot import BotLabeler

from vk_bot.AsyaCommandRule import AsyaCommandRule
from config import VK_PREFIXES
from vk_bot.isReplyTo import isReplyTo

import random

others_labeler = BotLabeler()

@others_labeler.message(AsyaCommandRule(VK_PREFIXES, ["помощь", "команды"]))
async def others_handler(message):
    answer =  "⚙ Полный список команд доступен по ссылке: https://vk.com/@async_bot-commands"
    await message.answer(answer, reply_to=isReplyTo(message.id))

@others_labeler.message(AsyaCommandRule(VK_PREFIXES, "пинг"))
async def others_handler(message):
    await message.answer("понг", reply_to=isReplyTo(message.id))

@others_labeler.message(AsyaCommandRule(VK_PREFIXES, ["скажи <text>","повтори <text>"]))
async def others_handler(message, text):
    await message.answer(text)

@others_labeler.message(AsyaCommandRule(VK_PREFIXES, ["сделай русским <text>","русский <text>"]))
async def zov_handler(message, text):
    new_text = text.replace('з', 'Z')

    new_text = new_text.replace('в', 'V')
    new_text = new_text.replace('З', 'Z')
    new_text = new_text.replace('В', 'V')

    await message.answer(new_text)

@others_labeler.message(AsyaCommandRule(VK_PREFIXES, ["выбери число от <num1> до <num2>"],
                                                     ["число от <num1> до <num2>"]))
async def randint_handler(message, num1, num2):
    await message.answer(random.randint(num1, num2), reply_to=isReplyTo(message.id))

@others_labeler.message(AsyaCommandRule(VK_PREFIXES, ["выбери из <text>", "выбери <text>"]))
async def randint_handler(message, text):
    text_list = text.split(",")
    word = random.choice(text_list)
    await message.answer(f"Я выберу: {word}", reply_to=isReplyTo(message.id))

@others_labeler.message(AsyaCommandRule(VK_PREFIXES, ["данет <text>", 'магический шар <text>']))
async def randint_handler(message, text):
    phrases = ['Ещё как', 'Очень вероятно', 'Мало шансов', 'Есть сомнения', 
               'Спроси позже','Нет','Да','Духи говорят да','Непонятно',
               'Без сомнений','Возможно','Думаю нет','Думаю да']
    
    await message.answer(random.choice(phrases), reply_to=isReplyTo(message.id))